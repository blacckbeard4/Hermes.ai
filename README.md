# HermesAI: Real-Time Streaming Sentiment Analysis

## Introduction & Executive Summary

HermesAI is an intelligent real-time conversation assistant designed to support high-pressure communication scenarios such as customer support calls, business meetings, stakeholder pitches, and internal discussions. Powered by live audio capture and GPT-based natural language processing, HermesAI listens, understands, and provides actionable insights during active conversations — offering next-best response suggestions, emotional tone analysis, and conversation outcome predictions.

The system features a **real-time streaming sentiment analysis pipeline** that delivers:
- Smart, empathetic response generation.
- Instant emotional and intent detection.
- Satisfaction and churn risk prediction.
- Live gamified dashboards to track agent performance and morale.
- Industry-specific customization for SaaS, CPG, B2B, healthcare, finance, and more.

HermesAI aims to transform every communicator into a composed, confident, and effective participant — enabling individuals and teams to handle objections, customer pain points, and high-stress conversations with precision.

---

## Project Materials

- 📄 [Project Code](https://github.com/SITONGRUC/HermesAI/tree/main/project_script)
- 📄 [Streaming Sentiment Analysis Whitepaper (PDF)](https://github.com/SITONGRUC/HermesAI/blob/main/flier.pdf)


---

## Key Features

- **Real-Time Listening:** Seamlessly plug into live calls, meetings, and chats.
- **Emotion & Intent Detection:** Understand emotional cues and customer intent instantly.
- **Smart Suggestions:** Receive next-best-sentence prompts and empathetic guidance during live interactions.
- **Gamified Dashboard:** Drive agent engagement through badges, streaks, and XP points.
- **Customizable Across Industries:** Adapt easily to any sector—SaaS, finance, healthcare, and more.

---

## Team 14 Members
- Jacob Battles
- Justin Varghese
- Anna Niedermeyer
- Sitong Li
- Bhargavi Pissay
- Dharmpalsinh Jhala

---

## 🚀 How to Set Up and Run

### 1. Clone the Repository
```bash
git clone https://github.com/SITONGRUC/HermesAI.git
cd HermesAI
```

### 2. Open in VS Code
- Open the `HermesAI/project_script` project folder using Visual Studio Code (VS Code).

### 3. Install Dependencies
- Create a virtual environment (optional but recommended):
  ```bash
  python -m venv venv
  source venv/bin/activate  # For Mac/Linux
  .\venv\Scripts\activate    # For Windows
  ```
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```

### 4. Add Your OpenAI API Key
- Create a `.env` file in the root folder and add:
  ```
  CHAT_GPT_KEY=your_openai_api_key_here
  ```

### 5. Run the Application
- In the terminal inside VS Code, run:
  ```bash
  streamlit run app.py
  ```

### 6. Access the App
- After running the command, Streamlit will provide a local URL (e.g., `http://localhost:8501`) — open it in your browser.


---



> **This project repository is created in partial fulfillment of the requirements for the Big Data Analytics course offered by the Master of Science in Business Analytics program at the Carlson School of Management, University of Minnesota.**