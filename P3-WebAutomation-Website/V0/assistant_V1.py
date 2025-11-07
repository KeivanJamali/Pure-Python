import requests

context = """<Context># System Prompt
- You are privet assistant, in a KeivanJamali.com website.
- Your role is to assist the user who wants to know about Keivan Jamali: Career, Projects, Background, Abilities, Contact Info.
# STYLE AND TONE
- Be friendly and funny while talking.
- Use emojis when answering at the end.
</Context>
<data>
# Context
- Keivan Jamali is a student at Sharif University of Technology and studying transportation in there. He graduated from Sharif University of Technology for Civil engineering.
- Graduated with GPA of 4/4 in the Bachelor.
- He ranks 2th among the students.
- He has more than 4 years experience of programming with python for scientific works.
# Public information that anyone can access:
1. Website: 'KeivanJamali.com'
2. Email Address: 'me@keivanjamali.com'
3. Keivan Jamali's career <website>https://keivanjamali.com</website>
4. Keivan Jamali's Projects are available at <website>https://keivanjamali.com/keivan-jamali-project-portfolio</website>
5. Keivan Jamali's Background is available at <website>https://keivanjamali.com/keivan-jamali-civil-engineering</website>
6. Keivan Jamali's experiences are available at <webpage>https://keivanjamali.com/keivan-jamali-services</website>
7. Keivan Jamali's contact info is available at <website>https://keivanjamali.com/keivan-jamali-contact</website>
</data>
<Prompt>
According to the [data], <Question>"""

HF_API_TOKEN = ["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", "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"]
selected_model = ["google/gemma-2-27b-it", "mistralai/Mixtral-8x7B-Instruct-v0.1", "mistralai/Mistral-7B-Instruct-v0.1", "mistralai/Mistral-7B-Instruct-v0.3"]

def send_to_assistant(prompt):
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN[1]}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": f"{context}{prompt}\n\nAssistant: ",
        "options": {
            "temperature": 1,
            "stop": ["Assistant"]  # Use a list for stop conditions
        }
    }

    response = requests.post(f"https://api-inference.huggingface.co/models/{selected_model[3]}", headers=headers, json=payload)

    if response.status_code == 200:
        generated_text = response.json()[0]['generated_text'].strip()
        # Extract only the assistant's response
        if "Assistant:" in generated_text:
            assistant_response = generated_text.split("Assistant:")[-1].strip()
            return assistant_response
        return generated_text
    else:
        return f"Error: {response.text}"