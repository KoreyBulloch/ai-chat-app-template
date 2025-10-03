# AI Logic

This folder contains all AI-related code, completely separate from the API.

## Files

- **ai_logic.py**: Contains the function that generates AI responses

## Configure Azure OpenAI credentials
- Create a .env file in the project root with your Azure OpenAI settings (See main README.md or .env.example for details)

## How It Works

The `get_ai_response()` function takes a user message and returns a response.

Currently, it uses **Azure OpenAI with AutoGen** framework, which provides:
- Connection to Azure OpenAI models (GPT-4, GPT-3.5-turbo, etc.)
- Agent-based conversation handling
- Support for both API key and Azure credential authentication

You can modify or replace this implementation with:
- Direct OpenAI API calls
- Anthropic Claude
- Local LLM models (like Llama)
- Any other AI service

## For Junior Developers

- This folder is independent - it doesn't know about FastAPI or React
- The function receives text and returns text
- To upgrade the AI, just modify the `get_ai_response()` function
- Keep all AI logic in this folder for easy organization

## Example Usage

```python
from ai.ai_logic import get_ai_response

response = get_ai_response("Hello!")
print(response)  # Output: An AI-generated response from Azure OpenAI
```
