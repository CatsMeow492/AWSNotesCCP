import openai
import os

# Load your OpenAI API key
openai.api_key = os.getenv('YOUR_OPENAI_API_KEY')

# Read the contents of failed_questions.txt
failed_questions_file = 'failed_questions.txt'
with open(failed_questions_file, 'r') as file:
    failed_questions = file.readlines()

# Prepare the prompt for ChatGPT
# Note: Customize this prompt as needed to fit the style of summary you're looking for
prompt = "Create a study guide summary based on the following topics:\n\n" + "".join(f"- {question}" for question in failed_questions)

# Query the ChatGPT API
response = openai.Completion.create(
  engine="text-davinci-003", # or another version if you prefer
  prompt=prompt,
  temperature=0.7,
  max_tokens=500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

# Print the generated study guide summary
print(response.choices[0].text.strip())
