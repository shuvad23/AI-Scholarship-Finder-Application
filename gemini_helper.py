# gemini_api.py
from langchain_core.messages import HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
from scraper import fetch_scholarships,search_daad_scholarships,fetch_usa_scholarships,fetch_india_scholarships,fetch_erasmus_mundus_scholarships
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_text(user_name,user_country,user_level,user_field,preferred_destinations):

    system_prompt = f"""
                You are an expert AI advisor specialized in helping international students find scholarships and plan their academic future.


                🎯 Your task:
                1. Search and summarize real, currently available scholarships that match his profile.
                2. Include details: title, degree level, eligibility, deadline, country, link.
            
                4. Recommend at least 10 top scholarships and give specific reasons for each.
                5. If there are few scholarships available, suggest:
                - Partial funding, internships, or alternate pathways
                - Trusted platforms to register and get updates

                💡 Then, give Shuva a personalized **Scholarship Roadmap**:
                - What to prepare (transcripts, tests, documents)
                - When to apply (best timeline)
                - How to improve chances (certifications, projects, platforms to follow)
                - Websites to track (e.g., buddy4study, scholarships.gov.in, etc.)

                User profile:
                - user_name:{user_name}
                - Country: {user_country}
                - Study level: {user_level}
                - Field of interest: {user_field}
                - Preferred countries: {preferred_destinations}

                📌 Format clearly:
                - 📌 **Scholarship Name**  
                - 🎓 Degree:  
                - 🧪 Field:  
                - 🌍 For:  
                - ⏳ Deadline:  
                - 🔗 Link:  
                - ✅ Why it fits your profile

                # finally : give some most top relevant(user) reference link to find scholarship with top most website
                🔚 End with a warm motivational note to encourage him to keep going.
                """

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.5
    )
    tools = [fetch_scholarships,search_daad_scholarships,fetch_usa_scholarships,fetch_india_scholarships]
    # tools =[]
    agent_execute = create_react_agent(model=llm,tools=tools)

    response_result = ""
    for chunk in agent_execute.stream({"messages": [HumanMessage(content=system_prompt)]}):
        if "agent" in chunk and "messages" in chunk["agent"]:
            for message in chunk["agent"]["messages"]:
                response_result += message.content

    return response_result