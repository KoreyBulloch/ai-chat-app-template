# AI Chat App Template

A simple chat application with clear separation between frontend, backend, and AI logic.


## 📁 Project Structure

```
ai-chat-app-template/
├── frontend/          # React application (UI)
├── backend/           # FastAPI server (API)
├── ai/                # AI logic (separate from API)
└── README.md
```


## ⚡ Quickstart (After First Time Setup)

Once you've completed the first-time setup below, choose one of the following options to run the application:


### Option 1: Automated Start (Recommended)

Run the PowerShell script that starts both servers automatically:

```powershell
.\start-app.ps1
```

This will:
- Open two separate PowerShell windows (one for backend, one for frontend)
- Backend will be available at `http://localhost:8000`
- Frontend will be available at `http://localhost:3000`

To stop the servers, close the PowerShell windows or press `Ctrl+C` in each window.


### Option 2: Manual Start

If you prefer to start each component manually:

**1. Start the Backend Server**

```powershell
cd backend
.\venv\Scripts\Activate.ps1
# Use the full path to ensure we're using the venv's python
.\venv\Scripts\python.exe main.py

# Alternative: After proper activation, you can use:
# python main.py
```

The API will run on `http://localhost:8000`

**2. Start the Frontend (in a new terminal)**

```powershell
cd frontend
npm start
```

The app will open at `http://localhost:3000`


---


## 🚀 First Time Setup

### Prerequisites

- Python 3.8+ installed
- Node.js installed (for frontend)
- Azure OpenAI resource and credentials (see Azure Portal)


### Backend Setup

1. Navigate to the backend folder:
```bash
cd backend
```

2. Create a virtual environment if you haven't already (recommended):
```bash
python -m venv venv
```

3. **Windows PowerShell Users**: If you get an error about script execution being disabled, run this one-time setup:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
*Note: This is only needed if PowerShell blocks the activation script. Many systems already have this configured.*

4. Activate the virtual environment:
```bash
# On Windows PowerShell
.\venv\Scripts\Activate.ps1

# On Windows Command Prompt
venv\Scripts\activate.bat

# On Mac/Linux
source venv/bin/activate
```
*Note: You need to activate the venv every time you open a new terminal window.*

5. Install Python dependencies if you haven't already:
```bash
# Use the full path to ensure we're using the venv's pip (most reliable)
.\venv\Scripts\pip.exe install -r requirements.txt

# Alternative: Use pip after activating venv
# pip install -r requirements.txt
```
*Note: Using the full path `.\.\venv\Scripts\pip.exe` ensures you're installing packages into the virtual environment, avoiding conflicts with global Python installations.*

6. Create a `.env` file in the project root for your Azure AI credentials if you haven't already (copy from `.env.example` and fill in values as indicated).

7. Start the FastAPI server:
```bash
# Use the full path to ensure we're using the venv's python (most reliable)
.\venv\Scripts\python.exe main.py

# Alternative: After proper activation, you can use:
# python main.py
```

The API will run on `http://localhost:8000`


### Frontend Setup

**Prerequisites:** Install Node.js from [nodejs.org](https://nodejs.org/) (download the LTS version). After installation, verify by running `node --version` and `npm --version` in a new terminal.

1. Navigate to the frontend folder:
```bash
cd frontend
```

2. Install dependencies if you haven't already:
```bash
npm install
```

3. Start the React app:
```bash
npm start
```

The app will open at `http://localhost:3000`


## 🎯 How It Works

1. **Frontend (React)**: User interface for sending/receiving messages
2. **Backend (FastAPI)**: API server that handles requests
3. **AI Logic**: Separate module that processes messages and generates responses


## 📝 For Junior Developers

- Each folder is independent and focused on one responsibility
- Start with `frontend/src/App.js` to see the UI
- Check `backend/main.py` to see how API endpoints work
- Look at `ai/ai_logic.py` to understand AI responses


## 🤖 How This Project Was Created

This template provides a starting point for building agentic AI solutions.  It was created using:

**GitHub Copilot** and **Claude Sonnet 4.5**

### Initial Prompt

```
You are an expert full stack developer who specializes in making simple, aesthetically pleasing, modern applications using React, Python, and Fast API that can be updated, understood, and maintained by junior devs.

Create a very basic chat app that uses React for the frontend, Python for the AI logic, and Fast API for the backend.

Rules to follow:
=> App must be very minimalistic.  Functionality can be added later if need be.
=> It is very important that junior devs with little coding experience are able to navigate the project and manage updates.
=> React to be used for the frontend.
=> Python to be used for teh AI logic.
=> FastAPI to be used for the API.
=> Frontend, AI logic, and backend/API are all separate.
``` 