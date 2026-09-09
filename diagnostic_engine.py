# ============================================================
# AI COGNITIVE LEARNING MAP - DIAGNOSTIC REASONING ENGINE
# VERSION 3.2
# ============================================================


def classify_diagnostic_reason(reason):
    """
    Converts the student's diagnostic response into
    a structured cognitive state.
    """

    reason_lower = reason.lower()

    if (
        "don't fully understand" in reason_lower
        or "misunderstood" in reason_lower
    ):
        return {
            "state": "Conceptual Gap",
            "code": "CONCEPTUAL_GAP",
            "recommendation": (
                "Review the fundamentals of this concept "
                "before attempting more difficult questions."
            )
        }

    elif (
        "need more practice" in reason_lower
        or "can't apply" in reason_lower
    ):
        return {
            "state": "Application Difficulty",
            "code": "APPLICATION_DIFFICULTY",
            "recommendation": (
                "Practice worked examples and application-based "
                "problems for this concept."
            )
        }

    elif "confused" in reason_lower:
        return {
            "state": "Concept Confusion",
            "code": "CONCEPT_CONFUSION",
            "recommendation": (
                "Review the differences between the related concepts "
                "and solve comparison-based questions."
            )
        }

    elif (
        "guessed" in reason_lower
        or "wasn't sure" in reason_lower
    ):
        return {
            "state": "Uncertain Knowledge",
            "code": "UNCERTAIN_KNOWLEDGE",
            "recommendation": (
                "Reinforce the concept with simpler questions "
                "before progressing."
            )
        }

    else:
        return {
            "state": "Unclassified",
            "code": "UNCLASSIFIED",
            "recommendation": (
                "Gather more evidence about this learning pattern."
            )
        }