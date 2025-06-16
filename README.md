# ai-chatbot

A simple AI-powered chatbot web application built with [Streamlit](https://streamlit.io/). The chatbot uses Groq's Llama model via LangChain for generating witty, Sherlock Holmes-style responses.

## Features

- Interactive chat interface in the browser
- AI responds in the style of Sherlock Holmes, with humor and wit
- Easily configurable via environment variables

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)
- API keys for Groq, OpenAI, and LangSmith

### Installation

1. Clone the repository:

   ```sh
   git clone <your-repo-url>
   cd ai_chatbot
    ```

2. Install dependencies using `uv`:

   ```sh
   uv install
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with the following content:

   ```env
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key
   LANGSMITH_API_KEY=your_langsmith_api_key
   ```

4. Run the application:

   ```sh
   streamlit run app.py
   ```

### Usage
Open your web browser and navigate to `http://localhost:8501` to interact with the chatbot. Type your messages in the input box and hit Enter to receive witty responses.

## Configuration
You can customize the chatbot's behavior by modifying the `main.py` file. The model used is Groq's Llama, and you can adjust parameters like temperature and max tokens to change the response style. In addition, you can set the `LANGCHAIN_TRACING_V2` environment variable to enable or disable LangChain tracing.
## Environment Variables
- `GROQ_API_KEY`: Your Groq API key for accessing the Llama model.
- `OPENAI_API_KEY`: Your OpenAI API key for additional functionalities.
- `LANGSMITH_API_KEY`: Your LangSmith API key for tracing and monitoring.
- `LANGCHAIN_TRACING_V2`: Set to `true` to enable LangChain tracing, or `false` to disable it.
- `LANGCHAIN_ENDPOINT`: The endpoint for LangChain, if applicable.
- `LANGCHAIN_PROJECT`: The project name for LangChain, if applicable.
- `QWEN_MODEL`: The model name for Qwen, if applicable.
- `DEEPSEEK_MODEL`: The model name for DeepSeek, if applicable.
- `LLAMA_MODEL`: The model name for Llama, if applicable.

Feel free to adjust these variables to suit your needs, or add more models if you wish to expand the chatbot's capabilities. In addition, the role can be customized by modifying the `role` variable in the `main.py` file to change how the chatbot interacts with users.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
