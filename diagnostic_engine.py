# ============================================================
# AI COGNITIVE LEARNING MAP - DIAGNOSTIC REASONING ENGINE
# VERSION 3.3
# ============================================================

COGNITIVE_STATES = {

    "CONCEPTUAL_GAP": {
        "state": "Conceptual Gap",
        "recommendation": (
            "Review the fundamentals of this concept "
            "before attempting more difficult questions."
        )
    },

    "APPLICATION_DIFFICULTY": {
        "state": "Application Difficulty",
        "recommendation": (
            "Practice worked examples and application-based "
            "problems for this concept."
        )
    },

    "CONCEPT_CONFUSION": {
        "state": "Concept Confusion",
        "recommendation": (
            "Review the differences between the related concepts "
            "and solve comparison-based questions."
        )
    },

    "UNCERTAIN_KNOWLEDGE": {
        "state": "Uncertain Knowledge",
        "recommendation": (
            "Reinforce the concept with simpler questions "
            "before progressing."
        )
    }
}


def classify_diagnostic_reason(reason_code):
    """
    Converts a diagnostic reason code into
    a structured cognitive state.
    """

    result = COGNITIVE_STATES.get(reason_code)

    if result is None:
        return {
            "state": "Unclassified",
            "code": "UNCLASSIFIED",
            "recommendation": (
                "Gather more evidence about this learning pattern."
            )
        }

    return {
        "state": result["state"],
        "code": reason_code,
        "recommendation": result["recommendation"]
    }
