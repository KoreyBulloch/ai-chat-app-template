"""
AI Chat Logic
This file contains all the AI logic for generating responses.
Keep all AI-related code here, separate from the API.
"""

# Import necessary libraries
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Import if using Azure Identity for authentication
from azure.ai.inference import ChatCompletionsClient
from azure.identity import DefaultAzureCredential


# Load environment variables from .env file in the ai folder
# Get the directory where this file is located
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')
load_dotenv(env_path)


# Get configuration from environment variables
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
model_name = os.getenv("AZURE_OPENAI_MODEL_NAME", deployment_name)  # Use deployment name if model name not specified
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
api_key = os.getenv("AZURE_OPENAI_API_KEY")  # If using your Azure OpenAI API key
use_azure_credentials = os.getenv("USE_AZURE_CREDENTIALS", "false").lower() == "true"  # If using Azure Identity


# Initialize the model client and agent globally
# This will be reused across multiple chat requests
if use_azure_credentials:
    # Option A (preferred): Use Azure credentials with DefaultAzureCredential
    model_client = AzureOpenAIChatCompletionClient(
        model=model_name,  # The underlying OpenAI model name
        api_version=api_version,  # API version
        azure_endpoint=endpoint,  # Your Azure endpoint
        azure_ad_token_provider=lambda: DefaultAzureCredential().get_token("https://cognitiveservices.azure.com/.default").token,  # Function to get Azure AD token
        azure_deployment=deployment_name,  # Your Azure deployment name
    )
else:
    # Option B: Use API key authentication
    model_client = AzureOpenAIChatCompletionClient(
        model=model_name,  # The underlying OpenAI model name
        api_version=api_version,  # API version
        azure_endpoint=endpoint,  # Your Azure endpoint
        api_key=api_key,  # Your Azure OpenAI API key
        azure_deployment=deployment_name,  # Your Azure deployment name
    )


# Create the assistant agent with a system message
agent = AssistantAgent(
    name="assistant",
    model_client=model_client,
    system_message="You are a helpful AI assistant. Provide clear and concise responses to user questions.",
)


# Import response handler functions
from .response_handler import get_ai_response_async, get_ai_response as get_ai_response_sync


# Wrapper functions to maintain backward compatibility
async def get_ai_response_async_wrapper(user_message: str) -> str:
    """Wrapper to call response handler with the agent."""
    return await get_ai_response_async(agent, user_message)


def get_ai_response(user_message: str) -> str:
    """Wrapper to call response handler with the agent."""
    return get_ai_response_sync(agent, user_message)

