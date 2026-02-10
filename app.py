import streamlit as st
import pandas as pd
from ai_engine import analyze_feedback
from prd_generator import generate_prd
from roadmap_generator import generate_roadmap

st.set_page_config(page_title="AI Product Copilot – QZIN", layout="wide")

st.title("AI Product Copilot – QZIN")
st.subheader("AI-Powered Product Discovery (Demo Mode)")

data = pd.read_excel("data/qzin_feedback.xlsx")

st.markdown("## Raw User Feedback")
st.dataframe(data.head(15))

if st.button("Run AI Analysis"):
    data["AI Insights"] = data["feedback_text"].apply(analyze_feedback)

    data["Category"] = data["AI Insights"].str.extract(r"Category: (.*)")
    category_counts = data["Category"].value_counts()

    st.markdown("## 🔝 Top Problem Categories")
    st.bar_chart(category_counts)

    top_issue = category_counts.idxmax()

    st.markdown("## 📄 Auto-Generated PRD")
    st.text(generate_prd(top_issue))

    st.markdown("## 🗺 Product Roadmap")
    roadmap = generate_roadmap(top_issue)

    col1, col2, col3 = st.columns(3)
    for col, key in zip([col1, col2, col3], ["Now", "Next", "Later"]):
        with col:
            st.subheader(key)
            for item in roadmap[key]:
                st.write("•", item)
