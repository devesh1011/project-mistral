from snowflake.snowpark import Session
from snowflake.cortex import Complete
from config import get_snowflake_params

params = get_snowflake_params()

sp_session = Session.builder.configs(params).create()


def generate_answer(prompt):
    # snowflake cortex llm-function
    return Complete("mistral-large2", prompt, session=sp_session)


print(generate_answer("how do snowflakes get their unique patterns?"))
