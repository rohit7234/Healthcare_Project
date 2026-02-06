// --- 3D Avatar Setup (Three.js) ---
const avatarContainer = document.getElementById('avatar-container');
let scene, camera, renderer, globe;

function init3D() {
    scene = new THREE.Scene();

    // Camera
    camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
    camera.position.z = 2;

    // Renderer
    renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(300, 300); // Start large
    avatarContainer.appendChild(renderer.domElement);

    // Geometry (Icosahedron - Futuristic Orb)
    const geometry = new THREE.IcosahedronGeometry(1.2, 1); // Larger base size
    const material = new THREE.MeshPhongMaterial({
        color: 0x3b82f6,
        wireframe: true,
        emissive: 0x1e3a8a,
        emissiveIntensity: 0.5
    });
    globe = new THREE.Mesh(geometry, material);
    scene.add(globe);

    // Lights
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(2, 2, 5);
    scene.add(light);

    const ambient = new THREE.AmbientLight(0x404040);
    scene.add(ambient);

    animate();
}

function animate() {
    requestAnimationFrame(animate);

    // Idle Animation
    globe.rotation.x += 0.005;
    globe.rotation.y += 0.008;

    renderer.render(scene, camera);
}

function pulseAvatar() {
    // Simple pulse effect when talking
    let scale = 1;
    const interval = setInterval(() => {
        scale = scale === 1 ? 1.1 : 1;
        globe.scale.set(scale, scale, scale);
    }, 200);

    setTimeout(() => {
        clearInterval(interval);
        globe.scale.set(1, 1, 1);
    }, 2000); // Pulse for 2 seconds
}

// Initialize 3D
init3D();

// --- Chat Logic ---

const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const historyList = document.getElementById('history-list');
const welcomeContainer = document.getElementById('welcome-container');
const chatWrapper = document.getElementById('chat-wrapper');
const avatarEl = document.getElementById('avatar-container');

// State
let conversationHistory = JSON.parse(localStorage.getItem('healthBotHistory')) || [];
let currentChatId = null;

// Define setInput strictly in global scope
window.setInput = function (text) {
    userInput.value = text;
    sendMessage();
}

// Initial render
renderHistory();

function toggleViewState(isChatting) {
    if (isChatting) {
        welcomeContainer.classList.add('hidden');
        chatWrapper.className = 'chat-wrapper visible';
        chatWrapper.style.display = ''; // Ensure it's not forced hidden
        avatarEl.classList.add('active');

        // Resize renderer to match smaller container
        if (renderer) {
            renderer.setSize(120, 120);
        }
    } else {
        welcomeContainer.classList.remove('hidden');
        chatWrapper.className = 'chat-wrapper'; // Hide
        chatWrapper.style.display = 'none'; // Force hide
        avatarEl.classList.remove('active');

        // Resize renderer to match larger container
        if (renderer) {
            renderer.setSize(300, 300);
        }
    }
}

if (conversationHistory.length === 0) {
    startNewChat();
} else {
    // Load last chat
    loadChat(conversationHistory[0].id);
}

// Auto-resize textarea
userInput.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});

// Enter to send
userInput.addEventListener("keypress", function (event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault(); // Prevent newline
        sendMessage();
    }
});

function generateId() {
    return '_' + Math.random().toString(36).substr(2, 9);
}

function startNewChat() {
    currentChatId = generateId();
    // Don't create object yet, just reset UI
    toggleViewState(false);
    userInput.value = '';
    // Highlight "New Chat" in sidebar? Custom logic needed or just deselect all
    renderHistory();
    chatBox.innerHTML = ''; // Clear chatbox when starting new chat
}

function saveHistory() {
    localStorage.setItem('healthBotHistory', JSON.stringify(conversationHistory));
}

// --- Modal Logic ---
const modal = document.getElementById('confirmation-modal');
const modalTitle = document.getElementById('modal-title');
const modalDesc = document.getElementById('modal-desc');
const modalConfirmBtn = document.getElementById('modal-confirm');
const modalCancelBtn = document.getElementById('modal-cancel');

let currentConfirmCallback = null;

function showModal(title, desc, onConfirm) {
    modalTitle.innerText = title;
    modalDesc.innerHTML = desc; // Allow HTML for bold text
    currentConfirmCallback = onConfirm;
    modal.classList.remove('hidden');
}

function hideModal() {
    modal.classList.add('hidden');
    currentConfirmCallback = null;
}

modalConfirmBtn.onclick = () => {
    if (currentConfirmCallback) currentConfirmCallback();
    hideModal();
};

modalCancelBtn.onclick = hideModal;

// Close on outside click
modal.onclick = (e) => {
    if (e.target === modal) hideModal();
};

function clearAllHistory() {
    showModal("Clear All History", "Are you sure you want to delete <b>ALL</b> chat history? This cannot be undone.", () => {
        localStorage.removeItem('healthBotHistory');
        conversationHistory = [];
        startNewChat();
    });
}

function deleteChat(id, event) {
    event.stopPropagation(); // Don't trigger loadChat
    showModal("Delete Consultation", "Remove this session from history?", () => {
        conversationHistory = conversationHistory.filter(c => c.id !== id);
        saveHistory();

        // If we deleted the current chat, switch to another or new
        if (id === currentChatId) {
            if (conversationHistory.length > 0) {
                loadChat(conversationHistory[0].id);
            } else {
                startNewChat();
            }
        }
        renderHistory();
    });
}

function renderHistory() {
    historyList.innerHTML = '';
    conversationHistory.forEach(chat => {
        const div = document.createElement('div');
        div.className = `history-item ${chat.id === currentChatId ? 'active' : ''}`;

        // Title Span
        const span = document.createElement('span');
        span.innerText = chat.title || "New Consultation";

        // Delete Button
        const delBtn = document.createElement('button');
        delBtn.className = 'history-delete-btn';
        delBtn.innerHTML = '<i class="fa-solid fa-trash"></i>';
        delBtn.onclick = (e) => deleteChat(chat.id, e);

        div.appendChild(span);
        div.appendChild(delBtn);

        div.onclick = () => loadChat(chat.id);
        historyList.appendChild(div);
    });
}

function loadChat(id) {
    currentChatId = id;
    renderHistory(); // Re-render to update 'active' class
    toggleViewState(true); // Show chat area
    const chat = conversationHistory.find(c => c.id === id);
    if (chat) renderChat(chat);
}

function renderChat(chat) {
    chatBox.innerHTML = '';
    chat.messages.forEach(msg => {
        appendMessageStyles(msg.sender, msg.text, false); // No streaming for history
    });
}

function appendMessageStyles(sender, text, stream = false) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message';

    const avatar = document.createElement('div');
    avatar.className = `message-avatar ${sender === 'user' ? 'user-avatar' : 'bot-avatar'}`;
    avatar.innerHTML = sender === 'user' ? '<i class="fa-solid fa-user"></i>' : '<i class="fa-solid fa-robot"></i>';

    const content = document.createElement('div');
    content.className = 'message-content';

    msgDiv.appendChild(avatar);
    msgDiv.appendChild(content);
    chatBox.appendChild(msgDiv);

    if (stream && sender === 'bot') {
        // Stream the markdown content
        typeText(content, text);
        pulseAvatar(); // Trigger 3D pulse
    } else {
        // Render immediately
        content.innerHTML = sender === 'bot' ? marked.parse(text) : text;
        if (sender === 'bot') {
            hljs.highlightAll(); // Highlight code blocks
        }
    }

    // Scroll
    scrollToBottom();
}

function scrollToBottom() {
    const wrapper = document.querySelector('.chat-wrapper');
    wrapper.scrollTop = wrapper.scrollHeight;
}

function typeText(element, text) {
    // Render Markdown first, but reveal strictly properly?
    // Actually, simple typewriter effect on HTML is hard.
    // Better strategy for "ChatGPT" style:
    // Render the chunk, but update the innerHTML repeatedly.
    // However, simplest "good looking" way is:

    const html = marked.parse(text);
    element.innerHTML = ""; // Clear

    // We will simulate streaming by appending chunks of the logic,
    // but honestly just appending words is safer for HTML tags.
    // Let's split by space (crude but works for plain text structure)
    // Note: Breaking HTML tags breaks render.
    // "Fake" streaming: Just fade in? No, user wants streaming.

    // Robust Streaming (Advanced):
    let i = 0;
    const speed = 15; // ms

    // Safe approach: render FULL html invisibly, then copy text content? NO.
    // approach: Just use interval to add chars to a buffer and re-markdown parse?
    // Costly but ensures HTML is valid.

    let buffer = "";
    const interval = setInterval(() => {
        buffer += text.charAt(i);
        element.innerHTML = marked.parse(buffer); // Re-parse every char (modern browsers handle this fine for short texts)
        hljs.highlightAll(); // Highlight code blocks after each update
        scrollToBottom();
        i++;
        if (i > text.length - 1) {
            clearInterval(interval);
        }
    }, speed);
}

async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    // Switch to chat view
    toggleViewState(true);

    // Initial check: if currentChatId corresponds to nothing in history (new chat state), create it
    let currentChat = conversationHistory.find(c => c.id === currentChatId);
    if (!currentChat) {
        currentChat = {
            id: currentChatId,
            title: text.substring(0, 30) + "...",
            messages: []
        };
        conversationHistory.unshift(currentChat);
        renderChat(currentChat); // Clean previous if any
    } else {
        // Update Title if generic
        if (currentChat.messages.length === 0) {
            currentChat.title = text.substring(0, 30) + "...";
        }
    }

    renderHistory();

    // UI
    userInput.value = '';
    userInput.style.height = 'auto'; // Reset height

    // Add user message
    currentChat.messages.push({ sender: 'user', text: text });
    appendMessageStyles('user', text, false);
    saveHistory();

    // Call API
    try {
        const response = await fetch('http://localhost:8000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });

        const data = await response.json();
        const botResponse = data.response;

        // Add bot message
        currentChat.messages.push({ sender: 'bot', text: botResponse });
        saveHistory();

        appendMessageStyles('bot', botResponse, true); // True = Stream it!

    } catch (error) {
        console.error(error);
        appendMessageStyles('bot', "Error connecting to server. Please ensure backend is running.", false);
    }
}
