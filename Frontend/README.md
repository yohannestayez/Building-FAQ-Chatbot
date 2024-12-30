## index.html
- The index.html file serves as the main structure of the chatbot's user interface. It includes a header with the title of the chatbot, a chat box where the conversation between the user and the bot will be displayed, and an input area where the user can type and send their queries. It also links to the external style.css for styling and script.js for functionality. This file acts as the front-facing component that users interact with when accessing the chatbot.

## style.css
- The style.css file provides the visual design and layout for the chatbot interface. It defines the overall look and feel, such as the font, colors, padding, and button styles. It also specifies the layout of various elements like the chat box, input field, and send button, ensuring a clean and user-friendly experience. Additionally, it includes responsive design features to make sure the chatbot is usable across different screen sizes and devices.

## script.js
- The script.js file handles the interactivity and communication between the user and the Flask backend. It listens for the user’s input in the text field and sends it to the backend through a POST request. It then receives the bot’s response and dynamically updates the chat box with the user's query and the bot’s reply. This file also allows the user to press the "Enter" key to send a message, making the interface more intuitive.