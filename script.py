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

# Read more:
# https://platform.openai.com/docs/assistants/overview?context=with-streaming
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
