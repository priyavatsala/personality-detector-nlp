import streamlit as st
from src.predict import predict_personality

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Personality Detector",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #12001f, #1f1147, #12001f);
    color: white;
}

.main-title {
    font-size: 70px;
    font-weight: bold;
    text-align: center;
    background: linear-gradient(to right, #ff66c4, #b896ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    font-size: 30px;
    color: #c7a6ff;
    margin-top: -20px;
}

.description {
    text-align: center;
    color: #cfcfcf;
    font-size: 22px;
    max-width: 900px;
    margin: auto;
    padding-top: 20px;
}

.card {
    background-color: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 30px;
}

.stTextArea textarea {
    background-color: #1b1038 !important;
    color: white !important;
    border-radius: 15px !important;
    border: 1px solid #7c4dff !important;
    font-size: 18px !important;
}

.stButton button {
    background: linear-gradient(to right, #9333ea, #06b6d4);
    color: white;
    border: none;
    border-radius: 30px;
    padding: 12px 30px;
    font-size: 18px;
    font-weight: bold;
}

.result-box {
    background: rgba(0,255,150,0.1);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(0,255,150,0.3);
    margin-top: 20px;
    font-size: 24px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown("""
<div style='display:flex; justify-content:center; gap:20px; margin-top:20px;'>

<div class='card' style='padding:12px 25px;'>📖 About Project</div>

<div class='card' style='padding:12px 25px;'>⚙️ Tech Stack</div>

<div class='card' style='padding:12px 25px;'>💡 How It Works</div>

</div>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("<h1 class='main-title'>Personality Detector</h1>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>using Natural Language Processing</p>", unsafe_allow_html=True)

st.markdown("""
<p class='description'>
Discover your MBTI personality type through AI-powered text analysis.
Share your thoughts, communication style, interests, and preferences.
</p>
""", unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("✍️ Write about yourself")

user_input = st.text_area(
    "",
    height=220,
    placeholder="Tell us about your interests, communication style, hobbies, decision making, or personality..."
)

if st.button("✨ Predict Personality"):

    if user_input.strip() != "":

        with st.spinner("Analyzing personality traits..."):

            result = predict_personality(user_input)

        st.markdown(f"""
        <div class='result-box'>
        🎯 Predicted Personality Type: <b>{result}</b>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("Please enter some text.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- INFO CARDS ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
    <h2>📌 About This Project</h2>

    <p>✔️ AI-powered MBTI prediction system</p>
    <p>✔️ NLP-based text analysis</p>
    <p>✔️ Real-time personality detection</p>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h2>⚡ How It Works</h2>

    <p>1️⃣ User provides text input</p>
    <p>2️⃣ NLP extracts linguistic features</p>
    <p>3️⃣ AI predicts MBTI personality</p>

    </div>
    """, unsafe_allow_html=True)