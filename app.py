import streamlit as st
from textblob import TextBlob

st.title("AI Interview / Presentation Tone Checker")

text = st.text_area(
    "Paste your interview or presentation response here:",
    height=200
)

if st.button("Analyze Tone"):

    if text.strip() == "":
        st.warning("Please enter some text")

    else:
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity

        if polarity >= 0.5:
            tone = "Highly Confident"
        elif polarity >= 0.2:
            tone = "Confident"
        elif polarity >= 0:
            tone = "Neutral"
        elif polarity >= -0.2:
            tone = "Nervous"
        else:
            tone = "Low Confidence / Negative"

        confidence_score = int((polarity + 1) * 50)

        st.subheader("Analysis Result")
        st.write("🎯 Detected Tone:", tone)
        st.write("📊 Polarity Score:", polarity)
        st.write("🧠 Subjectivity Score:", subjectivity)
        st.metric("Confidence Score", f"{confidence_score}%")
        st.progress(confidence_score)

        st.subheader("Feedback & Suggestions")

        if polarity < 0:
            st.write("🔹 Use more positive and confident words.")
            st.write("🔹 Avoid negative phrasing.")
        else:
            st.write("🔹 Your tone is good. Maintain clarity and confidence.")