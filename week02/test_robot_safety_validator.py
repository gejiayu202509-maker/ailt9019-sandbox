import unittest

from robot_safety_validator import validate_scenario


def scenario(plan):
    return {
        "max_payload_kg": 2.0,
        "forbidden_zones": ["human_only_area"],
        "objects": {
            "blue_block": {"weight_kg": 0.4},
            "toolbox": {"weight_kg": 3.5},
        },
        "plan": plan,
    }


class RobotSafetyValidatorTests(unittest.TestCase):
    def test_accepts_safe_plan(self):
        result = validate_scenario(
            scenario(
                [
                    {"action": "move_to", "zone": "workbench"},
                    {"action": "pick", "object": "blue_block"},
                    {"action": "place"},
                ]
            )
        )
        self.assertEqual(result, {"verdict": "PASS", "findings": []})

    def test_rejects_forbidden_zone_with_step_evidence(self):
        result = validate_scenario(
            scenario([{"action": "move_to", "zone": "human_only_area"}])
        )
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual(result["findings"][0]["step"], 1)
        self.assertIn("Forbidden zone", result["findings"][0]["reason"])

    def test_rejects_overweight_object(self):
        result = validate_scenario(scenario([{"action": "pick", "object": "toolbox"}]))
        self.assertEqual(result["verdict"], "FAIL")
        self.assertIn("exceeds limit", result["findings"][0]["reason"])

    def test_rejects_unknown_object(self):
        result = validate_scenario(scenario([{"action": "pick", "object": "cup"}]))
        self.assertEqual(result["verdict"], "FAIL")
        self.assertIn("Unknown object", result["findings"][0]["reason"])

    def test_rejects_unsupported_action(self):
        result = validate_scenario(scenario([{"action": "drill", "object": "wall"}]))
        self.assertEqual(result["verdict"], "FAIL")
        self.assertIn("Unsupported action", result["findings"][0]["reason"])

    def test_rejects_missing_required_fields(self):
        result = validate_scenario({"plan": []})
        self.assertEqual(result["verdict"], "FAIL")
        self.assertGreaterEqual(len(result["findings"]), 1)

    def test_rejects_invalid_scenario_types(self):
        invalid = scenario([])
        invalid["max_payload_kg"] = "heavy"
        result = validate_scenario(invalid)
        self.assertEqual(result["verdict"], "FAIL")
        self.assertIn("Invalid scenario", result["findings"][0]["reason"])


if __name__ == "__main__":
    unittest.main()
