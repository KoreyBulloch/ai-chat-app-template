# Start script for AI Chat App
# This script starts both the backend and frontend servers

Write-Host "Starting AI Chat App..." -ForegroundColor Green
Write-Host ""

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Function to check if a command exists
function Test-Command {
    param($command)
    $null -ne (Get-Command $command -ErrorAction SilentlyContinue)
}

# Check if Python is installed
if (-not (Test-Command python)) {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Check if Node.js is installed
if (-not (Test-Command node)) {
    Write-Host "Error: Node.js is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Check if backend virtual environment exists
$venvPath = Join-Path $scriptDir "backend\venv\Scripts\Activate.ps1"
if (-not (Test-Path $venvPath)) {
    Write-Host "Warning: Backend virtual environment not found at backend\venv" -ForegroundColor Yellow
    Write-Host "Please run the first-time setup. See README.md for instructions." -ForegroundColor Yellow
    exit 1
}

# Check if frontend node_modules exists
$nodeModulesPath = Join-Path $scriptDir "frontend\node_modules"
if (-not (Test-Path $nodeModulesPath)) {
    Write-Host "Warning: Frontend dependencies not installed" -ForegroundColor Yellow
    Write-Host "Installing frontend dependencies..." -ForegroundColor Cyan
    Push-Location (Join-Path $scriptDir "frontend")
    npm install
    Pop-Location
}

# Start backend in a new PowerShell window
Write-Host "Starting backend server..." -ForegroundColor Cyan
$backendPath = Join-Path $scriptDir "backend"
$backendScript = @"
cd '$backendPath'
& '.\venv\Scripts\Activate.ps1'
Write-Host 'Backend server starting on http://localhost:8000' -ForegroundColor Green
python main.py
"@

Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendScript

# Wait a moment for backend to start
Write-Host "Waiting for backend to initialize..." -ForegroundColor Cyan
Start-Sleep -Seconds 3

# Start frontend in a new PowerShell window
Write-Host "Starting frontend server..." -ForegroundColor Cyan
$frontendPath = Join-Path $scriptDir "frontend"
$frontendScript = @"
cd '$frontendPath'
Write-Host 'Frontend server starting on http://localhost:3000' -ForegroundColor Green
npm start
"@

Start-Process powershell -ArgumentList "-NoExit", "-Command", $frontendScript

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "AI Chat App is starting!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Backend API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Frontend:    http://localhost:3000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Both servers are running in separate windows." -ForegroundColor Yellow
Write-Host "Close those windows or press Ctrl+C in them to stop the servers." -ForegroundColor Yellow
Write-Host ""
