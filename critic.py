from llm import generate_text


def evaluate_response(question: str, user_response: str, source_text: str, model="gemini-1.5-flash") -> int:
    """
    Evaluates the user's response using the Gemini API.

    Args:
        prompt: The original question prompt.
        user_response: The user's response.
        source_text: The source text.
        model: The model to use (defaults to Gemini).

    Returns:
        A rating (1-3) or None if there was an error.
    """

    evaluation_prompt = f"""
    Original Question: {question}

    User Response: {user_response}

    Source Text: {source_text}

    Evaluate the User Response on a scale of 1 to 3, where:
    1: The user doesn't know the answer.
    2: The user knows some aspects but misses details.
    3: The user has mastered the material.

    Provide ONLY the numerical rating (1, 2, or 3) as your response. Do NOT include any punctuation or any other characters of any kind. 
    """

    try:
        rating_str = generate_text(evaluation_prompt, model=model)
        if rating_str is not None:
            rating = int(rating_str.strip())  #added strip and int conversion
            if 1 <= rating <= 3: # added input validation
                return rating
            else:
                print("Invalid rating received from LLM.")
                return None
        else:
            return None #added error handling
    except ValueError:
        print("Invalid rating received from LLM (non-numerical).")
        return None
    except Exception as e:
        print(f"Error evaluating response: {e}")
        return None


def qualitative_feedback(question: str, user_response: str, source_text: str, rating: int, model="gemini-1.5-flash") -> int:
    """
    Evaluates the user's response using the Gemini API.

    Args:
        prompt: The original question prompt.
        user_response: The user's response.
        source_text: The source text.
        model: The model to use (defaults to Gemini).

    Returns:
        A rating (1-3) or None if there was an error.
    """

    feedback = f"""
    Original Question: {question}

    User Response: {user_response}

    Source Text: {source_text}

    The user has been evaluated on a scale of 1-3, where:
    1: The user doesn't know the answer.
    2: The user knows some aspects but misses details.
    3: The user has mastered the material.

    The User has received the following reading: {rating}

    Provide qualitative feedback on the users response. Don't be unncessarily polite. Keep
    your response as concise as possible. If the user doesn't know, don't beat them up for it.
    If they ask for additional information outside the scope of the question, INCLUDE THE ANSWER TO THEIR FOLLOWUP QUESTION IN YOUR RESPONSE.

    """

    try:
        feedback = generate_text(feedback, model=model)
        return feedback
    except Exception as e:
        print(f"Error evaluating response: {e}")
        return None
