
# Sale Agent with Google ADK

🧠 Overview:
AS-AI is a conversational AI assistant built using Google's Agent Development Kit (ADK), designed to collect user information respectfully and intelligently. It operates with a friendly tone, ensuring a smooth user experience while also handling consent and follow-up logic automatically.

🔧 Key Features:
✅ Lead Collection with Consent

Starts with a warm greeting and asks for consent to collect data.

If the user agrees, AS-AI collects:

Name

Country

Interests

The information is saved in a structured format to a CSV file with a unique lead_id.

✅ Automatic Follow-Up System

If the user declines or doesn’t respond:

AS-AI records partial or no data with status: no.

Triggers a non-blocking async timer to send a follow-up message like “Hi, are you still interested?” after a delay (e.g., 30 seconds).

Ensures other parts of the conversation remain responsive during the wait.

✅ Multi-Agent Architecture

Built with LangGraph-style routing using:

root_agent: Handles greetings and routes messages.

csv_agent: Handles data collection and tool calls.

follow_up_agent: Handles "no" responses and delayed re-engagement.

✅ Tool Integration

csv_tool: Appends collected data into a local CSV file.

start_async_timer: Delays sending a follow-up prompt without blocking the agent.

⚙️ Tech Stack:
Google ADK for agent orchestration

LangGraph-like sub-agent routing

Gemini 1.5 Flash as the core LLM

Python, asyncio, pandas, uuid

CSV file storage for collected data


## Video demo



```bash
  https://drive.google.com/file/d/1FBynenUyUvNrmicMPaFkyiqF_MokqIcA/view?usp=sharing
```
## Activate Env



## Virtaul ENV

Virtaul Env

```bash
  virtualenv env
```
## Activate Env



```bash
  env/Scripts/activate
```    

## Installation

Install Google ADK

```bash
  pip install google-adk
```    

## Installation

Install Pandas

```bash
  pip install pandas
```    

## RUN

Running web interface

```bash
  adk web
```    
## 🚀 About Me
AI Developer

