import requests
import requests
from PIL import Image
from io import BytesIO
import pytesseract
from openai import OpenAI
import re

class DivarContest:
    def __init__(self, api_token):
        self.api_token = api_token
        self.model = "gpt-4.1-mini"
        self.client = OpenAI(api_key=self.api_token, base_url="https://api.metisai.ir/openai/v1")

    def capture_the_flag(self, question):
        url = self.extract_url(question)
        image = self.download_image(url)
        ciphertext = self.extract_text(image)
        prompt = f"""You are a true expert in the field of cybersecurity and confidentiality.
                The following ciphertext is encrypted with a simple monoalphabetic substitution cipher (one letter maps to exactly one other letter).
                Please decrypt it into meaningful, correct English text.
                To do this:

                    Perform letter frequency analysis on the ciphertext and compare it to standard English letter frequencies.

                    Identify common short words like THE, AND, YOU, IS, ARE by analyzing repeated patterns.

                    Use these insights to build a substitution key and iteratively refine it for maximum coherence.

                    Avoid defaulting to common filler texts or pangrams.

                    Once decrypted, extract and output any numbers or flags included in the message.

                Provide ONLY the final decoded English message and any extracted number or flag — no explanations or filler.

                Example:
                Ciphertext: MEQXOEKTUSHOFJUTJXYIMXQJYIJXUIKCEVJXUQISYYLQBKUIEVJXUSXQHQSJUHIYDTYLQHMYJXBEMUHSQIUSXQHI
                Decrypted:  EVERYTHINGHAPPENSFORAREASONANDTHOSEWHOWAITAREEVENTUALLYREWARDEDWITHSUCCESSFLAG534
                Flag: 534

                Ciphertext:
                {ciphertext}"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.1
        )
        result = response.choices[0].message.content.strip()
        return self.find_number(result)

    
    def extract_url(self, text):
        match = re.search(r"\{\s*([^}]+?)\s*\}", text)
        result = match.group(0) if match else None
        return result[2:-2]
    
    def download_image(self, url):
        response = requests.get(url)
        return Image.open(BytesIO(response.content))
    
    def extract_text(self, image):
        return pytesseract.image_to_string(image).strip().replace("\n", "")
    
    def find_number(self, text):
        match = re.search(r"flag:\s*(\d+)", text, re.IGNORECASE)
        if match:
            number_after_flag = int(match.group(1))
        else:
            number_after_flag = None
        return number_after_flag

