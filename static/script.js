let userName = null;

function addMessage(message, type) {
    const chatBox = document.getElementById("chat-box");

    const div = document.createElement("div");

    div.classList.add("message");

    if (type === "user") {
        div.classList.add("user-message");
    } else {
        div.classList.add("bot-message");
    }

    // Make sure we display the actual text
    div.textContent = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendMessage() {

    // Get the input element
    const input = document.getElementById("message");

    // Get the text inside the input
    const message = input.value.trim();

    // Don't send empty messages
    if (!message) {
        return;
    }

    // Display user's message
    addMessage(message, "user");

    // Clear input
    input.value = "";

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message,
                user_name: userName
            })
        });

        const data = await response.json();

        // Display bot response
        addMessage(data.response, "bot");

    } catch (error) {

        console.error("Error:", error);

        addMessage(
            "Sorry, something went wrong while connecting to the chatbot.",
            "bot"
        );
    }
}


document
    .getElementById("message")
    .addEventListener("keydown", function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    });