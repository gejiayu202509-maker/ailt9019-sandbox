import unittest

from study_plan import build_study_plan


class StudyPlanTests(unittest.TestCase):
    def test_builds_three_part_plan(self):
        plan = build_study_plan("Vibe Coding", 45)

        self.assertEqual(len(plan), 3)
        self.assertTrue(all("Vibe Coding" in item for item in plan))

    def test_rejects_empty_subject(self):
        with self.assertRaises(ValueError):
            build_study_plan("   ", 45)

    def test_rejects_non_positive_time(self):
        with self.assertRaises(ValueError):
            build_study_plan("Vibe Coding", 0)


if __name__ == "__main__":
    unittest.main()

