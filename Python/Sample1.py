import streamlit as st
import time
import pandas as pd

# Simulated data
confluence_content = "This page contains information about the leave policy, reimbursement process, and contact details for HR support."
metadata = {
    "Title": "Leave and Reimbursement Policy",
    "Last Updated": "2025-03-24",
    "Author": "HR Team",
    "Tags": ["leave", "reimbursement", "HR"]
}
suggested_questions = [
    "What is the leave policy?",
    "How can I claim travel reimbursement?",
    "Who should I contact for HR queries?"
]
answer_text = "Employees are entitled to 20 days of annual leave. To claim travel reimbursement, submit the required documents to HR within 30 days."

# Page config
st.set_page_config(page_title="Confluence QnA", layout="centered")

# Title
st.markdown("## 📄 Confluence Knowledge Base QnA")

# Spinner to simulate loading
with st.spinner("Fetching content from Confluence..."):
    time.sleep(1.5)

# Tabs for layout
tab1, tab2 = st.tabs(["Ask Question", "View Metadata"])

with tab1:
    selected_prompt = st.selectbox("💡 Choose a suggested question:", suggested_questions)
    user_question = st.text_input("❓ Enter your question:", value=selected_prompt)

    if st.button("Submit", use_container_width=True):
        st.toast("Question submitted successfully.")
        st.text_area("🧠 Answer:", value=answer_text, height=300)

    if st.button("🔄 Refresh Knowledge Base", use_container_width=True, type="primary"):
        st.session_state.setupComplete = False
        st.toast("Knowledge base is being refreshed...")

with tab2:
    with st.expander("📌 Metadata Details"):
        st.json(metadata)

    st.markdown("### 🏷️ Tags Table")
    df_tags = pd.DataFrame(metadata["Tags"], columns=["Tags"])
    st.table(df_tags)
