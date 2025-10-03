"""
FastAPI Backend Server
This file handles all API endpoints for the chat application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sys
import os

# Add the parent directory to path so we can import from ai folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import AI logic
from ai.ai_logic import get_ai_response

# Create FastAPI app
app = FastAPI(title="Chat App API")

# Allow frontend to communicate with backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define what a message looks like
class Message(BaseModel):
    text: str


# Define what a response looks like
class Response(BaseModel):
    reply: str


@app.get("/")
def read_root():
    """
    Simple endpoint to check if the server is running.
    Visit http://localhost:8000 to see this message.
    """
    return {"message": "Chat API is running! 🚀"}


@app.get("/favicon.ico")
def favicon():
    """
    Serve the favicon from the frontend public folder.
    """
    favicon_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "frontend", "public", "favicon.ico"
    )
    return FileResponse(favicon_path)


@app.post("/chat", response_model=Response)
def chat(message: Message):
    """
    Main chat endpoint.
    Receives a message from the frontend and returns an AI response.
    
    Args:
        message: The user's message
        
    Returns:
        A response with the AI's reply
    """
    # Get AI response from the separate AI logic module
    ai_reply = get_ai_response(message.text)
    
    return Response(reply=ai_reply)


# Run the server
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting FastAPI server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
