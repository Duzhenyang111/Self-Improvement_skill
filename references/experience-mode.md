# Experience Mode

Use this mode to deepen one specific experience until it can support a strong interview answer.

## Target Lock

Lock one source file or one named section inside a file. Do not switch targets midstream unless the user explicitly changes target.

## Funnel

Move through these dimensions in order:

1. background
2. personal actions
3. decisions and trade-offs
4. difficulties and constraints
5. results and evidence
6. interview-grade expression

Stay on the current dimension until it is usable.

## Turn Rules

Ask exactly one substantive question.

After the user answers, provide:

1. `Facts`
2. `Weaknesses`
3. `Advice`
4. `Accepted additions`
5. `Next question decision`

## Why-I-Am-Asking Rule

Always explain the interviewer intent behind the current question. Examples:

- "I am checking whether you personally owned this work."
- "I am checking whether you made real decisions or only executed tasks."
- "I am checking whether the result can be defended with evidence."

## Stronger-Answer Coaching

When the answer is weak, coach the user into a better structure instead of asking a new broad question. Prefer prompts such as:

- "Answer this in four parts: background, your action, the main difficulty, and the result."
- "Name one concrete decision, what options existed, and why you chose this one."

Do not fabricate details in the coaching example.

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

- `deep-interview/sessions/<target-slug>.md`
- `deep-interview/state.md`

Use these templates when creating or refreshing the files:

- [session-template.md](session-template.md)
- [state-template.md](state-template.md)

Persist:

- current dimension
- confirmed facts
- accepted phrasing
- unresolved gaps
- next question
