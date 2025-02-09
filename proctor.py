from llm import generate_text
import random



def select_test_item(metadata: dict) -> str:  
    """
    Selects a test item based on access count and last rating.

    Args:
        metadata: The metadata dictionary.

    Returns:
        The filename of the selected test item, or None if no items are available.
    """
    if not metadata:
        return None

    weights = [4 - data["last_rating"] for data in metadata.values()]
    files = list(metadata.keys())

    selected_item = random.choices(files, weights)
    return selected_item[0]


def generate_question(source_text: str, model="gemini-1.5-flash") -> int:
    """
    Generates a question based on the text contained

    Args:
        source_text: The source text.
        model: The model to use (defaults to Gemini).

    Returns:
        A rating (1-3) or None if there was an error.
    """

    prompt = f"""

    Source Text: {source_text}

    Ask a question about the above text. It can be a single- or multi-part question, but should emphasize both knowledge of specific details and a command of 
    any involved processes. Keep questions concise. The answer to the question MUST be contained within the source text. It should NOT reference the source text directly.

    Good Examples:

        Who invented the theory of relativity?
        What is the highest mountain in the world?

    Bad Examples:

        According to the text, who invented the theory of relativity?

    """

    try:
        question = generate_text(prompt, model=model)
        if question is not None:
            return question
        else:
            return None #added error handling
    except Exception as e:
        print(f"Error evaluating response: {e}")
        return None