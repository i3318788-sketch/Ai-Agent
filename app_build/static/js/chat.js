// AI Chatbot Demo Controller

document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chatForm');
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');
    const chatTyping = document.getElementById('chatTyping');
    const chatSendBtn = document.getElementById('chatSendBtn');
    const suggestionBtns = document.querySelectorAll('.suggestion-btn');

    if (chatForm && chatInput && chatMessages && chatTyping) {
        // Send a message via suggestion button
        suggestionBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const query = btn.getAttribute('data-query');
                if (query) {
                    sendMessage(query);
                }
            });
        });

        // Submit form
        chatForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const messageText = chatInput.value.trim();
            if (messageText) {
                sendMessage(messageText);
                chatInput.value = '';
            }
        });
    }

    // Core message handler
    async function sendMessage(text) {
        // Append user message UI
        appendMessage(text, 'user');
        scrollToBottom();

        // Show typing indicator
        showTypingIndicator(true);
        scrollToBottom();

        // Disable input during query
        chatInput.disabled = true;
        chatSendBtn.disabled = true;

        // Introduce a subtle minimum delay (e.g., 900ms) for realistic UX
        const startTime = Date.now();

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: text })
            });

            const result = await response.json();
            const elapsed = Date.now() - startTime;
            const remainingDelay = Math.max(900 - elapsed, 0);

            // Wait for delay to expire to make typing indicator look natural
            await new Promise(resolve => setTimeout(resolve, remainingDelay));

            if (response.ok && result.response) {
                appendMessage(result.response, 'bot');
            } else {
                appendMessage("I apologize, but my intelligence core encountered an error. Please try again in a moment.", "bot");
            }
        } catch (error) {
            console.error('Chat error:', error);
            appendMessage("Unable to connect to AeroBot. Please verify your local Flask server is running.", "bot");
        } finally {
            showTypingIndicator(false);
            chatInput.disabled = false;
            chatSendBtn.disabled = false;
            chatInput.focus();
            scrollToBottom();
        }
    }

    // Append standard markup message bubble
    function appendMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;

        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        avatarDiv.innerHTML = sender === 'bot' 
            ? '<i class="fa-solid fa-robot"></i>' 
            : '<i class="fa-solid fa-user"></i>';

        const textDiv = document.createElement('div');
        textDiv.className = 'message-text';
        
        // Simple Markdown-like parsing for bold text (**text**) and newlines
        let formattedText = escapeHTML(text)
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');

        // Check if there are list items
        if (formattedText.includes('1. ') || formattedText.includes('- ')) {
            // Add custom list rendering if helpful, or let line breaks display it
        }

        textDiv.innerHTML = formattedText;

        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(textDiv);
        chatMessages.appendChild(messageDiv);
    }

    // Toggle typing indicator visibility
    function showTypingIndicator(show) {
        chatTyping.style.display = show ? 'flex' : 'none';
    }

    // Scroll chat area to the newest messages
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Utility to prevent injection of raw tags into HTML
    function escapeHTML(str) {
        return str.replace(/[&<>'"]/g, 
            tag => ({
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                "'": '&#39;',
                '"': '&quot;'
            }[tag] || tag)
        );
    }
});
