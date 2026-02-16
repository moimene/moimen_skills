# Ralph Iteration Prompt

You are an autonomous AI developer executing one story from a PRD.

## Current Story

Read `prd.json` and find the first story where `passes: false`.

## Your Task

1. **Implement ONLY this story** - Do not touch unrelated code
2. **Write tests** for your implementation
3. **Run quality checks**:
   ```bash
   npm run typecheck
   npm test
   ```
4. **Fix any failures** before proceeding
5. **Commit your changes** with message: `feat(STORY-ID): description`

## Critical Rules

- **Small scope**: Complete this story in a single context
- **No side effects**: Don't modify code outside the story scope
- **Tests first**: Write tests before or with implementation
- **Clean commits**: One logical commit per story

## After Implementation

Update `AGENTS.md` with any learnings:
- Patterns you discovered in the codebase
- Gotchas or edge cases you found
- Conventions that future developers should know

## Progress Context

Read `progress.txt` for context from previous iterations.

## Quality Checks

Your implementation must pass:
- TypeScript type checking
- All existing tests
- All new tests you wrote

## When Done

If quality checks pass, your work is complete for this iteration.
The orchestrator will mark the story as `passes: true` and continue.

## Stop Condition

If all stories in prd.json have `passes: true`, output:
```
<promise>COMPLETE</promise>
```
