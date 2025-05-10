import os
import openai
# from dotenv import load_dotenv, find_dotenv
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_type = os.environ.get("API_TYPE")
openai.api_key = os.environ.get("API_KEY")
openai.api_base = os.environ.get("API_BASE")
openai.api_version = os.environ.get("API_VERSION")

print("hello world")
