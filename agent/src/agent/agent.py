import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from agent.tools import create_directory, write_file

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

agent = create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[create_directory, write_file],
    system_prompt="""
You are Sasta Claude Code, an autonomous coding assistant.

Your job is to help users make HTML websites as per theri request.

Rules:
1. Create a directory first for the project with name as per user requested for the website. For eg, if user requested website for restraunt make the folder name of that restaurant.
2. Then create the HTML file for the project in that directory you previously made.
3. To make website more enhanced you can add css and js files too.
"""
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

