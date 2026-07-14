# AeroAutomate AI Automation Service Platform

A premium landing page, interactive AI agent demo, and insights blog built for an elite AI automation consulting business.

---

## Features
1. **Premium Landing Page**: A fully responsive dark-themed landing page featuring hero metrics, service offerings, and a lead capturing Contact form.
2. **AI Agent Demo Room**: An interactive chatbot interface that simulates a live consultation with an AI operations architect, with a natural typing indicator, pre-set query suggestions, and rule-based expert answers.
3. **Operations Blog**: A structured news layout containing three expand-and-read articles focusing on AI trends, prototyping tech stacks, and security protocols.
4. **Lead Logging**: The Flask backend captures contact form inquiries and logs them locally to `inquiries.json`.

---

## File Structure
```text
app_build/
├── app.py                  # Main Flask application & response engine
├── requirements.txt         # Package dependencies (Flask, python-dotenv)
├── README.md               # Setup and execution guide
├── inquiries.json          # Local database for contact inquiries (auto-generated)
├── templates/
│   ├── base.html           # Shared layout, navbar, footer, scripts
│   ├── index.html          # Landing Page & contact form
│   ├── agent_demo.html     # AI Chatbot interactive interface
│   └── blog.html           # Blog post index
└── static/
    ├── css/
    │   └── style.css       # Custom modern stylesheet
    └── js/
        ├── main.js         # Navigation and contact form submissions
        └── chat.js         # Chat interface and typing delays
```

---

## Local Setup Instructions

### 1. Prerequisites
Ensure you have **Python 3.8 or higher** installed on your system. You can check this by running:
```bash
python --version
```

### 2. Create and Activate a Virtual Environment
Navigate to the `app_build/` directory in your terminal and run:

**Windows (PowerShell/CMD):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install Flask and other necessary packages:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask development server:
```bash
python app.py
```

### 5. Access in Web Browser
Open your browser and navigate to:
```text
http://127.0.0.1:5000/
```
- Use the navbar to switch between the **Home page**, the **AI Agent Demo**, and the **Blog**.
- Check `app_build/inquiries.json` after submitting a message in the contact form to see the captured lead logs!
