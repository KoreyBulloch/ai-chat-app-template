# Frontend (React)

This folder contains the user interface for the chat application.

## Files

- **src/App.js**: Main component with all the chat logic
- **src/App.css**: Styles for the chat interface
- **src/index.js**: Entry point that renders the app
- **src/index.css**: Global styles
- **public/index.html**: HTML template
- **package.json**: Lists all npm packages needed

## How It Works

1. User types a message and clicks "Send"
2. Message is sent to the backend API at `http://localhost:8000/chat`
3. Backend returns an AI response
4. Response is displayed in the chat

## For Junior Developers

### Understanding App.js

- `useState`: Stores data (messages, input text, loading state)
- `sendMessage()`: Function that sends message to backend
- `messages.map()`: Loops through all messages and displays them
- CSS classes like `.user-message` and `.ai-message` style the messages differently

### Making Changes

- Want to change colors? Edit `App.css`
- Want to change how messages are sent? Edit the `sendMessage()` function
- Want to add new features? Start by adding to the `App.js` component

### Common Tasks

**Change the color scheme:**
Edit the gradient in `App.css` - look for `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

**Add a new button:**
Add it in the JSX part of `App.js` (inside the `return` statement)

**Display message timestamps:**
Add a timestamp to each message object and display it in the message bubble

## Security Notes

NPM overrides have been added to `package.json` to address security vulnerabilities in transitive dependencies (nth-check, postcss, webpack-dev-server). These overrides force newer, secure versions of these packages without breaking the React build setup.
