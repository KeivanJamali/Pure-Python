from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="microsoft/Phi-3-medium-4k-instruct", trust_remote_code=True)
pipe(messages)