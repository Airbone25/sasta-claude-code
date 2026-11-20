import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from agent.tools import create_directory, write_file, read_file, list_files, edit_file
from agent.prompt import systemPrompt

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

agent = create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[create_directory, write_file, read_file, list_files, edit_file],
    system_prompt=systemPrompt()
)

messages = []

def ask_agent(messages: list[object]) -> str:
    response = agent.invoke({
        "messages": messages
    })

    messages.append({
        "role": "assistant",
        "content": response["messages"][-1].content[0]["text"]
    })

    return response["messages"][-1].content[0]["text"]

print("----- SASTA CLAUDE CODE -----")
while True:
    query = input("Ask-> ")
    messages.append({
        "role" : "user",
        "content": query
    })
    response = ask_agent(messages)
    print(f"Bot: {response}")

