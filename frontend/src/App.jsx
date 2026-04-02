import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = message;

    setChatHistory((prev) => [
      ...prev,
      { sender: "user", text: userMessage }
    ]);

    setMessage("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/chat", {
        message: userMessage
      });

      setChatHistory((prev) => [
        ...prev,
        { sender: "bot", text: response.data.response }
      ]);
    } catch (error) {
      setChatHistory((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "Error: Cannot reach backend."
        }
      ]);
      console.error(error);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  };

  return (
    <div className="app">
      <div className="chat-container">
        <h1>Cloud Support AI Chatbot</h1>

        <div className="chat-box">
          {chatHistory.length === 0 ? (
            <p className="placeholder">
              Ask me about AWS, Linux, or cloud troubleshooting...
            </p>
          ) : (
            chatHistory.map((chat, index) => (
              <div
                key={index}
                className={`message ${chat.sender}`}
              >
                <strong>
                  {chat.sender === "user" ? "You" : "Bot"}:
                </strong>{" "}
                {chat.text}
              </div>
            ))
          )}
        </div>

        <div className="input-area">
          <input
            type="text"
            placeholder="Type your message..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
