# Experience Mode

Use this mode to deepen one specific experience until it can support a strong interview answer.

## Target Lock

Lock one source file or one named section inside a file. Do not switch targets midstream unless explicitly changing target.

## Funnel

Move through these dimensions in order:

1. background
2. personal actions
3. decisions and trade-offs
4. difficulties and constraints
5. results and evidence
6. interview-grade expression

Stay on the current dimension until it is usable.

## Difficulty Levels

### Three Levels

- **basic**: Fact confirmation
  - "What did you do?"
  - "What was your role?"
  - "What technology did you use?"

- **advanced**: Decision analysis
  - "Why did you choose this approach?"
  - "What alternatives were considered?"
  - "What were the trade-offs?"

- **challenge**: Stress testing
  - "What if X situation happened?"
  - "What are the risks of this approach?"
  - "If you could redo this, what would you change?"

### Difficulty Control

- Start at basic level by default
- User can request upgrade/downgrade: `go harder` / `go easier`
- Current difficulty recorded in state.md
- Auto-advance to next level when answer is `ready`

## Turn Rules

Ask exactly one substantive question.

After each answer, provide:

1. `Facts`
2. `Gaps`
3. `Improvement suggestions`
4. `Accepted additions`
5. `Next question decision`

## Self-Check Rule

Every question must have an explicit self-check purpose:

- "This question confirms: did I really lead this work?"
- "This question validates: can I explain the technical decision trade-offs?"
- "This question checks: are there quantifiable results?"

## Self-Improvement Coaching

When the answer is weak, guide toward a better structure instead of asking a new broad question:

- "Try answering in four parts: background, your action, the main difficulty, and the result."
- "Name one concrete decision, what options existed, and why you chose this one."

Do not fabricate details in the coaching example.

## Quick Mode

When using quick mode:

- Ask only 1 question per dimension
- No follow-up deep dives
- Skip directly to next dimension
- 6 dimensions = 6 questions
- Estimated time: 10-15 minutes

## Timed Mode

When using timed mode:

1. Calculate number of questions based on total time (2-3 min per question)
2. Allocate questions by dimension priority
3. Auto-enter finalize when time is reached

## Revisit

User can request to return to a completed dimension:

- `revisit: background`
- `revisit: decisions`

When revisiting:
1. Show previously confirmed content
2. Continue deepening or correcting
3. Update session record

## Skip

User can skip the current dimension:

- `skip this dimension`

Record the skip reason and move to the next dimension.

Skipped dimensions are marked as "skipped" in finalize, reminding the user they may need to be supplemented.

## Stop Condition

Recommend stopping when the experience has:

- clear context
- clear ownership
- at least one real decision
- at least one difficulty
- at least one result or impact
- enough material for a one-minute spoken answer

## State Update

Store progress in:

- `deep-interview/drafts/<target-slug>.md` (editable working copy)
- `deep-interview/sessions/<target-slug>.md` (session record)
- `deep-interview/state.md` (global state)

Use these templates when creating or refreshing the files:

- [session-template.md](session-template.md)
- [state-template.md](state-template.md)

Persist:

- current dimension
- difficulty level
- confirmed facts
- accepted phrasing
- unresolved gaps
- next question
