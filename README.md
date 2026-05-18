# LLM Engineering Evaluation Lab

## Overview
The LLM Engineering Evaluation Lab is a structured collection of realistic software engineering tasks designed to evaluate coding models on practical debugging, reasoning, and test-driven problem solving.

Each task simulates a real-world engineering scenario where:
- A working system contains a subtle bug
- Existing tests may be incomplete or insufficient
- A failing test suite is used to validate correctness
- A golden solution demonstrates the correct fix

The goal is to design tasks that distinguish between superficial pattern matching and true engineering understanding.

---

## Project Goals
This repository is designed to practice and explore:
- Realistic software debugging scenarios
- Test design and failure case engineering
- Idempotency, state, and consistency bugs
- Edge case reasoning
- Evaluation design for coding agents and LLMs
- Writing minimal but correct fixes (golden solutions)

---

## Repository Structure
```
llm-engineering-eval-lab/
│
├── tasks/
│   ├── task_001_event_deduplication/
│   │   ├── README.md
│   │   ├── buggy/
│   │   ├── tests/
│   │   ├── golden_solution/
│   │   └── evaluator_notes.md
│   │
│   ├── task_002_timezone_bug/
│   ├── task_003_async_cache_race/
│   └── ...
│
├── docs/
│   ├── evaluation_principles.md
│   └── common_llm_failure_patterns.md
│
├── scripts/
│   └── run_tests.py
│
├── requirements.txt
└── README.md
```

---

## How to Run Tests

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Run tests
From the project root:
```
pytest
```

---

## Task Format
Each task includes:

### 1. Buggy Implementation
Located in:
buggy/

Contains intentionally flawed but realistic code.

---

### 2. Test Suite
Located in:
tests/

Includes:
- baseline tests
- fail-to-pass tests
- edge case validations

---

### 3. Golden Solution
Located in:
golden_solution/

A minimal correct implementation that fixes the bug while preserving constraints.

---

### 4. Task Description
Each task contains a README explaining:
- expected behavior
- actual behavior
- constraints
- context of the bug

---

### 5. Evaluator Notes
Explains:
- why the task is difficult
- what skills are being tested
- common incorrect model behaviors

---

## Design Philosophy
This repository is built around the idea that:
> Real engineering skill is not just writing code, but reasoning correctly about system behavior under constraints.
Tasks emphasize:
- state consistency
- correctness over cleverness
- edge-case handling
- realistic production-style bugs

---

## Common LLM Failure Modes Targeted
Many tasks are designed to expose:
- shallow patching instead of root-cause fixes
- incorrect assumptions about state
- failure to handle idempotency
- ignoring edge cases
- overfitting to test cases
- incorrect abstraction placement

---

## Contributing / Extending
New tasks should follow this structure:
- realistic bug report
- minimal reproducible codebase
- incomplete or failing tests
- clearly defined constraints
- golden solution that is simple and correct
- evaluator notes explaining intent

---

## Why This Project Exists
This project is both:
- a personal engineering practice lab
- a structured environment for designing evaluation tasks for coding models

It bridges:
- software engineering
- testing strategy
- AI evaluation design

---

## Author
Ashley A. Dehart

## License
For educational and research use.