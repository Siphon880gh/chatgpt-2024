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
assist_id = os.getenv('OPENAI_ASSISTANT_TRANSLATOR')

print("**************************")
print("Test .env")
print("**************************")
print("api_key: " + api_key)
print("org_id: " + org_id)
print("proj_id: " + proj_id)
print("proj_id: " + proj_id)

# Create an OpenAI client
client = OpenAI(
  api_key=api_key, 
  organization=org_id,
  project=proj_id,
)


# Assistant gpt-4-turbo with instructions: You can translate from English to the language of my choice
# Create assistant at https://platform.openai.com/assistants/
assistant = client.beta.assistants.retrieve(assist_id)
# print(my_assistant)

thread = client.beta.threads.create()

def translateTo(language, text): 
    return f"Please translate this to {language}:\n\n{text}!"

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content=translateTo("French", "Hello, how are you?"), 
)
print(message)
