import os
from dotenv import load_dotenv
from openai import OpenAI
import time

load_dotenv()

OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPEN_AI_KEY)


def summarize_text(input_file, output_file):
    try:
        start_time = time.time()  # Record start time

        # Read input text from the file
        with open(input_file, 'r', encoding='utf-8') as file:
            input_text = file.read()

        # Split input text into smaller segments (e.g., by paragraph)
        # Split by double newline (assumes paragraphs are separated by double newline)
        segments = input_text.split('\n\n')

        # Initialize summarized text
        summarized_text = ''

        # Process each segment individually
        for segment in segments:
            # Append a brief introduction as the prompt
            prompt = f"The following is a summary of the provided text: {segment} using bullet points. The summary must be readable and divided within the chapters for a presentation. The answer must be wrriten in french. Also, tell more about the story itself, developpe it and give me enough information so I would be able to tell it during the presentation without looking dumb\n"

            # Request summarization from OpenAI API using the gpt-4-turbo model
            completion = client.chat.completions.create(
                model="gpt-4-turbo",  # Specify the appropriate model
                messages=[
                    {"role": "system", "content": prompt},
                ],
                max_tokens=4000,  # Adjust the token limit as needed
            )

            # Extract and append summarized text from the response
            summarized_text += completion.choices[0].message.content.strip() + \
                '\n\n'

        # Write summarized text to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(summarized_text)

        print(f"Summarized text written to '{output_file}'")

        end_time = time.time()  # Record end time
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_file = 'input.txt'
output_file = 'output.md'
summarize_text(input_file, output_file)
