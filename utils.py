# utils.py
import json
import os
from datetime import datetime

def load_metadata(filepath):
    """Loads metadata from a JSON file.

    Args:
        filepath: The path to the JSON file.

    Returns:
        A dictionary containing the metadata, or an empty dictionary if the file doesn't exist or there's an error.
    """
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return empty dict if file doesn't exist
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {filepath}. Returning empty dictionary.")
        return {} # Return empty dict if JSON is invalid
    except Exception as e: # Catch other potential errors
        print(f"Error loading metadata: {e}")
        return {}


def save_metadata(filepath, metadata):
    """Saves metadata to a JSON file.

    Args:
        filepath: The path to the JSON file.
        metadata: The metadata dictionary to save.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(metadata, f, indent=4)  # Use indent for pretty printing
    except Exception as e:
        print(f"Error saving metadata: {e}")


def load_text_item(filepath):
    """Loads the content of a text file.

    Args:
        filepath: The path to the text file.

    Returns:
        The content of the text file as a string, or None if there's an error.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:  # Handle encoding
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except Exception as e:
        print(f"Error loading text item: {e}")
        return None


def generate_metadata_from_files(text_files_dir):
    """Generates initial metadata from a folder of text files.

    Args:
        text_files_dir: The path to the directory containing the text files.

    Returns:
        A dictionary containing the initialized metadata.
    """
    metadata = {}
    try:
        for filename in os.listdir(text_files_dir):
            if filename.endswith(".txt"):  # Only process.txt files (or adjust as needed)
                filepath = os.path.join(text_files_dir, filename)
                if os.path.isfile(filepath): # Check if it's a file
                    metadata[filename] = {
                        "access_count": 0,
                        "last_rating": 2,  # Default rating of 2 (kind of know it)
                        "last_access_time": datetime.now().isoformat(),
                    }
    except FileNotFoundError:
        print(f"Directory not found: {text_files_dir}")
        return {}
    except Exception as e:
        print(f"Error generating metadata: {e}")
        return {}
    return metadata