import uuid
import os
import pandas as pd

def generate_lead_id():
    """
    Generates a random lead_id.
    
    Returns:
        A unique lead_id integer.
    """
    return int(str(uuid.uuid4().int)[:8])


def csv_tool(lead_id: int, name: str = "", country: str = "", intrest: str = "", status: str = "") -> str:
    """
    Appends a person's name, country, interest, and status to a CSV file.

    Args:
        lead_id: Unique lead ID.
        name: The person's name (optional).
        country: The person's country (optional).
        intrest: The person's interest (optional).
        status: Status ("done" or "no").

    Returns:
        A success or error message.
    """
    try:
        global CSV_FILE_PATH

        #  file exists 
        file_exists = os.path.isfile(CSV_FILE_PATH)

        # status is "done" or "no"
        if status not in ["done", "no"]:
            return f"Invalid status '{status}'. Only 'done' or 'no' allowed."

       
        if not lead_id:
            return "lead_id is required."

        # save the row
        columns = ['lead_id', 'name', 'country', 'intrest', 'status']
        df = pd.DataFrame([[lead_id, name, country, intrest, status]], columns=columns)

        df.to_csv(CSV_FILE_PATH, mode='a', header=not file_exists, index=False)
        return f"Saved: lead_id={lead_id}, name='{name}', country='{country}', intrest='{intrest}', status='{status}'"
    
    except Exception as e:
        return f"Error saving to CSV: {str(e)}"

CURRENT_LEAD_ID = generate_lead_id()

prompt = f"""

You are AS-AI, a friendly assistant helping us collect basic user information for our records. Please follow these guidelines to ensure a smooth and respectful experience:

1. Friendly Introduction & Consent Request      
2. If the User Agrees to Share Info (Says "Yes")
   - Ask three simple questions:
       a) “What is your name?”
       b) “Which country are you from?”
       c) “What are your interests?”
   - Wait for all three answers.
   - Once all responses are collected:
       - Call the tool `csv_tool` and add a new row with:
           - lead_id: {CURRENT_LEAD_ID}
           - name: [User's name]
           - country: [User's country]
           - interest: [User's interest]
           - status: "done"


4. Communication Style
   - Be friendly, approachable, and polite throughout the interaction.
   - Use simple language. Avoid technical or complex terms.
   - Keep the tone respectful—never pressure the user.

5. System Boundaries
   - Do not disclose internal tools, data processes, or file names.
   - Focus only on collecting user name, country, and interest.
   - Do not ask for sensitive or personal data beyond what’s specified.

— 


### Communication Style

- **Tone**: Friendly, respectful, and conversational.
- **Style**: Clear, natural, and easy to understand.

---

### Data Entry Format
Tool Used: `csv_tool`

Captured Columns:
- {CURRENT_LEAD_ID}
- name
- country
- interest
- status (either "done" or "no")


This assistant helps gently collect optional data while respecting user preferences.
"""



prompt2 = f""" 

give resposne to user :
   - “Just checking in—are you still interested?”
   - If the user replies “Yes” again, re-ask any unanswered questions.
   - If the user replies “No” or doesn’t respond again:
       a) Say: “Alright, no worries!”
       b) Call the tool `csv_tool` and add a new row:
           - lead_id: {CURRENT_LEAD_ID}
           - name: [whatever is provided or leave blank]
           - country: [whatever is provided or leave blank]
           - interest: [whatever is provided or leave blank]
           - status: "no" 

       c) if user say no i dont like to share information 
            must call this tool start_async_timer 
            give response after tool call end not before tool call end  
            and give resposne follow up "hi are you still intrested"


ensures follow-ups, and respects the user's choice at every step.

"""


import time
def trigger_follow_up(callback_id: str, delay_seconds: int):
    time.sleep(delay_seconds)
    return f"[Follow-Up Triggered] Lead ID: {callback_id} — Just checking in—are you still interested?"


import asyncio

def start_async_timer(callback_id: str, delay_seconds: int = 30) -> str:
    """
    Starts an async timer and triggers a follow-up callback after delay.
    
    Args:
        callback_id: A unique identifier for the follow-up (like lead_id).
        delay_seconds: Time to wait before triggering the callback (default 30).
    
    Returns:
        A confirmation message that the timer has started.
    """
    try:
        asyncio.create_task(trigger_follow_up(callback_id, delay_seconds))
        return f"Timer started for {delay_seconds} seconds for lead_id: {callback_id}"
    except Exception as e:
        return f"Failed to start timer: {str(e)}"
    


