# agent/agent.py

from agent.rules import RULES
from agent.processor import clean_input, extract_information
from agent.memory import Memory


class ModelBasedAgent:

    def __init__(self):
        self.memory = Memory()

    def handle_memory_storage(self, cleaned_input: str):
        key, value = extract_information(cleaned_input)

        if key and value:
            self.memory.store(key, value)
            return f"Got it! I will remember your {key} is {value}"

        return None

    def handle_memory_query(self, cleaned_input: str):
        if "what is my name" in cleaned_input:
            if self.memory.has("name"):
                return f"Your name is {self.memory.retrieve('name')}"
            return "I don't know your name yet"

        if "where do i live" in cleaned_input:
            if self.memory.has("location"):
                return f"You live in {self.memory.retrieve('location')}"
            return "I don't know where you live yet"

        return None

    def handle_rules(self, cleaned_input: str):
        for key, response in RULES:
            if key in cleaned_input:
                return response
        return None

    def respond(self, user_input: str) -> str:
        cleaned = clean_input(user_input)

        # 1. Store new info
        result = self.handle_memory_storage(cleaned)
        if result:
            return result

        # 2. Answer memory questions
        result = self.handle_memory_query(cleaned)
        if result:
            return result

        # 3. Fallback rules
        result = self.handle_rules(cleaned)
        if result:
            return result

        return "I don't understand"