import os
import json
import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'ai-automation-dev-key')

# Simple path to store contact form submissions
INQUIRIES_FILE = os.path.join(os.path.dirname(__file__), 'inquiries.json')

# Simulated Knowledge Base for AI Consultant Agent
KNOWLEDGE_BASE = [
    {
        "keywords": [r"service", r"offer", r"what do you do", r"capabilities"],
        "response": "We specialize in end-to-end AI automation. Our core services include:\n"
                    "1. **Autonomous AI Agents**: Customer support, custom internal tools, and email dispatchers.\n"
                    "2. **Workflow Integrations**: Connecting CRMs, databases, and APIs using custom logic or platforms like Make/Zapier.\n"
                    "3. **Data Pipelines & Extraction**: Automated web scraping, doc parsing, and AI processing.\n"
                    "Let us know what bottlenecks you're facing, and we can design an agent for it!"
    },
    {
        "keywords": [r"cost", r"price", r"pricing", r"budget", r"how much"],
        "response": "Our projects are tailored to your business needs:\n"
                    "- **Basic Automations**: (e.g., simple lead syncing, custom notifications) starting at $1,500 - $3,000.\n"
                    "- **Custom AI Agents**: (e.g., LLM-powered email responders, document analysers) ranging from $4,000 - $8,000.\n"
                    "- **Enterprise Workflows**: Full operational automation from $10,000+.\n"
                    "We always provide a free initial consultation and a detailed fixed-price quote!"
    },
    {
        "keywords": [r"timeline", r"how long", r"duration", r"time frame", r"speed"],
        "response": "Implementation speed is one of our key priorities:\n"
                    "- Simple automated workflows are usually deployed within **5 to 10 business days**.\n"
                    "- Complex custom AI agent integrations typically take **3 to 6 weeks** depending on security protocols and API integrations."
    },
    {
        "keywords": [r"consult", r"hire", r"contact", r"call", r"get started", r"meeting"],
        "response": "Getting started is easy! You can fill out the contact form on our **Home page**, or email us directly. We'll set up a 30-minute discovery call to map out your processes and find where AI can save you the most hours."
    },
    {
        "keywords": [r"agent", r"what is an agent", r"how does it work"],
        "response": "An AI Agent is an autonomous program powered by a Large Language Model (LLM). Unlike a traditional bot, it can plan tasks, interact with external software (like Slack, Gmail, or your CRM), search databases, and make decisions to complete complex, multi-step workflows without human intervention."
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo')
def demo():
    return render_template('agent_demo.html')

@app.route('/blog')
def blog():
    # Pre-populating blog posts
    posts = [
        {
            "id": 1,
            "title": "Unlocking ROI: How Autonomous Agents Save Small Businesses 20+ Hours a Week",
            "date": "July 12, 2026",
            "author": "PM @ PM Team",
            "summary": "AI agents are no longer just for big tech. Learn how custom LLM pipelines are transforming administrative workflows, sales outreach, and customer service for scaling teams.",
            "content": "In 2026, the competitive landscape has shifted. Businesses that leverage autonomous AI agents are scaling operations without adding overhead. An AI agent is a piece of software that uses LLM reasoning to call APIs, write drafts, update databases, and send emails. For example, a customer service agent can analyze incoming support tickets, search a internal database for answers, draft a highly specific response, and send it—or escalate to a human if necessary. By delegating these repetitive tasks, businesses free up critical human talent for strategic growth. Our typical clients see a complete return on investment within the first 30 days."
        },
        {
            "id": 2,
            "title": "Choosing Your Stack: Python/Flask vs Node.js for Fast AI Prototyping",
            "date": "June 28, 2026",
            "author": "Lead Architect",
            "summary": "When building AI-powered apps, your choice of backend stack determines how fast you can iterate. Here's why Flask remains a top choice for AI startups.",
            "content": "Python is the undisputed language of AI and machine learning. From LangChain and LlamaIndex to Hugging Face and PyTorch, the ecosystem is built for Python. Flask, being a lightweight microframework, allows you to spin up secure API endpoints with minimal boilerplate. This makes it perfect for AI prototyping, where you need to quickly integrate model APIs, manage asynchronous tasks, and serve simple HTML interfaces. While Node.js has great concurrency, the ease of writing data parsing pipelines and importing AI helper modules directly in Python makes Flask the clear choice for modern automation builders."
        },
        {
            "id": 3,
            "title": "The Security Checklist for Deploying Custom LLMs in Internal Workflows",
            "date": "May 15, 2026",
            "author": "QA Auditor",
            "summary": "Connecting AI models to your private databases comes with security risks. Here is a checklist to ensure your customer data remains safe.",
            "content": "Security is the number one concern for enterprise AI adoption. If an AI agent has access to write data to your CRM or read emails, a prompt injection attack could trick it into leaking confidential database contents or deleting critical entries. To mitigate these risks, follow these rules: 1) Implement strict role-based access controls (RBAC) so the agent can only access directories it absolutely needs. 2) Never pass user inputs directly to command executors. 3) Maintain comprehensive audit logs of all API actions performed by the agent. 4) Use secure, private API gateways when connecting models to internal APIs."
        }
    ]
    return render_template('blog.html', posts=posts)

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No data provided"}), 400
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        # Simple validation
        if not name or not email or not message:
            return jsonify({"status": "error", "message": "All fields are required"}), 400
        
        # Simple email format check
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"status": "error", "message": "Invalid email address format"}), 400

        # Load existing inquiries or start new
        inquiries = []
        if os.path.exists(INQUIRIES_FILE):
            try:
                with open(INQUIRIES_FILE, 'r', encoding='utf-8') as f:
                    inquiries = json.load(f)
            except json.JSONDecodeError:
                pass # Overwrite if corrupt
        
        # Append new inquiry
        inquiries.append({
            "name": name,
            "email": email,
            "message": message,
            "timestamp": request.date or "N/A"
        })

        with open(INQUIRIES_FILE, 'w', encoding='utf-8') as f:
            json.dump(inquiries, f, indent=4)

        return jsonify({"status": "success", "message": "Thank you! Your message has been logged successfully."})

    except Exception as e:
        return jsonify({"status": "error", "message": f"Server error: {str(e)}"}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"status": "error", "message": "Message is missing"}), 400

        user_message = data.get('message', '').strip().lower()
        if not user_message:
            return jsonify({"response": "I didn't catch that. Could you please type something?"})

        # Search for keyword matches in knowledge base
        for entry in KNOWLEDGE_BASE:
            for pattern in entry["keywords"]:
                if re.search(pattern, user_message):
                    return jsonify({"response": entry["response"]})

        # Fallback simulation response
        fallback_msg = (
            f"That's an interesting question about automation! While I simulate my intelligence, "
            f"this is exactly the type of process optimization we design at our agency. "
            f"I recommend scheduling a discovery call. Just head to our Home page, submit a request, "
            f"and our automation engineers will sketch out a solution tailored to your exact query: '{data.get('message')}'!"
        )
        return jsonify({"response": fallback_msg})

    except Exception as e:
        return jsonify({"status": "error", "message": f"Chat failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
