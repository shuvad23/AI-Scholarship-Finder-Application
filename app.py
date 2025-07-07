# app.py
import streamlit as st
from scraper import fetch_scholarships
from gemini_helper import generate_text
from utils import format_prompt

st.set_page_config("AI Scholarship Finder")

st.title("🎓 AI-Powered Scholarship Finder")
st.markdown("Get personalized scholarship suggestions based on your profile.")

with st.form("profile_form"):
    name = st.text_input("Name")
    country = st.selectbox("Your Country", ["Bangladesh", "India", "Germany", "USA","UK"])
    field = st.text_input("Field of Study", "Computer Science")
    level = st.selectbox("Degree Level", ["Bachelor", "Master", "PhD"])
    preferred_destinations = st.selectbox("preferred_destinations",["India", "Germany", "USA","UK"])

    submitted = st.form_submit_button("Find Scholarships")

if submitted:
    st.info("🔎 Searching for scholarships...")
    # scholarships = fetch_scholarships(keyword)


    profile = f"{name}, from {country}, wants to study {field} at {preferred_destinations} level."

    st.info("💡 Asking Gemini for suggestions...")
    with st.spinner("Generating response..."):
        recommendation = generate_text(name,country,level,field,preferred_destinations)

    st.subheader("🎯 Gemini Recommendations")
    st.write(recommendation)
