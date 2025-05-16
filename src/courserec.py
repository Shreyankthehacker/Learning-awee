import json
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from state import State


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="/home/shreyank/Gen-ai/Task-3/education/chroma_course_db", embedding_function=embedding_model)

def course_recommendation(state: State):
    query = state.query
    print("searching")
    
    results = vectorstore.similarity_search(query, k=3)

    # Load all courses from JSON file (assuming it's a list of dicts)
    with open('course.json', 'r') as f:
        courses = json.load(f)

    # Extract course names from the top-k documents
    matched_courses = []
    for doc in results:
        course_name = doc.metadata.get("course_name")
        if course_name:
            for c in courses:
                if c.get("course_name") == course_name:
                    matched_courses.append({
                        "course_name": course_name,
                        "course_url": c.get("course_url"),
                        "abstract": c.get("abstract", ""),
                        "instructor": c.get("instructor", "")
                    })
                    break  # Break after first match to avoid duplicates

    # Build the final answer
    recommendations = ["Recommended NPTEL course(s):"]
    for course in matched_courses:
        recommendations.append(f"{course['course_name']} - {course['course_url']}")

    return {"answer": state.answer + ["Recommended NPTEL courses are"]+recommendations}
