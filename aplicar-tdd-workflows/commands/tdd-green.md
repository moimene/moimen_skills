Implement minimal code to make failing tests pass - TDD Green Phase.

[Extended thinking: Implements only the code necessary to make tests pass, following YAGNI principles and avoiding over-engineering.]

## Role

Implement minimal code using Task tool with subagent_type="backend-development::backend-architect".

## Prompt Template

"Implement MINIMAL code to make tests pass for: $ARGUMENTS

## Core Principles

1. **YAGNI (You Aren't Gonna Need It)**
   - Only implement what's needed to pass tests
   - No speculative features
   - No premature optimization
   - No extra abstractions

2. **Simplest Thing That Could Work**
   - Hardcoded values are acceptable initially
   - Simple conditionals over complex patterns
   - Direct implementations over generalized solutions
   - Flat code over nested abstractions

3. **Make It Work First**
   - Don't worry about code beauty yet
   - Ignore duplication temporarily
   - Focus solely on test satisfaction
   - Refactoring comes in next phase

## Implementation Process

### Step 1: Analyze Failing Tests
- Understand what each test expects
- Identify the minimal interface required
- Note expected inputs and outputs
- Document error conditions

### Step 2: Implement Just Enough
```typescript
// If test expects: add(2, 3) === 5
// Start with:
function add(a: number, b: number): number {
  return a + b;  // Simplest implementation
}
// NOT:
function add(...numbers: number[]): number {
  return numbers.reduce((sum, n) => sum + n, 0);  // Over-engineered
}
```

### Step 3: Run Tests After Each Change
- Verify new test passes
- Ensure no regressions
- Document any unexpected failures

### Step 4: Stop When Green
- Resist urge to improve
- Note improvements for refactor phase
- Commit working state

## Framework-Specific Patterns

**TypeScript/JavaScript**
```typescript
// Minimal class implementation
class UserService {
  constructor(private repo: UserRepository) {}
  
  async getUser(id: string): Promise<User | null> {
    return this.repo.findById(id);  // Direct delegation
  }
}
```

**Python**
```python
# Minimal function implementation
def validate_email(email: str) -> bool:
    return '@' in email and '.' in email  # Simple check
```

**Go**
```go
// Minimal struct method
func (s *Service) GetItem(id string) (*Item, error) {
    return s.repo.Find(id)  // Direct call
}
```

## Anti-Patterns to Avoid

❌ **Over-Engineering**
```typescript
// DON'T: Complex factory for simple object
class UserFactory {
  private builders: Map<string, UserBuilder>;
  // ... 50 lines of abstraction
}

// DO: Direct construction
function createUser(data: UserData): User {
  return new User(data.id, data.name, data.email);
}
```

❌ **Premature Abstraction**
```typescript
// DON'T: Interface for single implementation
interface IUserValidatorStrategy { /* ... */ }
class EmailValidator implements IUserValidatorStrategy { /* ... */ }

// DO: Simple function
function isValidEmail(email: string): boolean {
  return email.includes('@');
}
```

❌ **Feature Creep**
```typescript
// Test only requires: get user by ID
// DON'T: Add pagination, filtering, sorting
// DO: Implement only getById
```

## Output Requirements

1. **Working Implementation**
   - All specified tests pass
   - No test modifications
   - Minimal code footprint

2. **Test Verification**
   - Run command provided
   - All tests green
   - Coverage report included

3. **Refactoring Notes**
   - List of code smells identified
   - Suggested improvements for next phase
   - Technical debt acknowledgment

## Validation Checklist

Before completing:

- [ ] All previously failing tests now pass
- [ ] No tests were modified to pass
- [ ] No unrelated tests broken
- [ ] Implementation is minimal
- [ ] No features beyond test requirements
- [ ] Code compiles/runs without errors

## Example Transformation

**Failing Test:**
```typescript
it('should calculate discount for premium user', () => {
  const user = { type: 'premium', purchases: 1000 };
  expect(calculateDiscount(user)).toBe(0.15);
});
```

**Minimal Implementation:**
```typescript
function calculateDiscount(user: { type: string; purchases: number }): number {
  if (user.type === 'premium') {
    return 0.15;
  }
  return 0;
}
```

**NOT:**
```typescript
// Over-engineered
class DiscountCalculator {
  private strategies: Map<string, DiscountStrategy>;
  private loyaltyMultiplier: number;
  // ... etc
}
```

Make tests pass for: $ARGUMENTS"

## Success Criteria

- 100% of targeted tests passing
- Zero test modifications
- Minimal code changes
- Ready for refactor phase
