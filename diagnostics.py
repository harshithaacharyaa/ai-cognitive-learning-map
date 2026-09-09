# ============================================================
# AI COGNITIVE LEARNING MAP - STRUCTURED DIAGNOSTICS
# VERSION 3.3
# ============================================================

DIAGNOSTIC_QUESTIONS = {

    "Learning Gap": {
        "question": "What best describes what happened?",
        "options": [
            {
                "text": "I don't fully understand the concept.",
                "code": "CONCEPTUAL_GAP"
            },
            {
                "text": "I understand the concept but need more practice.",
                "code": "APPLICATION_DIFFICULTY"
            },
            {
                "text": "I confused it with another concept.",
                "code": "CONCEPT_CONFUSION"
            },
            {
                "text": "I guessed the answer.",
                "code": "UNCERTAIN_KNOWLEDGE"
            }
        ]
    },

    "Possible Misconception": {
        "question": "Why did you think your answer was correct?",
        "options": [
            {
                "text": "I misunderstood the concept.",
                "code": "CONCEPTUAL_GAP"
            },
            {
                "text": "I confused it with another concept.",
                "code": "CONCEPT_CONFUSION"
            },
            {
                "text": "I remembered a similar rule incorrectly.",
                "code": "CONCEPTUAL_GAP"
            },
            {
                "text": "I was confident but guessed.",
                "code": "UNCERTAIN_KNOWLEDGE"
            }
        ]
    },

    "Confidence Gap": {
        "question": "Why were you unsure even though your answer was correct?",
        "options": [
            {
                "text": "I remembered the answer but wasn't sure.",
                "code": "UNCERTAIN_KNOWLEDGE"
            },
            {
                "text": "I understand the concept but need more practice.",
                "code": "APPLICATION_DIFFICULTY"
            },
            {
                "text": "I confused it with another concept.",
                "code": "CONCEPT_CONFUSION"
            },
            {
                "text": "I guessed correctly.",
                "code": "UNCERTAIN_KNOWLEDGE"
            }
        ]
    }
}
