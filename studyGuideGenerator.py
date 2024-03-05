import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv('OPEN_AI')

def generate_study_guide():
    
    print("working on it...")
    
    with open('questionShuffler/failed_questions.txt', 'r') as file:
        failed_questions = file.read()
    
    prompt = (
        f"I answered the following questions incorrectly.\n"
        f"Can you generate a short intuitive study guide to help me understand the underlying concepts?\n"
        f"I'll tip you $200 if you do a good job. Generate the study guide in .md format.\n"
        f"{failed_questions}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        with open('study_guide.md', 'w') as output_file:
            output_file.write(response['choices'][0]['message']['content'])
            print("Study guide generated successfully!")
    
    except Exception as e:
        print(f"Error generating study guide: {str(e)}")



generate_study_guide()