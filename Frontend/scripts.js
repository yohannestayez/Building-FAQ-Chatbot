const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

function appendMessage(sender, message) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender);
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
}

async function sendMessage() {
    const query = userInput.value.trim();
    if (!query) return;

    // Display user message
    appendMessage("user", query);

    // Clear input field
    userInput.value = "";

    // Call the backend API
    fetchChatResponse(query);
}

function fetchChatResponse(query) {
    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
    })
    .then(response => {
        // Handle non-OK responses
        if (!response.ok) {
            return Promise.reject(new Error(`Error: ${response.statusText}`));
        }
        return response.json();
    })
    .then(data => {
        appendMessage("bot", data.response);
    })
    .catch(error => {
        appendMessage("bot", `Sorry, there was an error. ${error.message}`);
    });
}

sendBtn.addEventListener("click", sendMessage);

// Allow "Enter" key to send the message
userInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") sendMessage();
});