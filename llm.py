from snowflake.snowpark import Session
from snowflake.cortex import Complete
import os
from dotenv import load_dotenv

load_dotenv()

params = {
    "account": os.environ.get("SNOWFLAKE_ACCOUNT"),
    "user": os.environ.get("SNOWFLAKE_USER"),
    "password": os.environ.get("SNOWFLAKE_USER_PASSWORD"),
    "warehouse": os.environ.get("WAREHOUSE"),
}

sp_session = Session.builder.configs(params).create()

prompt = [{"role": "user", "content": "How do snowflakes get their unique patterns?"}]

options = {"temperature": 0.1, "max_tokens": 150}

response = Complete("mistral-large", prompt, options=options)
print(response)
