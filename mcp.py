# mcp_server.py

"""
Task 2: MCP Server integrated with EduChain
- Provides tools and resources:
  - Generate MCQs
  - Generate Lesson Plan
  - Bonus: Generate Flashcards
"""

import json
from mcp_sdk import Server, Tool, Resource
from educhain import Educhain

# Initialize EduChain client
client = Educhain()

# Tool: Generate MCQs
def generate_mcqs(topic: str, num_questions: int = 5) -> dict:
    """
    Generate multiple-choice questions for a given topic.
    """
    result = client.qna_engine.generate_questions(
        topic=topic,
        num=num_questions,
        question_type="Multiple Choice",
        custom_instructions="Basic questions for educational purposes."
    )
    return json.loads(result.json())

# Resource: Generate Lesson Plan
def get_lesson_plan(subject: str) -> dict:
    """
    Return a lesson plan text for a given subject.
    """
    lesson_plan = f"""
Lesson Plan for: {subject}

1. Introduction to {subject}
2. Key Concepts Overview
3. Examples and Exercises
4. Review and Q&A
"""
    return {"subject": subject, "lesson_plan": lesson_plan.strip()}

# Bonus Tool: Generate Flashcards
def generate_flashcards(topic: str, num_cards: int = 5) -> dict:
    """
    Generate flashcards for a given topic.
    """
    flashcards = []
    for i in range(num_cards):
        flashcards.append({
            "question": f"Explain concept {i + 1} in {topic}.",
            "answer": f"This is the explanation for concept {i + 1}."
        })
    return {"topic": topic, "flashcards": flashcards}

# Create MCP server
server = Server(name="EduChainMCPServer")

# Register the tools and resources
server.register_tool(
    Tool(
        name="generate_mcqs",
        description="Generate multiple-choice questions for a topic.",
        func=generate_mcqs
    )
)

server.register_resource(
    Resource(
        name="get_lesson_plan",
        description="Provide a lesson plan for a subject.",
        func=get_lesson_plan
    )
)

server.register_tool(
    Tool(
        name="generate_flashcards",
        description="Generate flashcards for a topic.",
        func=generate_flashcards
    )
)

if __name__ == "__main__":
    print("Starting MCP server with EduChain...")
    server.run()
