import requests
from openai import OpenAI
import re
from bs4 import BeautifulSoup

class DivarContest:
    def __init__(self, api_token):
        self.api_token = api_token
        self.model = "gpt-4.1-mini"
        self.client = OpenAI(api_key=self.api_token, base_url="https://api.metisai.ir/openai/v1")

    def web_search(self, url):
        resp = requests.get(url)
        resp.raise_for_status()
        html = resp.text

        soup = BeautifulSoup(html, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form", "noscript"]):
            tag.decompose()

        texts = soup.stripped_strings
        cleaned_text = "\n".join(texts)

        return cleaned_text

    def refine_question(self, question):
        prompt = f"""
                    You are an AI assistant specialized in clarifying vague or ambiguous questions.

                    Given this question, improve and clarify it without changing its meaning.
                    If it is already clear, just return it as is.

                    Question:
                    \"\"\"{question}\"\"\"

                    Now Only give me the refined question.
                    """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=150,
        )
        return response.choices[0].message.content.strip()

    def core_agent(self, question):
        refined = self.refine_question(question)

        urls = re.findall(r'https?://[^\s]+', refined)
        if urls:
            raw_data = self.web_search(urls[0])
            return refined, raw_data

        return refined, None

    def answer_agent(self, original_question, raw_data):
        prompt = f"""
                You are a knowledgeable assistant.

                Using the original question and the following information extracted from the web (if any),
                please provide a concise and precise answer to the question.

                Original question:
                \"\"\"{original_question}\"\"\"

                Information from web:
                \"\"\"{raw_data if raw_data else 'No external information provided.'}\"\"\"

                Please ONLY give me the final answer that my Original question wants, no more detail or explanation.
                """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()

    # The main function called for the question
    def capture_the_flag(self, question):
        refined_question, raw_data = self.core_agent(question)
        final_answer = self.answer_agent(refined_question, raw_data)
        return final_answer
