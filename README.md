# Spaced Repetition CLI

This is a simple command-line interface (CLI) application for spaced repetition learning. It uses Large Language Models (LLMs) to generate questions and evaluate answers, helping you learn and retain information more effectively.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://your-repo-url.git](https://your-repo-url.git)  # Replace with your repository URL
    cd spaced_repetition
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv.venv
    source.venv/bin/activate  # On Windows:.venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (Or, if you used `setup.py` and built a distribution:)
    ```bash
    pip install dist/spaced_repetition-0.1.0-py3-none-any.whl # Replace with actual filename
    ```

4.  **Set up your LLM API key:**

    Set the `GEMINI_API_KEY` environment variable with your Gemini API key in a .env file in the root directory.  **Do not** hardcode your API key in the code.

## Usage

1.  **Run the application:**

    ```bash
    spaced_repetition --data_dir my_data_folder
    ```
    (Replace `my_data_folder` with your data directory path. If you don't specify `--data_dir`, it defaults to `data`.)

2.  **Answer questions:** The application will present questions. Type your answer and press Enter.

3.  **Exit:** Type `exit` and press Enter to quit the application.

## Data Directory Structure

The data directory should have the following structure:

    ```
    my_data_folder/  # Or your chosen data directory
    ├── metadata.json  # Metadata file (created by --init)
    └── text_files/    # Contains the text files (learning items)
    ├───── item1.txt  # Example learning item
    ├───── item2.txt  # Another learning item
    └─────...