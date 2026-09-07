# Week 2: project directions and first prototype

This folder completes the Week 2 build-start checkpoint:

- [`candidates.md`](candidates.md) contains three directions for team discussion:
  Quant, Web3, and Robotics/AI.
- `robot_safety_validator.py` is a small local prototype for the Robotics/AI
  direction.
- `sample_plan.json` is a safe simulated scenario.
- `test_robot_safety_validator.py` contains acceptance and refusal cases.

## Run the prototype

From this folder:

```bash
python3 robot_safety_validator.py sample_plan.json
```

Expected result:

```json
{
  "verdict": "PASS",
  "findings": []
}
```

## Run the evaluation

```bash
python3 -m unittest -v test_robot_safety_validator.py
```

The tests cover a valid baseline plus forbidden-zone, overload, unknown-object,
unsupported-action, and malformed-input failures. A failed plan reports the
specific step and rule, making the result inspectable rather than relying on a
model's unsupported judgement.

## Scope and ethics boundary

This prototype evaluates simulated JSON only. It does not connect to or control
a physical robot, and a PASS result is not a real-world safety certification.
Physical deployment would require sensor integration, hardware interlocks,
operator review, and domain-specific safety testing outside this project.

## AI-use note

Codex helped draft the shortlist, implement the prototype, and write tests.
The student remains responsible for selecting the final team direction,
verifying the code, explaining its behaviour, and disclosing AI assistance in
the final course deliverables.
