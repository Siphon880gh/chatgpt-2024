from openai import OpenAI

from typing_extensions import override
from openai import AssistantEventHandler

import requests
from dotenv import load_dotenv
import os
# Specify the path to the .env file two directories up
dotenv_path = os.path.join(os.path.dirname(__file__), '.', '.env')

# Load the .env file from the specified path
load_dotenv(override=True, dotenv_path=dotenv_path)

secret_key = os.getenv('ELEVENLABS_API_KEY')
api_key = os.getenv('OPENAI_API_KEY')
org_id = os.getenv('OPENAI_ORG_ID')
proj_id = os.getenv('OPENAI_PROJ_ID')

# print("******************")
# print("api_key: " + api_key)
# print("org_id: " + org_id)
# print("proj_id: " + proj_id)


client = OpenAI(
  api_key=api_key, 
  organization=org_id,
  project=proj_id,
)

# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")


from openai import OpenAI
client = OpenAI()

# Assistant gpt-4-turbo with instructions: You can translate from English to the language of my choice
assistant = client.beta.assistants.retrieve("asst_YuQ0oeOMZiV09aOMsBNT7n0J")
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

# print(message)

class EventHandler(AssistantEventHandler):    
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)
 

with client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=assistant.id,
  event_handler=EventHandler(),
) as stream:
  stream.until_done()
