import os
from dotenv import load_dotenv

load_dotenv()


def get_snowflake_params():
    return {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_USER_PASSWORD"),
        "warehouse": os.getenv("WAREHOUSE"),
    }


def get_mistral_api_key():
    return os.getenv("MISTRAL_API_KEY")
