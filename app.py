import streamlit as st
from analyze import analyze_text

st.set_page_config(page_title="HermesAI", layout="wide")
st.sidebar.title("HermesAI Navigation 🪽")

# Page state
if "page" not in st.session_state:
    st.session_state.page = "Input"

# Sidebar Navigation
if st.sidebar.button("📝 Input Page"):
    st.session_state.page = "Input"
if st.sidebar.button("🧠 AI Analysis"):
    st.session_state.page = "AI Analysis"

# User input state
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# -------------------- INPUT PAGE --------------------
if st.session_state.page == "Input":
    st.subheader("Enter Call Transcript or Complaint Message:")
    user_input = st.text_area("📨 Call Transcript:", placeholder="e.g., Where is my order? It's been 5 days...", height=150)
    if st.button("Submit Complaint"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a message before submitting.")
        else:
            st.session_state.user_input = user_input
            st.success("✅ Message received! Click 'AI Analysis' on the left.")

# -------------------- AI ANALYSIS PAGE --------------------
elif st.session_state.page == "AI Analysis":
    st.markdown("<h1 style='text-align: center;'>🪽 HermesAI</h1>", unsafe_allow_html=True)

    if st.session_state.user_input == "":
        st.info("No input yet. Please enter a complaint on the 'Input Page'.")
    else:
        result = analyze_text(st.session_state.user_input)

        # Normalize values
        rating = int(round(result["Forecasted Rating"]))
        stars = "⭐" * rating
        avg_wait = f"{result['Avg Waiting time']} min"
        predicted_time = f"{result['Predicted time to fix']} min"
        estimated_duration = f"{result['Avg call time']} min"
        next_line = result["Next sentence to say"]
        classification = result["Issue Classification"]
        solution = result["Possible Solutions"]
        emotion = result.get("Customer Emotion", "🤔")

        # Layout: Call Time (Left) + Rating/Emotion/Issue (Right)
        left_col, right_col = st.columns([2, 1])
        with left_col:
            st.subheader("⏱ Call Metrics")
            st.metric("Predicted Call Time", predicted_time)
            st.metric("Avg Wait Time", avg_wait)
            st.metric("Estimated Duration", estimated_duration)
        with right_col:
            st.subheader("Predicted Rating")
            st.markdown(f"<h3>{stars}</h3><p>({rating}/5)</p>", unsafe_allow_html=True)

            st.markdown("### Customer Emotion")
            st.markdown(f"<div style='font-size:48px'>{emotion}</div>", unsafe_allow_html=True)

            st.markdown("### Issue Classification")
            st.markdown(f"_{classification}_")

        st.markdown("---")

        # Call Summary
        st.subheader("📞 Call Summary")
        st.markdown(f"**Call Transcript:** _{st.session_state.user_input}_")
        st.markdown(f"**Next Sentence to Say:** _{next_line}_")
        st.markdown(f"**Suggested Solution:** _{solution}_")