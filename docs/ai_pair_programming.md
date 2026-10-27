# CO6 — AI Pair Programming Post-Mortem

This document is a template for the student's final reflection. Update it with the
actual tools/prompts used during development.

## 1. Where AI accelerated development

Examples:
- generated initial test cases
- suggested FastAPI project structure
- reviewed complexity explanations
- produced documentation drafts
- helped identify edge cases

## 2. Where AI failed

Examples:
- an initial scheduling implementation did not consider teacher conflicts
- a generated route algorithm incorrectly assumed an unweighted graph
- some generated type hints required correction

## 3. Reviewer-of-record discipline

Every AI-generated code change was treated as a suggestion, not as an authoritative answer.

The development workflow was:

```text
Specification
    ↓
AI-assisted draft
    ↓
Human review
    ↓
Unit/property tests
    ↓
Static type checking
    ↓
Linting
    ↓
Integration testing
    ↓
Human approval
```

## 4. Example prompts

- "Implement Dijkstra using a binary heap and explain its complexity."
- "Review this scheduler for teacher and room conflicts."
- "Generate pytest tests for this graph API."
- "Refactor this class according to SOLID principles."

## 5. Disclosure

The final report should state exactly which AI tools were used, for what purpose,
and which parts were manually reviewed and modified.
