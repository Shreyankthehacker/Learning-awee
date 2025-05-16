from IPython.display import Video
import subprocess
import warnings 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import re
from state import State
from llms import llm


template_for_manim = '''
You are an expert in using Manim (Mathematical Animation Engine) to create beautiful and precise mathematical animations using Python code.

Your task is to generate Manim Python code based solely on:

1. A **math-related query** (e.g., explain Pythagoras' theorem visually, show vector addition, illustrate derivative on a graph).
2. A **simple visual description** or example for how it could be animated — only using **text** or **emojis**, no images.

⚠️ Guidelines:
- Only output valid Python code compatible with Manim Community Edition.
- Do not include any text explanation or description — return **code only**.
- Do not use images or external assets — use only text (like Tex, MathTex, MarkupText) or emojis when needed.
- Try your best to match the query and visualization using Manim's animation capabilities.

IMPORTANT: You must output **only the raw executable Python code**, with no additional text, no comments, no markdown fences (no triple backticks or 'python' tags), and no other formatting or explanation before or after the code.

At the very end of your code, add the line:
print("enjoy animation")

Write the code in such a way that the animation should be pleasing to watch with colour and make sure words don't overlap on one another.

INPUT FORMAT:
Query: {query}
Example: {example}

OUTPUT FORMAT:
Only the Python code (for Manim), exactly as it should be saved in a `.py` file, with nothing else.

Now generate the code.
'''

eg_template = prompt = (
    "You are a helpful and knowledgeable math tutor.\n"
    "I will give you either a math problem or just the name of a topic.\n"
    "If I give you a math problem, solve it step by step with clear and concise explanations.\n"
    "If I give you only a topic name, return a simple but effective example problem along with a full solution that helps explain the topic.\n"
    "Keep your responses easy to understand and focused on building intuition."

    "Input format :"
    "Query:{query}"
)

topic_chain = ChatPromptTemplate.from_template(eg_template) | llm | StrOutputParser()



prompt_manim = ChatPromptTemplate.from_template(template_for_manim)

chain = prompt_manim | llm | StrOutputParser()


import subprocess

def video_animation(state: State):
    query = state.query

    example = topic_chain.invoke({'query': query})
    result = chain.invoke({'query': query, 'example': example})

    print("Initial generated code:")
    print(result)

    marker = "from manim import *"
    sindex = result.find(marker)
    if sindex == -1:
        return {"error": "Generated code not found in output."}
    

    lindex = result.rfind("```")
   
    code = result[sindex:lindex]

    max_attempts = 3
    attempt = 0

    while attempt < max_attempts:
        with open("hello.py", "w") as f:
            f.write(code)

        
        process = subprocess.run(
            ['manim', '-pql', 'hello.py'],
            capture_output=True,
            text=True
        )

        if process.returncode == 0:
            print("Manim ran successfully.")
            break  

        
        error_message = process.stderr
        print(f"Manim error on attempt {attempt+1}:\n{error_message}")

        
        fix_prompt = (
            f"The following Manim code failed to run with error:\n{error_message}\n\n"
            f"Please fix the code so it runs successfully: annd just return the python code that is executable and directly able to write in .py file i dont want anything additional\n\n{code}"
        )

        fixed_result = llm.invoke(fix_prompt)
        fixed_code_start = fixed_result.content.find(marker)
        if fixed_code_start == -1:
            
            return {"error": "LLM did not return valid fixed code.", "llm_response": fixed_result.content}
        index = fixed_result.rfind("```")

        code = fixed_result.content[fixed_code_start:index].strip()
        attempt += 1

    if attempt == max_attempts and process.returncode != 0:
        
        return {"error": "Failed to generate runnable Manim code after multiple attempts.", "last_error": error_message}

    return {"State": state, "message": "Manim animation generated and ran successfully."}



    
