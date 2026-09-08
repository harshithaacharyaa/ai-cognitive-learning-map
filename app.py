import streamlit as st

# ============================================================
# AI COGNITIVE LEARNING MAP - VERSION 1.0
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

    st.header("🧩 DSA Knowledge Assessment")

    st.write(
        "Answer each question and rate how confident you are "
        "in your answer."
    )

    # ========================================================
    # QUESTION 1 - ARRAYS
    # ========================================================

    q1 = st.radio(
        "1. Which data structure stores elements in contiguous memory?",
        [
            "Linked List",
            "Array",
            "Tree",
            "Graph"
        ],
        key="q1"
    )

    c1 = st.slider(
        "Confidence for Question 1",
        1, 5, 3,
        key="c1"
    )

    st.divider()

    # ========================================================
    # QUESTION 2 - LINKED LISTS
    # ========================================================

    q2 = st.radio(
        "2. Which pointer usually points to the next node in a linked list?",
        [
            "Head",
            "Next",
            "Root",
            "Parent"
        ],
        key="q2"
    )

    c2 = st.slider(
        "Confidence for Question 2",
        1, 5, 3,
        key="c2"
    )

    st.divider()

    # ========================================================
    # QUESTION 3 - STACK
    # ========================================================

    q3 = st.radio(
        "3. Which data structure follows the LIFO principle?",
        [
            "Queue",
            "Stack",
            "Array",
            "Linked List"
        ],
        key="q3"
    )

    c3 = st.slider(
        "Confidence for Question 3",
        1, 5, 3,
        key="c3"
    )

    st.divider()

    # ========================================================
    # QUESTION 4 - RECURSION
    # ========================================================

    q4 = st.radio(
        "4. What must a recursive function eventually have?",
        [
            "A loop",
            "A base case",
            "A database",
            "A queue"
        ],
        key="q4"
    )

    c4 = st.slider(
        "Confidence for Question 4",
        1, 5, 3,
        key="c4"
    )

    st.divider()

    # ========================================================
    # QUESTION 5 - TREES
    # ========================================================

    q5 = st.radio(
        "5. What is the topmost node of a tree called?",
        [
            "Leaf",
            "Child",
            "Root",
            "Edge"
        ],
        key="q5"
    )

    c5 = st.slider(
        "Confidence for Question 5",
        1, 5, 3,
        key="c5"
    )

    st.divider()

    # ========================================================
    # ANALYSIS ENGINE
    # ========================================================

    def analyze_answer(answer, correct_answer, confidence):

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
                "You answered correctly, but your confidence is relatively low."
            )

        elif not correct and confidence < 4:

            return (
                "Learning Gap",
                "🟠",
                "This concept needs additional learning and practice."
            )

        else:

            return (
                "Possible Misconception",
                "🔴",
                "You were highly confident but answered incorrectly. "
                "This concept should be investigated."
            )

    # ========================================================
    # ANALYZE BUTTON
    # ========================================================

    if st.button(
        "🧠 Analyze My Knowledge",
        use_container_width=True
    ):

        # ----------------------------------------------------
        # QUESTION DATA
        # ----------------------------------------------------

        answers = {

            "Arrays": (
                q1,
                "Array",
                c1
            ),

            "Linked Lists": (
                q2,
                "Next",
                c2
            ),

            "Stack & Queue": (
                q3,
                "Stack",
                c3
            ),

            "Recursion": (
                q4,
                "A base case",
                c4
            ),

            "Trees": (
                q5,
                "Root",
                c5
            )
        }

        # ----------------------------------------------------
        # STORE RESULTS
        # ----------------------------------------------------

        results = []

        for concept, data in answers.items():

            answer = data[0]
            correct_answer = data[1]
            confidence = data[2]

            status, icon, explanation = analyze_answer(
                answer,
                correct_answer,
                confidence
            )

            results.append({

                "concept": concept,
                "status": status,
                "icon": icon,
                "confidence": confidence,
                "correct": answer == correct_answer,
                "explanation": explanation
            })

        # ====================================================
        # RESULTS HEADER
        # ====================================================

        st.divider()

        st.header("📊 Your Cognitive Profile")

        # ====================================================
        # CALCULATE SCORES
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

        # ====================================================
        # TOP METRICS
        # ====================================================

        col1, col2, col3 = st.columns(3)

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

            strong_count = sum(
                result["status"] == "Strong"
                for result in results
            )

            st.metric(
                "Strong Concepts",
                f"{strong_count}/{total_questions}"
            )

        st.divider()

        # ====================================================
        # CONCEPT ANALYSIS
        # ====================================================

        st.subheader("🔍 Concept-by-Concept Analysis")

        for result in results:

            st.markdown(
                f"### {result['icon']} {result['concept']}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Status:** {result['status']}"
                )

                st.write(
                    f"**Confidence:** "
                    f"{result['confidence']}/5"
                )

            with col2:

                st.write(
                    result["explanation"]
                )

            st.progress(
                result["confidence"] / 5
            )

        st.divider()

        # ====================================================
        # PERSONALIZED RECOMMENDATION
        # ====================================================

        st.subheader("🎯 Your Recommended Next Step")

        priority_order = [
            "Possible Misconception",
            "Learning Gap",
            "Confidence Gap"
        ]

        recommendation = None

        for priority in priority_order:

            for result in results:

                if result["status"] == priority:

                    recommendation = result

                    break

            if recommendation:

                break

        if recommendation:

            concept = recommendation["concept"]
            status = recommendation["status"]

            if status == "Possible Misconception":

                st.error(
                    f"🚨 **Focus on {concept} first.**\n\n"
                    "You answered incorrectly with high confidence. "
                    "Review the fundamentals and test your understanding "
                    "again before moving forward."
                )

            elif status == "Learning Gap":

                st.warning(
                    f"📚 **Focus on {concept} next.**\n\n"
                    "Your performance suggests that this concept "
                    "needs more learning and practice."
                )

            elif status == "Confidence Gap":

                st.info(
                    f"💡 **Reinforce {concept}.**\n\n"
                    "You answered correctly, but your confidence "
                    "is relatively low. Practice a few more problems "
                    "to strengthen your understanding."
                )

        else:

            st.success(
                "🎉 Your assessed concepts look strong. "
                "You're ready to move forward."
            )

        st.divider()

        # ====================================================
        # PERSONALIZED STUDY PLAN
        # ====================================================

        st.subheader("📚 Suggested Study Plan")

        needs_attention = [

            result
            for result in results

            if result["status"] != "Strong"
        ]

        if needs_attention:

            for result in needs_attention:

                concept = result["concept"]
                status = result["status"]

                st.markdown(
                    f"**{concept}** → ",
                    unsafe_allow_html=False
                )

                if status == "Possible Misconception":

                    st.write(
                        "1. Review the fundamentals\n"
                        "2. Explain the concept in your own words\n"
                        "3. Solve 3 beginner problems\n"
                        "4. Retake the assessment"
                    )

                elif status == "Learning Gap":

                    st.write(
                        "1. Study the concept fundamentals\n"
                        "2. Follow one worked example\n"
                        "3. Solve 3 beginner problems\n"
                        "4. Retake the assessment"
                    )

                else:

                    st.write(
                        "1. Review the concept\n"
                        "2. Solve 2–3 practice problems\n"
                        "3. Retest your confidence"
                    )

        else:

            st.success(
                "No major learning gaps detected. "
                "You can move to the next level."
            )

        st.divider()

        # ====================================================
        # DYNAMIC COGNITIVE MAP
        # ====================================================

        st.subheader("🗺️ Your Cognitive Learning Map")

        st.write(
            "This map connects concepts in a basic learning sequence. "
            "The labels below reflect your current assessment."
        )

        # ----------------------------------------------------
        # STATUS LOOKUP
        # ----------------------------------------------------

        status_map = {

            result["concept"]:
            result["status"]

            for result in results
        }

        # ----------------------------------------------------
        # NODE LABELS
        # ----------------------------------------------------

        def node_label(concept):

            status = status_map.get(
                concept,
                "Not Assessed"
            )

            if status == "Strong":

                return f"{concept}\\n🟢 Strong"

            elif status == "Confidence Gap":

                return f"{concept}\\n🟡 Reinforce"

            elif status == "Learning Gap":

                return f"{concept}\\n🟠 Learning Gap"

            elif status == "Possible Misconception":

                return f"{concept}\\n🔴 Investigate"

            else:

                return f"{concept}\\n⚪ Not Assessed"

        # ----------------------------------------------------
        # GRAPH
        # ----------------------------------------------------

        graph = f"""

        digraph {{

            rankdir=LR

            node [
                shape=box
                style="rounded"
                fontsize=12
            ]

            Arrays [
                label="{node_label('Arrays')}"
            ]

            LinkedLists [
                label="{node_label('Linked Lists')}"
            ]

            StackQueue [
                label="{node_label('Stack & Queue')}"
            ]

            Recursion [
                label="{node_label('Recursion')}"
            ]

            Trees [
                label="{node_label('Trees')}"
            ]

            Graphs [
                label="Graphs\\n⚪ Not Assessed"
            ]

            Arrays -> LinkedLists
            LinkedLists -> Recursion
            StackQueue -> Recursion
            Recursion -> Trees
            Trees -> Graphs
        }}

        """

        st.graphviz_chart(graph)

        st.divider()

        # ====================================================
        # LEARNING INTERPRETATION
        # ====================================================

        st.subheader("🧠 What Your Results Suggest")

        if knowledge_score >= 80:

            st.success(
                "You demonstrated strong performance across most "
                "assessed concepts. You can begin working on "
                "more advanced DSA problems."
            )

        elif knowledge_score >= 60:

            st.info(
                "You have a reasonable foundation, but some concepts "
                "need reinforcement before moving to advanced topics."
            )

        else:

            st.warning(
                "Your current assessment suggests that several "
                "fundamental concepts need strengthening. "
                "Focus on the recommended concepts before progressing."
            )

        # ====================================================
        # FOOTER
        # ====================================================

        st.divider()

        st.caption(
            "AI Cognitive Learning Map — Version 1.0 | "
            "Rule-based cognitive assessment prototype"
        )