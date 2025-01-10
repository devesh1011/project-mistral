# Project Mistral

<!-- ## Overview
Project Mistral is an AI-powered system designed to decompose complex queries into sub-queries, retrieve relevant documents, and generate precise answers using a large language model (LLM). -->

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/devesh1011/project-mistral.git
   cd project-mistral
   ```

2. Create a virtual environment and activate it:
    ```python3 -m venv .venv
    source .venv/bin/activate```

3. Install the required dependencies:

    ```pip install -r requirements.txt```

4. Set up environment variables: Create a .env file in the root directory and add the following variables:

    ```
    SNOWFLAKE_ACCOUNT="dnfrzvt-vgb56792"
    SNOWFLAKE_USER="devesh1010"
    SNOWFLAKE_USER_PASSWORD="Haunted97!"
    WAREHOUSE="COMPUTE_WH"
    MISTRAL_API_KEY="ZpDHXnr3eQk0nkVa3OZZPEnv65SCwf3o"
    ```

## Usage

1. Run the main script:

```python main.py```