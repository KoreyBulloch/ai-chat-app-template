# Backend (FastAPI)

This folder contains the API server that handles communication between the frontend and AI logic.

## Files

- **main.py**: The main server file with API endpoints
- **requirements.txt**: Python packages needed to run the server (includes FastAPI, Azure OpenAI, and AutoGen dependencies)

## API Endpoints

### GET /
- Check if the server is running
- Returns: `{"message": "Chat API is running! 🚀"}`

### POST /chat
- Send a message and get an AI response
- Request body: `{"text": "your message here"}`
- Returns: `{"reply": "AI response here"}`

## Running the Server

```bash
# Create a virtual environment (first time only)
python -m venv venv

# Activate the virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Windows Command Prompt:
# venv\Scripts\activate.bat
# On Mac/Linux:
# source venv/bin/activate

# Install dependencies - Use the full path to ensure we're using the venv's pip (most reliable)
.\venv\Scripts\pip.exe install -r requirements.txt

# Alternative: Use pip after activating venv
# pip install -r requirements.txt

# Start the server - Use the full path to ensure we're using the venv's python (most reliable)
.\venv\Scripts\python.exe main.py

# Alternative: After proper activation, you can use:
# python main.py

```

**Note:** Always activate the virtual environment before running the server! Using full paths (`.\venv\Scripts\pip.exe` and `.\venv\Scripts\python.exe`) ensures you're using the virtual environment's packages, avoiding conflicts with global Python installations.

**Prerequisites:** 
- Azure OpenAI resource with deployment configured
- `.env` file with Azure credentials, located in the ai folder (see main README for setup)

The server will run on `http://localhost:8000`

## For Junior Developers

- `main.py` is the only file you need to understand
- Each function has comments explaining what it does
- The `@app.post("/chat")` means "create an endpoint at /chat that accepts POST requests"
- We import the AI logic from a separate folder to keep things organized
