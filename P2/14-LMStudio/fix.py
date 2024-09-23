import openai
import requests

# Set your local LM Studio server URL
openai.api_base = "http://localhost:1234/v1"

# Define your model name
mistral = "TheBloke/Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q4_0.gguf"
llama = "QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/Meta-Llama-3-8B-Instruct.Q4_0.gguf"


# Function to get available models
def list_models():
    response = requests.get(f"{openai.api_base}/models")
    return response.json()

# Function to generate a chat completion with system, user, and assistant roles
def generate_chat_completion(prompt,
                             max_tokens=100, 
                             temperature=0.7, 
                             top_p=0.9, 
                             n=1, 
                             presence_penalty=0.5,
                             frequency_penalty=1.1,
                             stream=False):
    response = requests.post(
        f"{openai.api_base}/completions",
        json={
            "model": selected_model,
            "prompt": prompt,  # Here we can pass the conversation format, instead of prompt- we can use message.
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "n": n,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty,
            "stream": stream
        }
    )
    return response.json()["choices"][0]["message"]["content"].strip()

selected_model = mistral
# Create a conversation structure
# messages = [
#     {"role": "system", "content": "You are a dog. You can only barks."},  # Set the system prompt to guide behavior
#     {"role": "user", "content": "hello. Do you like to play a game?"}  # User's input
# ]
# create prompt
# print("Available models:", list_models())

while True:
    prompt = input("Prompt: ")
    if prompt in ["exit", "buy"]:
        break
    print("GPT   ======   ", generate_chat_completion(prompt))
