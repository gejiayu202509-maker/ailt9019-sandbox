"""A tiny, testable study-plan generator for AILT9019 practice."""


def build_study_plan(subject: str, minutes: int) -> list[str]:
    """Return a three-part study plan for a subject and time budget."""
    subject = subject.strip()
    if not subject:
        raise ValueError("Subject cannot be empty.")
    if minutes <= 0:
        raise ValueError("Minutes must be positive.")

    preview = max(1, round(minutes * 0.2))
    practice = max(1, round(minutes * 0.6))
    review = minutes - preview - practice
    if review < 1:
        review = 1
        practice = max(1, minutes - preview - review)

    return [
        f"Preview {subject}: {preview} min",
        f"Practise {subject}: {practice} min",
        f"Recall and review {subject}: {review} min",
    ]


if __name__ == "__main__":
    for item in build_study_plan("Intro to Vibe Coding", 45):
        print(f"- {item}")

