from openai import OpenAI, AssistantEventHandler
from typing_extensions import override

from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '.', '.env')
load_dotenv(override=True, dotenv_path=dotenv_path)

secret_key = os.getenv('ELEVENLABS_API_KEY')
api_key = os.getenv('OPENAI_API_KEY')
org_id = os.getenv('OPENAI_ORG_ID')
proj_id = os.getenv('OPENAI_PROJ_ID')

print("**************************")
print("Test .env")
print("**************************")
print("api_key: " + api_key)
print("org_id: " + org_id)
print("proj_id: " + proj_id)

# Create an OpenAI client
client = OpenAI(
  api_key=api_key, 
  organization=org_id,
  project=proj_id,
)
