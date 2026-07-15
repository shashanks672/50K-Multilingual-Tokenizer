import streamlit as st
import pandas as pd
import random
from tokenizers import Tokenizer

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="50K Multilingual Tokenizer",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.hero{
background: linear-gradient(135deg,#6C63FF,#4F8BF9,#00C9A7);
padding:35px;
border-radius:20px;
color:white;
box-shadow:0 8px 25px rgba(0,0,0,.2);
margin-bottom:25px;
}

.hero h1{
font-size:42px;
margin-bottom:5px;
}

.hero p{
font-size:18px;
opacity:.95;
}

.metric-box{
background:white;
padding:20px;
border-radius:18px;
box-shadow:0px 5px 18px rgba(0,0,0,.08);
text-align:center;
}

.token-chip{
display:inline-block;
padding:10px 18px;
margin:6px;
border-radius:30px;
color:white;
font-weight:bold;
font-size:15px;
}

.footer{
text-align:center;
padding:25px;
color:gray;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Tokenizer
# -----------------------------
tokenizer = Tokenizer.from_file("tokenizer_50k.json")

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero">
<h1>🤖 50K Multilingual Tokenizer</h1>
<p>
English 🇬🇧 | हिन्दी 🇮🇳 | ಕನ್ನಡ 🇮🇳 | தமிழ் 🇮🇳
<br>
Custom BPE Tokenizer (50,000 Vocabulary)
</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Example Buttons
# -----------------------------
c1,c2,c3,c4 = st.columns(4)

if c1.button("🇬🇧 English"):
    st.session_state.text="Hello, welcome to our tokenizer demo."

if c2.button("🇮🇳 Hindi"):
    st.session_state.text="नमस्ते, आप कैसे हैं?"

if c3.button("🇮🇳 Kannada"):
    st.session_state.text="ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಾ?"

if c4.button("🇮🇳 Tamil"):
    st.session_state.text="வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?"

text = st.text_area(
    "Enter Text",
    value=st.session_state.get("text",""),
    height=180
)

if st.button("🚀 Tokenize",use_container_width=True):

    encoding = tokenizer.encode(text)

    tokens = encoding.tokens
    ids = encoding.ids

    st.divider()

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-box">
        <h2>📝</h2>
        <h1>{len(text)}</h1>
        <p>Characters</p>
        </div>
        """,unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-box">
        <h2>🔖</h2>
        <h1>{len(tokens)}</h1>
        <p>Tokens</p>
        </div>
        """,unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-box">
        <h2>📚</h2>
        <h1>50K</h1>
        <p>Vocabulary</p>
        </div>
        """,unsafe_allow_html=True)

    st.markdown("## 🎨 Generated Tokens")

    colors=[
        "#6C63FF",
        "#00C9A7",
        "#F39C12",
        "#FF5E7E",
        "#3498DB",
        "#8E44AD",
        "#16A085",
        "#E74C3C"
    ]

    html=""

    for token in tokens:
        color=random.choice(colors)
        html+=f"""
        <span class='token-chip'
        style='background:{color};'>
        {token}
        </span>
        """

    st.markdown(html,unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## 📋 Token Information")

    df=pd.DataFrame({
        "Token":tokens,
        "Token ID":ids
    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

st.markdown("""
<div class="footer">
Made with ❤️ using Streamlit & Hugging Face Tokenizers
</div>
""",unsafe_allow_html=True)