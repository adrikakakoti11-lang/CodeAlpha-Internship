import streamlit as st
from deep_translator import GoogleTranslator
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍"
)
st.markdown("""

<style>

.stApp{

    background-color:#FFF8FC;

}

h1,h2,h3{

    color:#D63384;

}

.stButton>button{

    background:#F8C8DC;

    color:black;

    border-radius:12px;

    border:none;

}

.stButton>button:hover{

    background:#F4A6C1;

}

section[data-testid="stSidebar"]{

    background:#FFEAF4;

}

textarea{

    border-radius:12px;

}

</style>

""", unsafe_allow_html=True)
st.title("🌸 AI Language Translator")
st.caption("Translate any text instantly into multiple languages 💕")
st.sidebar.title("🎀 Translator")

st.sidebar.info("""
### Features

🌍 5 Languages

⚡ Google Translate

💖 Instant Translation

✨ Built with Streamlit
""")

text = st.text_area(
    "💌 Enter your text",
    placeholder="Type something to translate..."
)
st.caption(f"Characters: {len(text)}")
languages = ["English","Assamese", "Hindi", "French", "Spanish", "German"]

source = st.selectbox("🌍 Translate From", languages)

target = st.selectbox("🌸 Translate To", languages)
translate = st.button("💖 Translate")
if translate:

    if text.strip() == "":
        st.error("💔 Please enter some text first.")    
    elif source == target:
        st.warning("🌼 Please choose two different languages.")

    else:
        translated = GoogleTranslator(
            source=source.lower(),
            target=target.lower()
        ).translate(text)

        st.success("🌸 Translation completed successfully!")

        st.subheader("💖 Your Translation")

        st.write(translated)
        st.divider()
        st.caption("Made with 💖 using Python & Streamlit")