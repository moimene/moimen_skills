#!/bin/bash
# Ralph - Autonomous AI Agent Loop
# Based on https://github.com/snarktank/ralph

set -e

# Parse arguments
TOOL="amp"
MAX_ITERATIONS=10

while [[ "$#" -gt 0 ]]; do
  case $1 in
    --tool) TOOL="$2"; shift ;;
    --max) MAX_ITERATIONS="$2"; shift ;;
    *) MAX_ITERATIONS="$1" ;;
  esac
  shift
done

echo "🤖 Ralph - Autonomous Agent Loop"
echo "Tool: $TOOL | Max iterations: $MAX_ITERATIONS"
echo ""

# Check prerequisites
if ! command -v jq &> /dev/null; then
  echo "❌ jq is required. Install with: brew install jq"
  exit 1
fi

if [ ! -f "prd.json" ]; then
  echo "❌ prd.json not found. Create it first."
  exit 1
fi

# Create progress file if not exists
touch progress.txt

# Get branch from PRD
BRANCH=$(jq -r '.branchName' prd.json)
echo "📦 Branch: $BRANCH"

# Checkout branch
if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
  git checkout "$BRANCH"
else
  git checkout -b "$BRANCH"
fi

# Main loop
for i in $(seq 1 $MAX_ITERATIONS); do
  echo ""
  echo "═══════════════════════════════════════"
  echo "🔄 Iteration $i of $MAX_ITERATIONS"
  echo "═══════════════════════════════════════"
  
  # Find first story that hasn't passed
  STORY_ID=$(jq -r '.userStories[] | select(.passes == false) | .id' prd.json | head -1)
  
  if [ -z "$STORY_ID" ]; then
    echo ""
    echo "✅ All stories completed!"
    echo "<promise>COMPLETE</promise>"
    exit 0
  fi
  
  STORY_TITLE=$(jq -r --arg id "$STORY_ID" '.userStories[] | select(.id == $id) | .title' prd.json)
  echo "📝 Story: $STORY_ID - $STORY_TITLE"
  
  # Log iteration start
  echo "" >> progress.txt
  echo "=== Iteration $i ===" >> progress.txt
  echo "Story: $STORY_ID - $STORY_TITLE" >> progress.txt
  echo "Started: $(date -Iseconds)" >> progress.txt
  
  # Get story details for prompt
  STORY_JSON=$(jq --arg id "$STORY_ID" '.userStories[] | select(.id == $id)' prd.json)
  
  # Create iteration prompt
  PROMPT=$(cat << EOF
You are implementing story $STORY_ID from the PRD.

## Story Details
$STORY_JSON

## Instructions
1. Implement ONLY this story, nothing else
2. Write tests for the implementation
3. Run quality checks (typecheck, tests)
4. If checks fail, fix and retry
5. When done, update AGENTS.md with any learnings

## Quality Checks to Run
- npm run typecheck
- npm test

## Current Progress
$(tail -50 progress.txt)

## Important
- Keep changes minimal and focused
- Do not modify unrelated code
- Commit with message: feat($STORY_ID): [description]
EOF
)

  # Invoke AI tool
  echo "🧠 Invoking $TOOL..."
  
  if [ "$TOOL" = "claude" ]; then
    echo "$PROMPT" | claude-code
  else
    echo "$PROMPT" | amp
  fi
  
  # Run quality checks
  echo "🔍 Running quality checks..."
  
  if npm run typecheck && npm test; then
    echo "✅ Quality checks passed"
    
    # Commit changes
    git add .
    git commit -m "feat($STORY_ID): $STORY_TITLE" || true
    
    COMMIT_HASH=$(git rev-parse --short HEAD)
    
    # Mark story as passed
    jq --arg id "$STORY_ID" '.userStories |= map(if .id == $id then .passes = true else . end)' prd.json > prd.json.tmp
    mv prd.json.tmp prd.json
    git add prd.json
    git commit -m "chore: mark $STORY_ID as passed"
    
    # Log success
    echo "Status: PASSED" >> progress.txt
    echo "Commit: $COMMIT_HASH" >> progress.txt
    
    echo "✅ Story $STORY_ID completed"
    
  else
    echo "❌ Quality checks failed"
    echo "Status: FAILED - quality checks" >> progress.txt
    echo "Will retry in next iteration" >> progress.txt
  fi
  
  echo "Finished: $(date -Iseconds)" >> progress.txt
  
done

echo ""
echo "⚠️ Max iterations ($MAX_ITERATIONS) reached"
echo "Some stories may still be pending. Check prd.json for status."

# Show summary
echo ""
echo "📊 Summary:"
jq -r '.userStories[] | "\(.id): \(.title) - \(if .passes then "✅" else "❌" end)"' prd.json
