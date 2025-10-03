"""
Response Handler
This module contains the functions for getting AI responses from the agent.
"""

import asyncio


# Async function to get AI response
async def get_ai_response_async(agent, user_message: str) -> str:
    """
    Async version: Generate an AI response using AutoGen agent.
    
    Args:
        agent: The AssistantAgent instance
        user_message: The message from the user
        
    Returns:
        A response string from the AI agent
    """
    try:
        # Run the agent with the user's message
        result = await agent.run(task=user_message)
        
        # Extract the last message content from the agent's response
        if result.messages:
            # Get the last message from the agent
            last_message = result.messages[-1]
            if hasattr(last_message, 'content'):
                return str(last_message.content)
            else:
                return str(last_message)
        
        return "I apologize, but I couldn't generate a response."
        
    except Exception as e:
        print(f"Error in AutoGen agent: {e}")
        return f"I encountered an error: {str(e)}"


# Synchronous wrapper for FastAPI compatibility
def get_ai_response(agent, user_message: str) -> str:
    """
    Generate an AI response based on the user's message using AutoGen.
    
    This function wraps the async AutoGen agent in a synchronous interface
    for compatibility with FastAPI.
    
    Args:
        agent: The AssistantAgent instance
        user_message: The message from the user
        
    Returns:
        A response string from the AI
    """
    
    # Run the async function in the event loop
    # Check if there's already a running event loop
    try:
        loop = asyncio.get_running_loop()
        # If we're in an async context, create a new task
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor() as pool:
            future = pool.submit(asyncio.run, get_ai_response_async(agent, user_message))
            return future.result()
    except RuntimeError:
        # No running loop, we can use asyncio.run directly
        return asyncio.run(get_ai_response_async(agent, user_message))
