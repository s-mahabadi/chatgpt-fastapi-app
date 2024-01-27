import openai

from _keys import OPENAI_API_KEY
# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = OPENAI_API_KEY

# Set the model and prompt
# model_engine = "text-davinci-003"
# prompt = "写一篇AI芯片论文"
model_engine = "gpt-3.5-turbo"
prompt = "Hello, I am a first try at connecting to you through an API call"

# Set the maximum number of tokens to generate in the response
max_tokens = 128

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response
print(completion.choices[0].text)

