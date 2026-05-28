import anthropic

from dotenv import load_dotenv

load_dotenv()

def main():
    messages = []
    add_user_messages(messages, "What is the capital of France?")
    answer = chat(messages)
    add_assistant_messages(messages, answer)
    add_user_messages(messages, "What is the population of Paris?")
    answer = chat(messages)
    add_assistant_messages(messages, answer)
    print(messages)

def add_user_messages(messages, message):
    messages.append({"role": "user", "content": message})

def add_assistant_messages(messages, message):
    messages.append({"role": "assistant", "content": message})
    
def chat(messages):
    client = anthropic.Anthropic()
    model = "claude-opus-4-6"
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=messages
    )
    return response.content[0].text

if __name__ == "__main__":
    main()
