import streamlit as st
import os
import sys
import time
import re
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# ==============================================================================
# 1️⃣ HELPER CLASS: REDIRECT STDOUT TO STREAMLIT
# ==============================================================================
# This class tricks Python into writing "print" statements to our Streamlit app
# instead of the invisible console.
class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']
        self.color_index = 0

    def write(self, data):
        # Filter out ANSI escape codes (terminal colors) to keep it clean
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        cleaned_data = ansi_escape.sub('', data)

        # Update the buffer and write to the Streamlit expander
        if cleaned_data.strip():
            self.buffer.append(cleaned_data)
            # We use distinct lines to make it readable
            self.expander.code("".join(self.buffer[-20:]), language="text") # Show last 20 lines to keep it snappy

    def flush(self):
        pass

# ==============================================================================
# 2️⃣ PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="High Quality content Generator",
    page_icon="🕵️‍♂️",
    layout="wide"
)

# Custom CSS for that "Pro" look
st.markdown("""
    <style>
    .stApp {background-color: #0e1117;}
    .reportview-container .main .block-container {padding-top: 2rem;}
    div[data-testid="stExpander"] {border: 1px solid #444; border-radius: 4px;}
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 3️⃣ SIDEBAR & CONFIGURATION
# ==============================================================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/9329/9329276.png", width=80)
    st.title("🤖 Agent Control")
    
    # API Key Input
    api_key = st.text_input(
        "🔑 Gemini API Key", 
        type="password", 
        help="Required to activate the agents."
    )
    
    st.divider()
    
    # Model Selection (Bonus Feature)
    model_choice = st.selectbox(
        "🧠 Select Brain", 
        ["gemini-2.5-flash-lite"],
        index=0
    )
    
    st.divider()
    
    st.markdown("### 🛠️ Team Structure")
    st.success("🧠 **Planner** (Strategy)")
    st.info("🔍 **Researcher** (Data)")
    st.warning("✍️ **Writer** (Content)")
    st.error("⚖️ **Reviewer** (Quality)")

# ==============================================================================
# 4️⃣ MAIN UI
# ==============================================================================
st.title("High Quality content Generator")
st.caption("🚀 Powered by CrewAI & Gemini Pro | Live Execution Logs Enabled")

# Input Section
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_area(
        "🎯 Mission Objective:", 
        placeholder="E.g., Research the latest trends in renewable energy storage for 2025.",
        height=100
    )
with col2:
    st.write("") # Spacer
    st.write("") 
    run_btn = st.button("🚀 Deploy Agents", type="primary", use_container_width=True)

# ==============================================================================
# 5️⃣ EXECUTION LOGIC
# ==============================================================================
if run_btn:
    if not api_key:
        st.toast("❌ API Key is missing!", icon="🛑")
        st.stop()
    
    if not user_input:
        st.toast("❌ Please define a mission!", icon="⚠️")
        st.stop()

    # --- INITIALIZE AGENTS ---
    os.environ["GOOGLE_API_KEY"] = api_key
    
    llm = ChatGoogleGenerativeAI(
        model=model_choice,
        verbose=True,
        temperature=0.5,
        google_api_key=api_key
    )

    # Define Agents
    planner = Agent(
        role="Planner",
        goal="Create a structured outline for the task",
        backstory="Senior Strategist. You plan before anyone acts.",
        llm=llm,
        verbose=True
    )
    researcher = Agent(
        role="Researcher",
        goal="Find accurate data to support the plan",
        backstory="Expert OSINT Analyst. You find facts others miss.",
        llm=llm,
        verbose=True
    )
    writer = Agent(
        role="Writer",
        goal="Write the final report",
        backstory="Senior Editor. You write like a pro.",
        llm=llm,
        verbose=True
    )
    reviewer = Agent(
        role="Reviewer",
        goal="Quality control",
        backstory="Strict Fact-Checker. You ensure 100% accuracy.",
        llm=llm,
        verbose=True
    )

    # Define Tasks
    task1 = Task(
        description=f"Create a detailed outline for: {user_input}",
        expected_output="Bulleted list outline",
        agent=planner
    )
    task2 = Task(
        description="Research the outline points. Gather key stats and facts.",
        expected_output="Detailed research notes",
        agent=researcher
    )
    task3 = Task(
        description="Write a full report based on the research.",
        expected_output="Markdown formatted article",
        agent=writer
    )
    task4 = Task(
        description="Review and polish the article.",
        expected_output="Final clean markdown",
        agent=reviewer
    )

    crew = Crew(
        agents=[planner, researcher, writer, reviewer],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential
    )

    # --- LIVE LOGGING UI ---
    st.subheader("📡 Live Agent Feed")
    
    # Create an empty container for the terminal
    log_container = st.empty()
    
    # The actual "Terminal" box
    with log_container.container():
        st.markdown("initializing uplinks...")
        terminal = st.empty() 

    # Redirect stdout to our terminal
    original_stdout = sys.stdout
    sys.stdout = StreamToExpander(terminal)

    try:
        with st.spinner("🤖 Agents are working on your mission..."):
            result = crew.kickoff()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        result = str(e)
    finally:
        # Restore normal stdout so we don't break Streamlit later
        sys.stdout = original_stdout

    # --- FINAL OUTPUT DISPLAY ---
    st.divider()
    st.success("✅ Mission Accomplished!")
    
    col_res1, col_res2 = st.columns([2, 1])
    
    with col_res1:
        st.subheader("📄 Final Report")
        st.markdown(result)
    
    with col_res2:
        st.subheader("💾 Actions")
        st.download_button(
            label="📥 Download Report",
            data=str(result),
            file_name="agent_mission_report.md",
            mime="text/markdown",
            use_container_width=True
        )
        with st.expander("🛠 Raw Data"):
            st.text(result)