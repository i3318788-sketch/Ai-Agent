# Technical Specification: AI Automation Services Landing Page & Demo

This document outlines the architecture, requirements, and tech stack for the AI Automation Services website.

---

## 1. Executive Summary
The goal is to build a high-converting, professional, and visually stunning landing page for an AI Automation Service Business. The website will showcase the business's capabilities, offer a interactive AI Agent demo page to demonstrate value, feature a blog/news section to show thought leadership, and include a contact form to capture leads. The application will be powered by a Python/Flask backend and a modern HTML5/CSS3/JavaScript frontend.

---

## 2. Requirements

### 2.1 Functional Requirements
- **Landing Page (Home)**:
  - **Hero Section**: Sleek dark/glassmorphic design with a clear value proposition, CTA buttons ("Try Demo", "Get Started").
  - **Features/Services Section**: Dynamic cards detailing services (e.g., custom LLM integration, workflow automation, data extraction).
  - **Contact Us Section**: A functional HTML form that submits user inquiries to the Flask backend.
- **AI Agent Demo Page**:
  - Chat interface that mimics a production-grade AI assistant.
  - Allows users to enter prompt/query and receive a real-time responsive answer.
  - Backend integration using a rule-based AI automation consultant bot that answers questions about automation, services, pricing, and timelines, simulating an actual AI conversation.
- **Blog Section**:
  - Standard blog index containing 3 high-quality placeholder articles related to AI automation trends.
  - Clicking on a card allows reading the article.
- **Admin/Inquiry logs (Optional/Bonus)**:
  - The backend will log contact submissions to a local JSON file or console to ensure lead capture works.

### 2.2 Non-Functional Requirements
- **Performance**: Instant load times with standard CSS and native JS (no heavy external libraries unless needed).
- **Design & Typography**: Modern dark mode/glassmorphism design using Google Fonts (e.g., *Inter* or *Outfit*), clean gradients, micro-animations, and responsive layouts.
- **Robustness**: Proper error handling for missing inputs, API failures in chat, and invalid email addresses in the contact form.

---

## 3. Architecture & Tech Stack

### 3.1 Tech Stack
- **Backend**: Python 3.x, Flask, `python-dotenv` (for config variables).
- **Frontend**: HTML5, Vanilla CSS3 (Custom styling with modern responsive variables), Vanilla JavaScript (ES6+).
- **Styling Paradigm**: CSS variables for colors, spacing, and typography. Rich gradients, hover states, and smooth transiton animations.

### 3.2 File Structure
The project will be organized inside `app_build/` as follows:
```text
app_build/
├── app.py                  # Main Flask application and API routes
├── requirements.txt         # Python dependencies
├── README.md               # Setup and execution instructions
├── templates/
│   ├── base.html           # Shared layout (Header, Navbar, Footer)
│   ├── index.html          # Landing Page (Hero, Features, Contact Form)
│   ├── agent_demo.html     # AI Agent Chat Demo UI
│   └── blog.html           # Blog listing and articles
└── static/
    ├── css/
    │   └── style.css       # Unified premium design styles
    └── js/
        ├── main.js         # Core UI interactions (contact form ajax)
        └── chat.js         # Chatbot interaction handling (ajax queries)
```

### 3.3 Backend API Endpoints
1. `GET /`: Renders the main landing page.
2. `GET /demo`: Renders the AI Agent Demo page.
3. `GET /blog`: Renders the blog section.
4. `POST /api/contact`: Accepts JSON containing `{name, email, message}`. Validates inputs, appends the inquiry to `inquiries.json`, and returns success.
5. `POST /api/chat`: Accepts JSON containing `{message}`. Processes the prompt through a response engine and returns `{response}`.

---

## 4. AI Agent Integration Detail
- The backend will implement an interactive **AI Automation Consultation Engine**.
- If the user types questions like *"What is AI automation?"*, *"How much does a project cost?"*, *"What services do you offer?"*, or custom inquiries, it will provide detailed, context-aware answers.
- A fallback logic will mock a creative LLM response based on keywords or generate a tailored response explaining how the business can solve that exact problem.

---

## 5. Verification Plan
- **Backend Unit Tests**: Verification of `/api/chat` and `/api/contact` routes.
- **Manual QA**: Verifying mobile responsiveness, contact form submission handling, and chatbot flow using dev server.
