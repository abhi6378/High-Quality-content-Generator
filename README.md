# High Quality Content Generator

Live Demo:  
https://abhi6378-high-quality-content-generator-app-zd3axt.streamlit.app/

A production-ready **Multi-Agent Content Generation System** built using **CrewAI**, **Google Gemini**, and **Streamlit**.

Unlike single-prompt chatbots, this application uses **four specialized AI agents** working in a strict sequential pipeline to plan, research, write, and review content — similar to a real editorial workflow.

---

## Agent Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Planner | Converts a vague goal into a clear and structured outline |
| Researcher | Collects facts, statistics, and technical information |
| Writer | Produces a coherent, engaging, and well-structured draft |
| Reviewer | Performs QA, grammar checks, and goal alignment |

---

## Task Flow Architecture (Sequential)

This project follows a **Sequential Process Architecture**.

Flow:

1. User provides a content goal  
2. Planner creates a structured outline  
3. Researcher gathers supporting facts  
4. Writer generates the draft  
5. Reviewer validates quality and accuracy  
6. Final report is produced  

Each step depends strictly on the output of the previous step.

---

## Why Multi-Agent?

Most LLM applications suffer from **"Jack of all trades, master of none."**

This system avoids that problem by enforcing **separation of responsibilities**:

- The Writer does not invent facts  
- The Researcher does not worry about writing style  
- The Reviewer acts as a quality gate  
- The Planner controls scope and direction  

This results in **better reasoning, higher accuracy, and cleaner output**.

---

## How Hallucination Is Reduced

Hallucinations are minimized through **contextual anchoring**:

- Planner defines a strict scope  
- Researcher works only within that scope  
- Writer uses only researcher-provided information  
- Reviewer flags or corrects unsupported claims  

This layered validation significantly improves reliability.

---

## Installation and Setup

### Prerequisites
- Python 3.10 or higher
- Google Gemini API Key

### Clone the Repository
```bash
git clone https://github.com/abhi6378/High-Quality-content-Generator.git
cd High-Quality-content-Generator
Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate
Windows:

bash
Copy code
venv\Scripts\activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Usage
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Steps:

Open the app in your browser

Enter your Gemini API key in the sidebar

Provide a content goal

Watch agents execute sequentially

Download the final report

Project Structure
css
Copy code
High-Quality-content-Generator/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
Author
Abhishek Vaishnav

GitHub:
https://github.com/abhi6378

