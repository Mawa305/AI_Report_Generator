# AI Report Generator

A Python-based AI Report Generator that uses the Gemini API to create structured reports from a user-provided topic.

## Features

- Takes a topic from the user
- Generates an AI-powered report using Gemini
- Uses environment variables for API key security
- Handles API errors with try/except
- Saves the report as a TXT file
- Saves structured data as a JSON file

## Technologies Used

- Python
- Gemini API
- Google GenAI SDK
- JSON
- python-dotenv
- Git & GitHub

## Project Flow

User enters a topic  
↓  
Python processes the topic  
↓  
Gemini API generates the report  
↓  
Report is saved as TXT and JSON

## Files

- `app.py` — Main Python application
- `AI_Report.txt` — Generated report
- `AI_Report.json` — Structured report data
- `.gitignore` — Prevents sensitive files from being uploaded

## Security

The Gemini API key is stored in a `.env` file and is excluded from GitHub using `.gitignore`.

**Never share or upload your API key.**

## Example

Input:

```text
AI Automation
