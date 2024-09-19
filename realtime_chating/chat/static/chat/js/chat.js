const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);

// Event listener for receiving messages
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const messages = document.getElementById('messages');
    const message = document.createElement('div');
    message.textContent = data.message;
    messages.appendChild(message);
};

// Event listener for handling WebSocket errors
chatSocket.onerror = function(e) {
    console.error('WebSocket error: ', e);
};

// Event listener for closing the WebSocket connection
chatSocket.onclose = function(e) {
    console.log('WebSocket closed: ', e);
};

// Send message when the button is clicked
document.getElementById('send-button').onclick = function(e) {
    const messageInputDom = document.getElementById('message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';  // Clear input field after sending
};
