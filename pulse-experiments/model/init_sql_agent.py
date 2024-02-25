


import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
from langchain.utilities import SQLDatabase
from dotenv import load_dotenv, find_dotenv
import openai
import os
from langchain.agents import create_sql_agent,AgentType
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit


_ = load_dotenv(find_dotenv())
key = os.getenv("OPENAI_API_KEY")
openai.api_key = ""

def sql_agent(db=None,
              llm="gpt-4",
              prompt="",
              suffix=""):
    """
    Initialize the SQL agent
    """
    db = SQLDatabase.from_uri(f'postgresql+psycopg2://<user>@<host>:<port>/<db>')
    llm2 = ChatOpenAI(temperature=0,
                      model=llm,
                      openai_api_key=openai.api_key)
    toolkit = SQLDatabaseToolkit(db=db,
                                 llm=llm2)
    agent_executor = create_sql_agent(
        llm=llm2,
        toolkit=toolkit,
        verbose=True,
        handle_parsing_errors=True,
        prefix=prompt,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        suffix=suffix,
        agent_executor_kwargs={"return_intermediate_steps": True}
    )

    return agent_executor