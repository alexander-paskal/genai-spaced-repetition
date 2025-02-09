# llm_interface.py
# Requires: google-generativeai

import os
import google.generativeai as genai

from dotenv import load_dotenv

# Set your Gemini API key (replace with your actual key)
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


def generate_text(prompt: str, model: str = "gemini-1.5-flash"): #model parameter added for future compatibility
    """
    Generates text using the Gemini API.

    Args:
        prompt: The prompt to send to the LLM.
        model: The model to use (defaults to Gemini).

    Returns:
        The generated text, or None if there was an error.
    """
    try:
        model = genai.GenerativeModel("models/" + model)
        result = model.generate_content(prompt)
        return result.text
    except Exception as e:
        print(f"Error generating text: {e}")
        return None


def evaluate_response(prompt, user_response, source_text, model: str = "gemini-1.5-flash"):
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
    Original Question: {prompt}

    User Response: {user_response}

    Source Text: {source_text}

    Evaluate the User Response on a scale of 1 to 3, where:
    1: The user doesn't know the answer.
    2: The user knows some aspects but misses details.
    3: The user has mastered the material.

    Provide only the numerical rating (1, 2, or 3) as your response.
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