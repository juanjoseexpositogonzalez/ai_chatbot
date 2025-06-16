import os

from decouple import config
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def environment_setup():
    """Prepares the environment"""

    os.environ["LANGCHAIN_TRACING_V2"] = config("LANGCHAIN_TRACING_V2")
    os.environ["LANGCHAIN_API_KEY"] = config("LANGSMITH_API_KEY")
    os.environ["GROQ_API_KEY"] = config("GROQ_API_KEY")
    os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")


def generate_response(user_message: str) -> str:
    """Generates a response from the AI model using Groq"""

    prompt = """
    Respond to the user's message with Shelock's style, using humor and wit.

    User: {user_message}

    """

    environment_setup()

    # Define the prompt template
    chat_prompt = ChatPromptTemplate.from_template(prompt)

    # Initialize the Groq model
    groq_model = ChatGroq(model=config("LLAMA_MODEL"))

    output_parser = StrOutputParser()

    # chain
    response_chain = chat_prompt | groq_model | output_parser
    # Generate the response
    response = response_chain.invoke({"user_message": user_message})
    return response
