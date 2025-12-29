# High Quality Content Generator

Live Demo:  
https://abhi6378-high-quality-content-generator-app-zd3axt.streamlit.app/

A production-ready **Multi-Agent Content Generation System** built using **CrewAI**, **Google Gemini**, and **Streamlit**.

Unlike single-prompt chatbots, this application uses **four specialized AI agents** working in a sequential pipeline to plan, research, write, and review content — similar to a real editorial workflow.

---

## Agent Roles and Responsibilities

| Role | Responsibility |
|-----|---------------|
| Planner | Converts a vague goal into a structured outline |
| Researcher | Collects facts, statistics, and technical data |
| Writer | Produces a coherent and engaging draft |
| Reviewer | Performs QA, grammar checks, and alignment validation |

---

## Task Flow Architecture

This project follows a **Sequential Process Architecture**.  
The output of one agent becomes the input for the next.

```mermaid
graph LR
    User[User Input] --> Planner[Planner]
    Planner --> Researcher[Researcher]
    Researcher --> Writer[Writer]
    Writer --> Reviewer[Reviewer]
    Reviewer --> Result[Final Report]
Why Multi-Agent?
Most LLM applications suffer from "Jack of all trades, master of none."

This system avoids that by enforcing separation of responsibilities:

The Writer does not invent facts

The Researcher does not worry about tone

The Reviewer validates accuracy and clarity

The Planner controls scope and structure

This results in higher accuracy, better reasoning, and cleaner output.

How Hallucination Is Reduced
Hallucinations are minimized through contextual anchoring:

Planner defines strict scope

Researcher works only within that scope

Writer can only use researcher output

Reviewer flags unsupported claims

This layered validation significantly improves reliability.

Installation and Setup
Prerequisites
Python 3.10+

Google Gemini API Key

Clone Repository
bash
Copy code
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
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open the live app

Enter your Gemini API key

Enter a content goal

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
