import os

from decouple import config

from ai_chatbot.assistant import LLMModel, LLMProvider


def prepare_environment() -> None:
    """
    Prepare the environment for the AI model.
    This function can be used to set up any necessary configurations or
    environment variables before using the AI model.
    """
    # TODO: Implement environment preparation logic depending on the model and provider.
    # Placeholder for environment preparation logic
    os.environ["OPENAI_API_KEY"] = config(  # type: ignore[assignment]
        "OPENAI_API_KEY",
    )  # type: ignore[assignment]
    os.environ["GROQ_API_KEY"] = config("GROQ_API_KEY")  # type: ignore[assignment]
    os.environ["LANGSMITH_API_KEY"] = config("LANGSMITH_API_KEY")  # type: ignore[assignment]
    os.environ["LANGCHAIN_TRACING_V2"] = config("LANGCHAIN_TRACING_V2")  # type: ignore[assignment]
    os.environ["LANGCHAIN_PROJECT"] = config("LANGCHAIN_PROJECT")  # type: ignore[assignment]


def return_provider_from_model(model: LLMModel) -> LLMProvider:
    """
    Returns the provider name based on the model name.

    Args:
        model (LLModel): The model name.

    Returns:
        LLMProvider: The provider name.
    """
    match model:
        case (
            LLMModel.GPT_4O_MINI
            | LLMModel.GPT_4_1
            | LLMModel.GPT_4_1_MINI
            | LLMModel.GPT_4_1_NANO
            | LLMModel.GPT_4O
            | LLMModel.GPT_O4_MINI
            | LLMModel.GPT_O1
            | LLMModel.GPT_O3_MINI
        ):
            return LLMProvider.OPENAI
        case (
            LLMModel.CLAUDE_SONNET_LATEST
            | LLMModel.CLAUDE_OPUS_LATEST
            | LLMModel.CLAUDE_HAIKU_LATEST
        ):
            return LLMProvider.ANTHROPIC
        case (
            LLMModel.LLAMA_3_INSTANT
            | LLMModel.LLAMA_3_VERSATILE
            | LLMModel.GEMMA_9B_IT
            | LLMModel.DEEPSEEK
            | LLMModel.MISTRAL
        ):
            return LLMProvider.GROQ
        case LLMModel.GEMINI_20_FLASH:
            return LLMProvider.GOOGLE_GENAI
        case LLMModel.GEMINI_20_FLASH_001:
            return LLMProvider.GOOGLE_VERTEX
        case LLMModel.COMMAND_R_PLUS:
            return LLMProvider.COHERE
        case _:
            raise ValueError(f"Unsupported model: {model}")
