from agent.agent import ModelBasedAgent

agent = ModelBasedAgent()

print("Agent: Hello! You can tell me things about yourself.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    response = agent.respond(user_input)
    print("Agent:", response)