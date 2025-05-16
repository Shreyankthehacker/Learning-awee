another_example_prompt = '''
You are given an example of a structured document or response.

Your task is to generate another example that follows the same structure, tone, and formatting — but with different content, keeping it logically consistent and realistic.

Instructions:
1. Carefully analyze the style, format, and data points in the provided example.
2. Generate a new example that could logically follow or be used as a sibling example.
3. Maintain the same level of detail and type of content.
4. Do not copy or paraphrase — create original data with the same schema.

Example:
{query}

Now, generate one more example in the exact same structure.
'''

similar_question = '''
You are given a question. Your task is to generate 3 similar questions that ask about the same topic or intent but are phrased differently.

Guidelines:
1. Preserve the core meaning of the question.
2. Use different wording, sentence structure, or question style (e.g., descriptive, interrogative, comparative).
3. Keep the tone and difficulty level consistent.
4. Avoid exact synonyms in all versions — be creative in rephrasing.

Example:
Original Question: What are the applications of soft matter physics?

Similar Questions:
1. How is soft matter physics applied in real-world scenarios?
2. What are some practical uses of soft matter in industry and research?
3. In which fields is soft matter physics commonly utilized?

Now, generate 3 similar questions for the following:

Original Question:{query}
'''

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
