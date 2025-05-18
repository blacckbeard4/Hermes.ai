import json
from openai import OpenAI
import os
api_key = os.getenv("CHAT_GPT_KEY")

def analyze(message, api_key, model="gpt-4o-mini", temperature=0):
    system_message = """
    You are a highly accurate customer service assistant.

    Given a single message from a customer service dialogue, fill out the following fields in JSON format. Do not add any explanation.

    Return this structure:
    {
      "Issue Classification": "<category like 'Delivery Delayed', 'Return Processing', etc.>",
      "Possible Solutions": "<concise proposed solution, e.g., 'issue refund', 'resend item'>",
      "Next sentence to say": "<what the agent should say next>",
      "Avg Waiting time": <estimated wait time in minutes (integer)>,
      "Avg call time": <expected total call time in minutes (integer)>,
      "Predicted time to fix": <how many minutes it will take to resolve the issue (integer)>,
      "Forecasted Rating": <estimated satisfaction score from 1.0 to 5.0 (float)>,
      "Customer Emotion": "<emoji representing the customer's emotional state>"
    }
    The response must be valid JSON.
    """

    client = OpenAI(api_key=api_key)
    messages = [{"role": "system", "content": system_message},
                {"role": "user", "content": message}]
    
    try:
        response = client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=temperature
        )
        content = response.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        print("Error:", e)
        return {
            "Issue Classification": "N/A",
            "Possible Solutions": "N/A",
            "Next sentence to say": "Sorry, I’m having trouble understanding.",
            "Avg Waiting time": 0,
            "Avg call time": 0,
            "Predicted time to fix": 0,
            "Forecasted Rating": 3.0,
            "Customer Emotion": "🤖"
        }

def analyze_text(message):
    return analyze(message, api_key=api_key)