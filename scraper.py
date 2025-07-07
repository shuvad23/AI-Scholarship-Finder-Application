from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
import os 
from dotenv import load_dotenv
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
@tool
def fetch_scholarships(subject: str = "Machine Learning", country: str = "Germany",level:str="Bachelor") -> str:
    """
    Search scholarships by subject and country using Tavily Search.

    Args:
        subject: Field of study or scholarship topic, e.g. "Machine Learning".
        country: Country of study or scholarship location, e.g. "Germany".

    Returns:
        A formatted string listing top scholarship results with titles, URLs, and snippets.
    """
    query = f"{subject} for {level} scholarships in {country}"
    tavily = TavilySearchResults(k=10)
    results = tavily.run(query)

    output = ""
    for i, item in enumerate(results):
        output += f"{i+1}. {item['title']}\n🔗 {item['url']}\n📝 {item['content']}\n\n"

    return output.strip()


@tool
def search_daad_scholarships(field: str = "Machine Learning", country: str = "Germany",level:str="Bachelor") -> str:
    """
    Search DAAD for scholarships using Tavily Search.
    Args:
        subject: Field of study or scholarship topic, e.g. "Machine Learning".
        country: Country of study or scholarship location, e.g. "Germany".

    Returns:
        A formatted string listing top scholarship results with titles, URLs, and snippets.
    """
    query = f"{field} for {level} scholarships in {country} site:daad.de"
    tavily = TavilySearchResults(k=5)
    results = tavily.run(query)

    output = ""
    for r in results:
        output += f"{r['title']}\n🔗 {r['url']}\n📝 {r['content']}\n\n"

    return output.strip()

from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

@tool
def fetch_usa_scholarships(field: str = "Machine Learning", country: str = "USA",level:str="Bachelor") -> str:
    """
    Search for scholarships to study in the USA using Tavily Search.

    Args:
        subject: Field of study (e.g., "AI", "Medicine", etc.)

    Returns:
        A formatted list of scholarship opportunities with titles, URLs, and descriptions.
    """
    query = f"{field} for {level} scholarships in {country} for international students site:scholarships.com OR site:studyusa.com OR site:educationusa.state.gov"
    search = TavilySearchResults(k=5)
    results = search.run(query)

    output = ""
    for i, r in enumerate(results):
        output += f"{i+1}. {r['title']}\n🔗 {r['url']}\n📝 {r['content']}\n\n"

    return output.strip()

@tool
def fetch_india_scholarships(subject: str = "Computer Science") -> str:
    """
    Get real scholarship listings to study in India using Tavily Search API.
    """
    query = f"{subject} scholarships for international students to study in India site:scholarships.gov.in OR site:buddy4study.com"
    tavily = TavilySearchResults(k=5)
    results = tavily.run(query)

    output = ""
    for i, r in enumerate(results):
        output += f"{i+1}. {r['title']}\n🔗 {r['url']}\n📝 {r['content']}\n\n"

    return output.strip()


from langchain.tools import tool
import requests
from bs4 import BeautifulSoup

@tool
def fetch_erasmus_mundus_scholarships(query: str = "Erasmus Mundus Computer Science") -> str:
    """
    Search and summarize Erasmus Mundus Joint Master’s scholarships
    related to the query using web scraping of the official catalogue
    or using a keyword-based search on scholarship aggregator sites.
    
    Args:
        query: Search term to find relevant Erasmus Mundus programs.

    Returns:
        Formatted string listing top Erasmus Mundus programs with titles and URLs.
    """

    query = f"{query} scholarships for international students to study in Europe site:https://eacea.ec.europa.eu/erasmus-plus/actions/key-action-1/erasmus-mundus-joint-master-degrees_en"
    tavily = TavilySearchResults(k=5)
    results = tavily.run(query)

    output = ""
    for i, r in enumerate(results):
        output += f"{i+1}. {r['title']}\n🔗 {r['url']}\n📝 {r['content']}\n\n"

    return output.strip()

