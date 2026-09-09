import streamlit as st
from questions import QUESTIONS

# ============================================================
# AI COGNITIVE LEARNING MAP - VERSION 2.0
# ============================================================

st.set_page_config(
    page_title="AI Cognitive Learning Map",
    page_icon="🧠",
    layout="wide"
)

# ============================================================
# TITLE
# ============================================================

st.title("🧠 AI Cognitive Learning Map")

st.write(
    "An intelligent learning assessment that analyzes "
    "your knowledge, confidence, and learning gaps."
)

st.divider()

# ============================================================
# STUDENT INFORMATION
# ============================================================

name = st.text_input("👤 What is your name?")

if name:

    st.success(
        f"Welcome, {name}! Let's understand your DSA knowledge."
    )

    st.header("🧩 Adaptive DSA Assessment")

    st.write(
        f"This V2 assessment contains {len(QUESTIONS)} questions "
        "across multiple DSA concepts and difficulty levels."
    )

    # ========================================================
    # STORE ANSWERS
    # ========================================================

    user_answers = {}
    user_confidence = {}

    # ========================================================
    # QUESTIONS
    # ========================================================

    for question in QUESTIONS:

        question_id = question["id"]

        st.markdown(
            f"### Question {question_id}"
        )

        st.caption(
            f"Concept: {question['concept']}  |  "
            f"Difficulty: {question['difficulty']}"
        )

        answer = st.radio(
            question["question"],
            question["options"],
            key=f"answer_{question_id}"
        )

        confidence = st.slider(
            "How confident are you?",
            1,
            5,
            3,
            key=f"confidence_{question_id}"
        )

        user_answers[question_id] = answer
        user_confidence[question_id] = confidence

        st.divider()

    # ========================================================
    # ANALYSIS ENGINE
    # ========================================================

    def analyze_answer(
        answer,
        correct_answer,
        confidence
    ):

        correct = answer == correct_answer

        if correct and confidence >= 4:

            return (
                "Strong",
                "🟢",
                "Strong understanding and good confidence."
            )

        elif correct and confidence < 4:

            return (
                "Confidence Gap",
                "🟡",
                "You answered correctly, but your confidence "
                "is relatively low."
            )

        elif not correct and confidence < 4:

            return (
                "Learning Gap",
                "🟠",
                "This concept needs additional learning "
                "and practice."
            )

        else:

            return (
                "Possible Misconception",
                "🔴",
                "You were highly confident but answered "
                "incorrectly. This concept should be investigated."
            )

    # ========================================================
    # ANALYZE BUTTON
    # ========================================================

    if st.button(
        "🧠 Analyze My Knowledge",
        use_container_width=True
    ):

        results = []

        # ----------------------------------------------------
        # ANALYZE EVERY QUESTION
        # ----------------------------------------------------

        for question in QUESTIONS:

            question_id = question["id"]

            answer = user_answers[question_id]

            confidence = user_confidence[question_id]

            correct_answer = question["answer"]

            status, icon, explanation = analyze_answer(
                answer,
                correct_answer,
                confidence
            )

            results.append({

                "id": question_id,

                "concept": question["concept"],

                "difficulty": question["difficulty"],

                "status": status,

                "icon": icon,

                "confidence": confidence,

                "correct": answer == correct_answer,

                "explanation": explanation,

                "question": question["question"],

                "correct_answer": correct_answer,

                "given_answer": answer,

                "prerequisite": question["prerequisite"]

            })

        # ====================================================
        # STORE RESULTS
        # ====================================================

        st.session_state["results"] = results

    # ========================================================
    # DISPLAY RESULTS
    # ========================================================

    if "results" in st.session_state:

        results = st.session_state["results"]

        st.divider()

        st.header("📊 Your Cognitive Profile")

        # ====================================================
        # OVERALL SCORES
        # ====================================================

        correct_count = sum(
            result["correct"]
            for result in results
        )

        total_questions = len(results)

        knowledge_score = (
            correct_count / total_questions
        ) * 100

        average_confidence = sum(
            result["confidence"]
            for result in results
        ) / total_questions

        strong_count = sum(
            result["status"] == "Strong"
            for result in results
        )

        misconception_count = sum(
            result["status"] == "Possible Misconception"
            for result in results
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Knowledge Score",
                f"{knowledge_score:.0f}%"
            )

        with col2:

            st.metric(
                "Average Confidence",
                f"{average_confidence:.1f}/5"
            )

        with col3:

            st.metric(
                "Strong Concepts",
                str(strong_count)
            )

        with col4:

            st.metric(
                "Investigate",
                str(misconception_count)
            )

        st.divider()

        # ====================================================
        # DIFFICULTY ANALYSIS
        # ====================================================

        st.subheader("📈 Performance by Difficulty")

        difficulties = [
            "Easy",
            "Medium",
            "Hard"
        ]

        for difficulty in difficulties:

            difficulty_results = [

                result
                for result in results

                if result["difficulty"] == difficulty
            ]

            if difficulty_results:

                difficulty_correct = sum(
                    result["correct"]
                    for result in difficulty_results
                )

                difficulty_score = (
                    difficulty_correct
                    / len(difficulty_results)
                ) * 100

                st.write(
                    f"**{difficulty}:** "
                    f"{difficulty_score:.0f}% "
                    f"({difficulty_correct}/"
                    f"{len(difficulty_results)})"
                )

                st.progress(
                    difficulty_score / 100
                )

        st.divider()

        # ====================================================
        # CONCEPT ANALYSIS
        # ====================================================

        st.subheader("🔍 Concept-by-Concept Analysis")

        concepts = []

        for result in results:

            if result["concept"] not in concepts:

                concepts.append(
                    result["concept"]
                )

        concept_scores = {}

        for concept in concepts:

            concept_results = [

                result
                for result in results

                if result["concept"] == concept
            ]

            concept_correct = sum(
                result["correct"]
                for result in concept_results
            )

            concept_score = (
                concept_correct
                / len(concept_results)
            ) * 100

            concept_scores[concept] = concept_score

            st.markdown(
                f"### {concept}"
            )

            st.write(
                f"**Knowledge:** "
                f"{concept_score:.0f}%"
            )

            st.progress(
                concept_score / 100
            )

            for result in concept_results:

                st.write(
                    f"{result['icon']} "
                    f"Question {result['id']} — "
                    f"{result['status']} — "
                    f"Confidence {result['confidence']}/5"
                )

        st.divider()

        # ====================================================
        # FIND PRIORITY CONCEPT
        # ====================================================

        st.subheader("🎯 Your Highest-Priority Learning Area")

        priority_order = [
            "Possible Misconception",
            "Learning Gap",
            "Confidence Gap"
        ]

        priority_result = None

        for priority in priority_order:

            for result in results:

                if result["status"] == priority:

                    priority_result = result

                    break

            if priority_result:

                break

        if priority_result:

            concept = priority_result["concept"]

            status = priority_result["status"]

            if status == "Possible Misconception":

                st.error(
                    f"🚨 **Investigate {concept} first.**\n\n"
                    "You answered incorrectly with high confidence. "
                    "This may indicate a misconception or misunderstanding "
                    "that should be investigated."
                )

            elif status == "Learning Gap":

                st.warning(
                    f"📚 **Focus on {concept} next.**\n\n"
                    "Your answers suggest that this concept needs "
                    "additional learning and practice."
                )

            else:

                st.info(
                    f"💡 **Reinforce {concept}.**\n\n"
                    "You answered correctly but your confidence "
                    "is relatively low."
                )

        else:

            st.success(
                "🎉 No major learning signals were detected."
            )

        st.divider()

        # ====================================================
        # PREREQUISITE ANALYSIS
        # ====================================================

        st.subheader("🔗 Prerequisite Analysis")

        prerequisite_warnings = []

        for result in results:

            prerequisite = result["prerequisite"]

            if prerequisite is None:
                continue

            if not result["correct"]:

                prerequisite_warnings.append(
                    (
                        result["concept"],
                        prerequisite
                    )
                )

        if prerequisite_warnings:

            for concept, prerequisite in prerequisite_warnings:

                prerequisite_score = concept_scores.get(
                    prerequisite,
                    None
                )

                if prerequisite_score is not None:

                    if prerequisite_score < 60:

                        st.warning(
                            f"⚠️ **{concept}** may be affected by "
                            f"weak performance in its prerequisite "
                            f"**{prerequisite}** "
                            f"({prerequisite_score:.0f}%)."
                        )

                    else:

                        st.info(
                            f"ℹ️ You struggled with **{concept}**, "
                            f"but its prerequisite **{prerequisite}** "
                            f"is relatively strong "
                            f"({prerequisite_score:.0f}%)."
                        )

        else:

            st.success(
                "No prerequisite warnings were detected."
            )

        st.divider()

        # ====================================================
        # STUDY PLAN
        # ====================================================

        st.subheader("📚 Personalized Study Plan")

        attention_concepts = []

        for concept in concepts:

            score = concept_scores[concept]

            if score < 60:

                attention_concepts.append(
                    (concept, score)
                )

        attention_concepts.sort(
            key=lambda item: item[1]
        )

        if attention_concepts:

            for concept, score in attention_concepts:

                st.markdown(
                    f"**{concept} — {score:.0f}%**"
                )

                st.write(
                    "1. Review the fundamentals\n"
                    "2. Study a worked example\n"
                    "3. Solve 3–5 practice problems\n"
                    "4. Retake questions on this concept"
                )

        else:

            st.success(
                "Your assessed concepts are above the current "
                "learning-gap threshold. You can move toward "
                "more advanced problems."
            )

        st.divider()

        # ====================================================
        # COGNITIVE LEARNING MAP
        # ====================================================

        st.subheader("🗺️ Your Cognitive Learning Map")

        st.write(
            "The map connects concepts using prerequisite "
            "relationships defined in the V2 question bank."
        )

        def map_label(concept):

            score = concept_scores.get(
                concept,
                None
            )

            if score is None:

                return (
                    f"{concept}\\n"
                    "⚪ Not Assessed"
                )

            if score >= 80:

                return (
                    f"{concept}\\n"
                    "🟢 Strong"
                )

            elif score >= 60:

                return (
                    f"{concept}\\n"
                    "🟡 Developing"
                )

            else:

                return (
                    f"{concept}\\n"
                    "🟠 Needs Work"
                )

        graph = f"""

        digraph LearningMap {{

            rankdir=LR

            node [
                shape=box
                style="rounded"
                fontsize=11
            ]

            Arrays [
                label="{map_label('Arrays')}"
            ]

            LinkedLists [
                label="{map_label('Linked Lists')}"
            ]

            StackQueue [
                label="{map_label('Stack & Queue')}"
            ]

            Recursion [
                label="{map_label('Recursion')}"
            ]

            Trees [
                label="{map_label('Trees')}"
            ]

            Graphs [
                label="{map_label('Graphs')}"
            ]

            Arrays -> LinkedLists

            LinkedLists -> Recursion

            StackQueue -> Recursion

            Recursion -> Trees

            Trees -> Graphs

            Recursion -> Graphs

        }}

        """

        st.graphviz_chart(graph)

        st.divider()

        # ====================================================
        # INTERPRETATION
        # ====================================================

        st.subheader("🧠 What Your Results Suggest")

        if knowledge_score >= 80:

            st.success(
                "You demonstrated strong overall performance. "
                "You can begin challenging yourself with more "
                "advanced DSA problems."
            )

        elif knowledge_score >= 60:

            st.info(
                "You have a reasonable foundation, but some "
                "concepts need reinforcement before progressing "
                "to more advanced topics."
            )

        else:

            st.warning(
                "Several fundamental concepts may need strengthening. "
                "Follow the personalized study plan before progressing."
            )

        st.divider()

        # ====================================================
        # FOOTER
        # ====================================================

        st.caption(
            "AI Cognitive Learning Map — Version 2.0 | "
            "Adaptive rule-based learning assessment prototype"
        )