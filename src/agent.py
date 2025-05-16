from langgraph.graph import StateGraph,START,END
from state import State
from query import get_query
from animation import video_animation
from nodes import get_example,get_similar_questions,bookrec,youtube_search_serpapi,wiki_explainer_tool
from courserec import course_recommendation



builder = StateGraph(State)

builder.add_node(get_query)
builder.add_node("video_animation",video_animation)
builder.add_node("Example Generator",get_example)
builder.add_node(course_recommendation)
builder.add_node("Similar questions",get_similar_questions)
builder.add_node("book Recommendations",bookrec)
builder.add_node("Blogs",wiki_explainer_tool)
builder.add_node("Youtube recommendations",youtube_search_serpapi)


builder.add_edge(START,"get_query")
builder.add_edge("get_query","video_animation")
builder.add_edge("get_query","Example Generator")
builder.add_edge("get_query","course_recommendation")
builder.add_edge("get_query","Similar questions")
builder.add_edge("get_query",'book Recommendations')
builder.add_edge("get_query",'Blogs')
builder.add_edge("get_query",'Youtube recommendations')

graph = builder.compile()

state = State(query = '',answer= [])
state = graph.invoke(state)