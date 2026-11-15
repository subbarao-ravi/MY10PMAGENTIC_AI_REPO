from dotenv import load_dotenv, find_dotenv
import os
from google import genai
from openai import OpenAI

#GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

load_dotenv(find_dotenv(), override=True)

#client = genai.Client(api_key=GOOGLE_API_KEY)

#for m in client.models.list():
    #print(m.name, "| input limit:", m.input_token_limit, "| output limit:", m.output_token_limit)