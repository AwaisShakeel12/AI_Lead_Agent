import os
import pandas as pd
from dotenv import load_dotenv
import uuid

CSV_FILE_PATH = r'E:\Gen_AI2\git\AI_Lead_Agent\first\lead.csv'

def generate_lead_id() -> str:
    """Generates a new random lead ID as string."""
    return str(uuid.uuid4().int)[:8]

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
        # is file exists 
        file_exists = os.path.isfile(CSV_FILE_PATH)

        # status is either "done" or "no"
        if status not in ["done", "no"]:
            return f"Invalid status '{status}'. Only 'done' or 'no' allowed."

        # is lead_id is present
        if not lead_id:
            return "lead_id is required."

        #  save the row
        columns = ['lead_id', 'name', 'country', 'intrest', 'status']
        df = pd.DataFrame([[lead_id, name, country, intrest, status]], columns=columns)

        df.to_csv(CSV_FILE_PATH, mode='a', header=not file_exists, index=False)
        return f"✅ Saved: lead_id={lead_id}, name='{name}', country='{country}', intrest='{intrest}', status='{status}'"
    
    except Exception as e:
        return f"Error saving to CSV: {str(e)}"

import time
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
    






