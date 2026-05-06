# agent/processor.py

def clean_input(user_input: str) -> str:
    return user_input.lower().strip()


def extract_information(user_input: str):
    """
    Extract known patterns from input
    Returns (key, value)
    """

    if "my name is" in user_input:
        value = user_input.split("my name is")[-1].strip()
        return ("name", value)

    if "i live in" in user_input:
        value = user_input.split("i live in")[-1].strip()
        return ("location", value)

    return (None, None)