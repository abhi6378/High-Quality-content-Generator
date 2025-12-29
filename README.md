# 🚀 High Quality Content Generator

**🔴 Live Demo:** [Click here to try the App](https://abhi6378-high-quality-content-generator-app-zd3axt.streamlit.app/)  

A production-ready **Multi-Agent System** that automates high-quality content generation. Built with **CrewAI** and **Google Gemini**, wrapped in an interactive **Streamlit** dashboard.

Unlike standard chatbots, this application employs a **Squad of 4 Specialized AI Agents** working in a sequential pipeline to Plan, Research, Write, and Review content, mimicking a real-world editorial team.

---

## 🧩 Agent Roles & Responsibilities

We utilize **Role-Based Agent Engineering** to ensure specific accountability.

| Agent Icon | Role | Responsibility |
| :---: | :--- | :--- |
| 🧠 | **The Planner** | Breaks down vague user goals into a structured logical outline. Prevents aimless wandering. |
| 🔍 | **The Researcher** | Scours for accurate facts, statistics, and technical details based *only* on the Planner's outline. |
| ✍️ | **The Writer** | Synthesizes the research into a cohesive, engaging narrative or report. Focuses on flow and tone. |
| ⚖️ | **The Reviewer** | Performs Quality Assurance (QA). Checks for clarity, grammatical errors, and alignment with the user's original goal. |

---

## 🔄 Task Flow Architecture

This project uses a **Sequential Process** architecture. The output of one agent becomes the context for the next.

```mermaid
graph LR
    User[User Input] --> A[🧠 Planner]
    A -- Outline --> B[🔍 Researcher]
    B -- Facts & Data --> C[✍️ Writer]
    C -- Draft --> D[⚖️ Reviewer]
    D -- Final Polish --> Result[📄 Final Report]
    
    style User fill:#f9f,stroke:#333,stroke-width:2px
    style Result fill:#9f9,stroke:#333,stroke-width:2px
🚀 Why Multi-Agent?
Most LLM applications suffer from "Jack of all trades, master of none." By using a Multi-Agent Architecture, we achieve:

Separation of Concerns: The "Writer" doesn't need to worry about fact-checking; the "Researcher" has already done it. This reduces cognitive load on the model.

Self-Correction: A dedicated "Reviewer" agent acts as a final filter, catching errors that a single-shot prompt might miss.

Complex Reasoning: Breaking a task into [Plan → Research → Execute] mimics human cognitive workflows, leading to significantly higher quality output.

🛡️ How Hallucination is Reduced
One of the biggest risks in AI is hallucination (inventing facts). This project mitigates that risk through Contextual Anchoring:

The Planner's Guardrails: The Planner sets the scope immediately. The Researcher is not allowed to search outside this scope.

Sequential Dependency: The Writer is not allowed to invent information. It is strictly instructed to use only the data provided by the Researcher.

The Reviewer Step: The final agent is explicitly prompted to look for inconsistencies. If the text claims "X is true" but the research didn't support it, the Reviewer flags or fixes it.

🛠️ Installation & Setup
Prerequisites
Python 3.10+

A Google Gemini API Key (Get it from Google AI Studio)

1. Clone the Repository
Bash

git clone [https://github.com/yourusername/high-quality-content-generator.git](https://github.com/yourusername/high-quality-content-generator.git)
cd high-quality-content-generator
2. Create a Virtual Environment (Recommended)
Windows:

Bash

python -m venv venv
venv\Scripts\activate
Mac/Linux:

Bash

python -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
💻 Usage
Run the Streamlit application:

Bash

streamlit run app.py
The web interface will open in your browser (usually http://localhost:8501).

Enter your Google API Key in the sidebar (it is handled securely and never saved).

Type your goal (e.g., "Write a guide on AI in Healthcare").

Watch the agents work in real-time and download the final report.

📂 Project Structure
Plaintext

high-quality-content-generator/
├── app.py              # Main application logic (Streamlit + CrewAI)
├── requirements.txt    # Project dependencies
├── README.md           # Documentation
└── .gitignore          # Files to ignore in version control
👤 Author
Abhishek 🔗 LinkedIn Profile (Add your actual link here)

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the project.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📜 License
Distributed under the MIT License. See LICENSE for more information.

<div align="center"> Built with ❤️ using <a href="https://www.crewai.com/">CrewAI</a> & <a href="https://streamlit.io/">Streamlit</a> </div>