from serpapi import GoogleSearch # type: ignore
import os 
from state import State
from dotenv import load_dotenv
from chains import simq_chain,example_chain
load_dotenv()

SERP = os.getenv('SERPAPI_API_KEY')

def youtube_search_serpapi(state:State):
    print("yt")
    params = {
        "engine": "youtube",
        "search_query": state.query,
        "api_key":SERP
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    videos = results.get("video_results", [])[:5]
    print(videos)
    formatted_results = [
        f"{i + 1}. {v.get('title')}\n   {v.get('link')}"
        for i, v in enumerate(videos)
    ]

    return {'answer':state.answer+["Youtube videos that you can go through are"]+[formatted_results]}


def get_similar_questions(state:State):
    result = simq_chain.invoke({'query':state.query})
    return {'answer':state.answer+[result]}
def get_example(state:State):
    result = example_chain.invoke({'query':state.query})
    return {'answer':state.answer+[result]}


def bookrec(state: State):
    params = {
        "engine": "google",
        "q":f"{state.query} related boks", 
        "api_key": SERP,    # your SerpAPI key as a string or env var
        "num": 5           # get top 5 results
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get("organic_results", [])[:5]
    print(organic_results)

    formatted_results = [
        f"{i + 1}. {res.get('title')}\n   {res.get('link')}"
        for i, res in enumerate(organic_results)
    ]

    return {'answer': state.answer + ["Google search results:"] + formatted_results}


import wikipedia

def wiki_explainer_tool(state):
    """Explains a topic using Wikipedia summary."""
    print("wiki")
    #result = llm.invoke({f" i want to get blogs realted to {state.query} from wen search for that get me a suitable searching query so that i can execute and get the blogs related to this query"})
    try:
        out = wikipedia.summary(state.query, sentences=5)
    except Exception as e:
       return {'answer':state.answer}
    return {'answer':state.answer+["Wikipidea information"]+[out]}


