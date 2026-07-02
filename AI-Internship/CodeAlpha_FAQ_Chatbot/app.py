import streamlit as st
if "messages" not in st.session_state:
    st.session_state.messages = []

st.set_page_config(
    page_title="🤖 FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)
st.sidebar.title("🤖 FAQ Chatbot")

st.sidebar.info(
    """
    This chatbot can answer questions about:

    • AI
    • Python
    • Machine Learning
    • Streamlit
    """
)

st.title("🤖 FAQ Chatbot")
st.write(
    "Welcome! 👋 Ask me questions about AI, Python, Machine Learning or Streamlit."
)

# Sample FAQs
faq = {
    "ai": "AI stands for Artificial Intelligence. It enables computers to perform tasks that usually require human intelligence.",

    "python": "Python is a simple and powerful programming language used for web development, AI, data science, and automation.",

    "machine learning": "Machine Learning is a branch of AI where computers learn patterns from data instead of being explicitly programmed.",

    "streamlit": "Streamlit is a Python framework used to build interactive web applications quickly."
}
st.sidebar.metric("FAQs Available", len(faq))

st.subheader("Ask a Question")
question = st.text_input(
    "💬 Ask me anything...",
    placeholder="Example: What is AI?"
)
if st.button("Clear"):
    st.session_state.messages = []

    st.rerun()

question = question.strip().lower()

found = False

for keyword, answer in faq.items():
    if keyword in question:
        st.success(answer) 
        st.session_state.messages.append(("You", question))
        st.session_state.messages.append(("Bot", answer))
        found = True
        break

if question != "" and not found:

    st.warning(
    "I couldn't find an answer. Try asking about AI, Python, Machine Learning or Streamlit."
)
    st.divider()

st.subheader("💬 Conversation")

for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f"🧑 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")
        st.sidebar.metric("Messages", len(st.session_state.messages))
        st.divider()
        st.caption("Made with ❤️ using Python and Streamlit") 