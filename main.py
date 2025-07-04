# task1_educhain_setup.py

"""
Task 1: EduChain Environment Setup Script
- Install EduChain library
- Generate educational content
- Format output as JSON
"""

from educhain import Educhain
import json

def main():
    # Initialize EduChain client
    client = Educhain()

    # Generate multiple-choice questions
    mcqs = client.qna_engine.generate_questions(
        topic="Python Programming Basics",
        num=5,
        question_type="Multiple Choice",
        custom_instructions="Basic beginner-level questions."
    )

    # Show the questions in console
    print("Generated Questions:")
    mcqs.show()

    # Convert questions to JSON
    mcq_json = mcqs.json()

    # Generate lesson plan (we'll do this as a text-based set of instructions)
    lesson_plan_text = f"""
Lesson Plan for: Python Programming Basics

1. Introduction to Python
2. Variables and Data Types
3. Conditional Statements
4. Loops
5. Functions
6. Basic File Handling
7. Recap and Q&A
"""

    # Prepare final output
    output = {
        "generated_mcqs": json.loads(mcq_json),
        "lesson_plan": lesson_plan_text.strip()
    }

    # Save to file
    with open("task1_output.json", "w") as f:
        json.dump(output, f, indent=2)

    # Print summary
    print("\nTask 1 Completed. Output saved to 'task1_output.json'.")

if __name__ == "__main__":
    main()
