/**
 * Main App Component
 * This is the main component that contains the entire chat interface.
 */

import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import './App.css';

function App() {
  // State to store all chat messages
  const [messages, setMessages] = useState([]);
  
  // State to store the current input text
  const [inputText, setInputText] = useState('');
  
  // State to track if we're waiting for AI response
  const [isLoading, setIsLoading] = useState(false);

  /**
   * Send a message to the backend and get AI response
   */
  const sendMessage = async () => {
    // Don't send empty messages
    if (!inputText.trim()) return;

    // Add user message to chat
    const userMessage = { text: inputText, sender: 'user' };
    setMessages(prevMessages => [...prevMessages, userMessage]);
    
    // Clear input field
    setInputText('');
    
    // Show loading state
    setIsLoading(true);

    try {
      // Call the backend API
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
      });

      const data = await response.json();
      
      // Add AI response to chat
      const aiMessage = { text: data.reply, sender: 'ai' };
      setMessages(prevMessages => [...prevMessages, aiMessage]);
      
    } catch (error) {
      // Handle errors (e.g., backend not running)
      const errorMessage = { 
        text: 'Sorry, I couldn\'t connect to the server. Make sure the backend is running!', 
        sender: 'ai' 
      };
      setMessages(prevMessages => [...prevMessages, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  /**
   * Handle pressing Enter key to send message
   */
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
    <div className="app">
      <div className="chat-container">
        {/* Header */}
        <div className="chat-header">
          <h1>💬 AI Chat</h1>
        </div>

        {/* Messages Area */}
        <div className="messages-area">
          {messages.length === 0 ? (
            <div className="welcome-message">
              <h2>Welcome! 👋</h2>
              <p>Start a conversation by typing a message below.</p>
            </div>
          ) : (
            messages.map((message, index) => (
              <div 
                key={index} 
                className={`message ${message.sender === 'user' ? 'user-message' : 'ai-message'}`}
              >
                <div className="message-bubble">
                  {message.sender === 'ai' ? (
                    <ReactMarkdown>{message.text}</ReactMarkdown>
                  ) : (
                    message.text
                  )}
                </div>
              </div>
            ))
          )}
          {isLoading && (
            <div className="message ai-message">
              <div className="message-bubble loading">
                <span>Thinking...</span>
              </div>
            </div>
          )}
        </div>

        {/* Input Area */}
        <div className="input-area">
          <input
            type="text"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your message..."
            className="message-input"
          />
          <button 
            onClick={sendMessage} 
            className="send-button"
            disabled={isLoading || !inputText.trim()}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
