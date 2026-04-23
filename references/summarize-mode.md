# Summarize Mode

Use this mode to compress a long interaction into reusable state.

## When To Use

- after several turns in one target
- before switching modes
- when the conversation history is becoming noisy
- before pausing for later continuation

## Goal

Reduce future context needs without losing the thread of the interview.

## Required Output

Update `deep-interview/state.md` with:

- current mode
- current target
- completed dimensions
- confirmed facts
- unresolved gaps
- advice already given
- user-accepted additions
- exact next question

Use [state-template.md](state-template.md) as the default shape.

## Compression Rules

- keep only durable facts and decisions
- remove conversational filler
- preserve the interviewer intent of the next question
- keep unresolved items explicit

## Chat Response

Tell the user only the high-value summary:

- what is now solid
- what is still weak
- what will be asked next
