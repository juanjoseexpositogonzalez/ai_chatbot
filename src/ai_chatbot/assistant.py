import logging
from enum import StrEnum
from typing import Any, Callable, Dict, List, Optional

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough


class LLMProvider(StrEnum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    COHERE = "cohere"
    GROQ = "groq"
    GOOGLE_GENAI = "google_genai"
    GOOGLE_VERTEX = "google_vertexai"


class LLMModel(StrEnum):
    GPT_4_1 = "gpt-4.1"
    GPT_4_1_MINI = "gpt-4.1-mini"
    GPT_4_1_NANO = "gpt-4.1-nano"
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_O4_MINI = "o4-mini"
    GPT_O1 = "o1"
    GPT_O3_MINI = "o3-mini"
    CLAUDE_SONNET_LATEST = "claude-3-5-sonnet-latest"
    CLAUDE_OPUS_LATEST = "claude-3-opus-latest"
    CLAUDE_HAIKU_LATEST = "claude-3-haiku-latest"
    LLAMA_3_INSTANT = "llama-3.1-8b-instant"
    LLAMA_3_VERSATILE = "llama-3.3-70b-versatile"
    GEMINI_20_FLASH = "gemini-2.0-flash"
    GEMINI_20_FLASH_001 = "gemini-2.0-flash-001"
    COMMAND_R_PLUS = "command-r-plus"
    GEMMA_9B_IT = "gemma2-9b-it"
    DEEPSEEK = "deepseek-r1-distill-llama-70b"
    MISTRAL = "mistral-saba-24b"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class Assistant:
    def __init__(
        self,
        system_prompt: str,
        llm_model: LLMModel,
        temperature: float,
        max_tokens: int | None,
        llm_provider: Callable[[LLMModel], LLMProvider],
        message_history: List[Dict[str, str]],
        tools: Optional[List[Any]],
    ):
        """
        Initialize the Assistant with the given parameters.
        Args:
            system_prompt (str): The system prompt to set the context for the AI.
            llm_model (LLMModel): The model to use for the AI.
            temperature (float): The temperature for the LLM response generation.
            max_tokens (int): The maximum number of tokens to generate in the response.
            llm_provider (Callable[[LLMModel], LLMProvider]): A function to get the LLM provider based on the model.
            message_history (List[Dict[str, str]]): The history of messages in the conversation.
            tools (Optional[List[Any]]): Optional tools that the assistant can use.
        """
        self.system_prompt = system_prompt
        self.llm_model = llm_model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.llm_provider = llm_provider(llm_model)
        self.messages = message_history
        self.tools = tools

        self.llm = self._initialize_llm()
        self.chain = self._get_conversation_chain()

    def get_response(self, user_input: str) -> str:
        """
        Generate a response based on the user input and the message history.

        Args:
            user_input (str): The user's input message.

        Returns:
            str: The generated response from the AI model.
        """

        return self.chain.invoke(user_input)

    def _initialize_llm(self) -> Any:
        """
        Initialize the LLM based on the specified provider.
        Returns:
            Any: The initialized LLM instance.
        """

        llm = init_chat_model(
            model=self.llm_model.value,
            model_provider=self.llm_provider.value,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return llm

    def _get_conversation_chain(self) -> Any:
        """
        Get the conversation chain based on the LLM provider.

        Returns:
            Any: The conversation chain instance.
        """
        prompt: ChatPromptTemplate = ChatPromptTemplate(
            [
                ("system", self.system_prompt),
                MessagesPlaceholder("conversation_history"),
                ("human", "{user_input}"),
            ]
        )

        llm = self.llm

        output_parser = StrOutputParser()

        chain = (
            # First, we define a runnable parallel to handle the tools
            {
                "tools": lambda x: self.tools,
                "user_input": RunnablePassthrough(),
                "conversation_history": lambda x: self.messages,
            }
            | prompt
            | llm
            | output_parser
        )

        return chain
