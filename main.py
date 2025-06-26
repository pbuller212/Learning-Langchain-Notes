import os
from dotenv import load_dotenv
from langchain_openai.llms import OpenAI

load_dotenv()
model = OpenAI(model="text-davinci-003", temperature=0, api_key=os.getenv('OPENAI_API_KEY'))

def main():
    print("Hello from learning-langchain-notes!")
    model.invoke("The sky is")

if __name__ == "__main__":
    main()
