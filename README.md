import streamlit as st
import os
import sys
import time
import re
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# 1️⃣ PAGE CONFIGURATION
st.set_page_config(
    page_title="AI Agent Crew",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for the Terminal Look
st.markdown("""
<style>
    .stTextArea textarea {
        background-color: #000000;
        color: #00FF00;
        font-family: 'Courier New', Courier, monospace;
    }
</style>
""", unsafe_allow_html=True)

# 2️⃣ HELPER CLASS: REDIRECT STDOUT TO STREAMLIT
class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

    def write(self, data):
        # Clean ANSI color codes for Streamlit display
        clean_data = self.colors.sub('', data)
        self.buffer.append(clean_data)
        # Update the container with the latest lines
        self.expander.code("".join(self.buffer), language='text')

    def flush(self):
        pass

# 3️⃣ SIDEBAR - CONFIGURATION
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/8637/8637102.png", width=100)
    st.header("⚙️ Configuration")
    
    api_key = st.text_input(
        "Enter Gemini API Key", 
        type="password", 
        help="Get your key from Google AI Studio"
    )
    
    st.divider()
    
    st.markdown("### 👥 The Crew")
    st.markdown("1. **Planner**: Strategies")
    st.markdown("2. **Researcher**: Facts")
    st.markdown("3. **Writer**: Content")
    st.markdown("4. **Reviewer**: Quality")
    
    st.divider()
    st.info("Built with CrewAI & Streamlit")

# 4️⃣ MAIN UI LAYOUT
st.title("🤖 AI Content Production Crew")
st.markdown("""
**Welcome to your automated content team.** Describe your goal below, and our multi-agent system will plan, research, write, and review it for you.
""")

# User Input
user_input = st.text_area("✍️ What should the crew work on?", placeholder="E.g., Write a comprehensive guide on the future of electric vehicles in 2025.")

# Run Button
if st.button("🚀 Kickoff Crew"):
    if not api_key:
        st.error("❌ Please enter your Google API Key in the sidebar to proceed.")
        st.stop()
    
    if not user_input:
        st.warning("⚠️ Please enter a topic or goal.")
        st.stop()

    # 5️⃣ AGENT SETUP (Hidden from UI until running)
    os.environ["GOOGLE_API_KEY"] = api_key
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        verbose=True,
        temperature=0.5,
        google_api_key=api_key
    )

    # Agents
    planner = Agent(
        role="Planner",
        goal="Break the user goal into actionable steps",
        backstory="Expert project manager who organizes chaos into clarity.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )

    researcher = Agent(
        role="Researcher",
        goal="Find accurate facts and data",
        backstory="Tech-savvy analyst who loves digging into details.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )

    writer = Agent(
        role="Writer",
        goal="Write compelling content",
        backstory="Creative writer who transforms facts into engaging stories.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )

    reviewer = Agent(
        role="Reviewer",
        goal="Polish the final content",
        backstory="Strict editor who ensures perfection and clarity.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )

    # Tasks
    task1 = Task(
        description=f"Plan the content structure for: '{user_input}'. Create a detailed outline.",
        expected_output="A bulleted list of section headers and key points.",
        agent=planner
    )

    task2 = Task(
        description="Research the planned topics. Provide stats, facts, and key information.",
        expected_output="A comprehensive text document with verified facts.",
        agent=researcher
    )

    task3 = Task(
        description="Write the full article based on the research. Use markdown formatting.",
        expected_output="A professional blog post/article in markdown.",
        agent=writer
    )

    task4 = Task(
        description="Review the article for flow, grammar, and tone. Make final edits.",
        expected_output="The final polished markdown article.",
        agent=reviewer
    )

    crew = Crew(
        agents=[planner, researcher, writer, reviewer],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential
    )

    # 6️⃣ LIVE EXECUTION LOG
    st.divider()
    st.subheader("🖥️ Live Execution Log")
    
    # We create a placeholder for the logs
    log_expander = st.expander("View Agent Thoughts & Actions", expanded=True)
    log_placeholder = log_expander.empty()
    
    # Redirect stdout to our custom class
    sys.stdout = StreamToExpander(log_placeholder)

    try:
        with st.spinner('🤖 Agents are working... Check the logs below!'):
            result = crew.kickoff()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        # Restore stdout in case of error
        sys.stdout = sys.__stdout__
        st.stop()

    # Restore stdout
    sys.stdout = sys.__stdout__

    # 7️⃣ DISPLAY FINAL RESULTS
    st.success("✅ Mission Accomplished!")
    
    st.divider()
    st.subheader("📄 Final Output")
    
    tab1, tab2 = st.tabs(["📝 Formatted Report", "🛠 Raw Output"])
    
    with tab1:
        st.markdown(result)
        
    with tab2:
        st.code(result)

    st.download_button(
        label="📥 Download Report",
        data=str(result),
        file_name="agent_report.md",
        mime="text/markdown"
    )