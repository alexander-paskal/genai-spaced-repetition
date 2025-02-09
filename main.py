# main.py
import argparse
import os
import time
from datetime import datetime

from proctor import select_test_item, generate_question
from critic import evaluate_response, qualitative_feedback
from utils import load_metadata, save_metadata, load_text_item, generate_metadata_from_files


def main():
    parser = argparse.ArgumentParser(description="Spaced Repetition CLI")
    parser.add_argument(
        "--data",
        type=str,
        default="data",  # Default data directory
        help="Path to the data directory",
    )

    args = parser.parse_args()

    DATA_DIR = args.data
    METADATA_FILE = os.path.join(DATA_DIR, "metadata.json")
    TEXT_FILES_DIR = os.path.join(DATA_DIR, "text_files")

    if not os.path.exists(METADATA_FILE):
        metadata = generate_metadata_from_files(TEXT_FILES_DIR)
        save_metadata(METADATA_FILE, metadata)
        print(f"Metadata initialized and saved to {METADATA_FILE}")
    else:
        metadata = load_metadata(METADATA_FILE)

    while True:
        test_item_filename = select_test_item(metadata)
        if test_item_filename is None:
            print("No more items to review. Exiting.")
            break

        source_text = load_text_item(os.path.join(TEXT_FILES_DIR, test_item_filename))
        question = generate_question(source_text)

        print(f"\nQuestion: {question}")
        user_response = input("Your answer (or type 'exit'): ")

        if user_response.lower() == "exit":
            break
        
        rating = evaluate_response(question, user_response, source_text)
        time.sleep(1)
        feedback = qualitative_feedback(question, user_response, source_text, rating)
        

        if rating is not None:
            print(f"Rating: {rating}")
            print(feedback)

            if rating < 3:
                print(f"source text: {source_text}")

            metadata[test_item_filename]["access_count"] = metadata.get(test_item_filename, {}).get("access_count", 0) + 1
            metadata[test_item_filename]["last_rating"] = rating
            metadata[test_item_filename]["last_access_time"] = datetime.now().isoformat()
            save_metadata(METADATA_FILE, metadata)
        else:
            print("Could not evaluate the response.")
        
        time.sleep(1)


if __name__ == "__main__":
    main()