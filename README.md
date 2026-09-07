# AILT9019 Sandbox

A small, testable practice project for AILT9019 AI Literacy II.

## What it does

`study_plan.py` turns a subject and an available number of minutes into a short study plan. It rejects empty subjects and non-positive study time so that an edge case is handled explicitly rather than silently producing a broken result.

## Run it

```bash
python3 study_plan.py
```

## Test it

```bash
python3 -m unittest -v
```

The tests cover a normal plan and two failure cases. This repository is intentionally small so every AI-assisted change can be inspected, run, tested, and explained.

## Vibe-coding evidence

- Describe: request one small, observable change.
- Inspect: identify the changed file and relevant lines.
- Run: execute the program locally.
- Test: try both normal and invalid inputs.
- Revise: change the request based on observed results.

## Current limitation

The plan uses fixed time ratios and does not yet account for deadlines, task difficulty, or prior mastery.

## Week 2 build start

Week 2 adds three scoped project candidates and a working prototype for the
robotics/AI direction. See [`week02/README.md`](week02/README.md) for the demo,
tests, acceptance criteria, and project boundaries.
