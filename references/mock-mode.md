# Mock Interview Mode

Simulate a real interview scenario with continuous questions, timed responses, and overall evaluation.

## Trigger Commands

- `start mock`
- `start mock: backend engineer`
- `start mock: 30min`
- `start mock: quick 15min`

## Flow

### 1. Preparation

1. Collect prepared experience/theme/role materials from `drafts/`
2. Identify askable targets (at least completed basic level)
3. Determine interview duration (default 30 minutes)
4. Generate question sequence (5-8 questions)

### 2. Question Sequence Design

Allocate questions by ratio:

- 40% experience deep-dive (from prepared materials)
- 30% theme capability validation (cross-experience proof)
- 20% role perspective questions (target position related)
- 10% stress testing (challenge level questions)

### 3. Interview Flow

For each question:

1. Display the question
2. Record the answer
3. Brief feedback (max 3 sentences)
4. Move immediately to next question (no deep-dive)

### 4. Time Control

- Suggested time per question: 2-3 minutes
- After 4 minutes: suggest wrapping up
- When total time reached: enter summary

### 5. Summary Report

Output:

- Overall score (1-10)
- Strongest answer and why
- Weakest answer and how to improve
- Materials that need supplementing
- Suggested practice directions

Save summary to `deep-interview/sessions/mock-<timestamp>.md`

## Question Selection Strategy

### Experience Questions

Select from completed experiences, prefer:

- Experiences with clear ownership
- Experiences with quantifiable results
- Experiences with interesting trade-offs

### Theme Questions

Select from identified themes, prefer:

- Themes with multiple supporting examples
- Themes relevant to target role

### Role Questions

Select based on target role evaluation lenses:

- Technical depth
- Ownership
- Prioritization
- Impact measurement

### Stress Questions

Challenge-level questions:

- "What if the timeline was cut in half?"
- "What would you do differently?"
- "What was the biggest risk you took?"

## Template

Use [mock-template.md](mock-template.md) for the session record.
