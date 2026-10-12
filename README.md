# AI SDLC Assistant

An AI-powered application that transforms software requirements written in natural language into structured Software Development Life Cycle (SDLC) planning outputs.

## Overview

Planning software development requires understanding requirements, identifying features, creating user stories, preparing development tasks, and defining test cases.

The AI SDLC Assistant uses Google's Gemini API to help organize this information into a structured plan.

## Features

- **Functional Requirements:** Identifies the main features the software should provide.
- **Non-Functional Requirements:** Suggests performance, security, reliability, scalability, and usability requirements.
- **User Stories:** Generates user stories in the format "As a [user], I want [feature], so that [benefit]."
- **Development Tasks:** Suggests practical tasks for developers.
- **Test Cases:** Generates test scenarios and expected results.
- **Potential Risks:** Identifies possible technical and business risks.
- **Structured Output:** Uses JSON to organize the generated information into separate sections.
- **Error Handling:** Displays user-friendly messages for certain API and response-format errors.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI Python SDK
- JSON
- python-dotenv

## How It Works

1. The user enters a software requirement.
2. Python inserts the requirement into a structured prompt.
3. The Gemini API generates the requested SDLC artifacts in JSON format.
4. Python parses the JSON response.
5. Streamlit displays each section separately.

## Project Structure

```text
AI-SDLC-Assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

The `.env` file contains the local API key and is intentionally excluded from version control.

## Setup and Installation

### Prerequisites

- Python installed
- A Google Gemini API key
- Internet access for API requests

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the example values with your actual repository URL and folder name.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a local `.env` file in the project root:

```text
GEMINI_API_KEY=your_actual_api_key
```

Use your own valid Gemini API key. Never commit the `.env` file.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## Example Use Case

**Input:** Build an online food delivery application with customer registration, restaurant browsing, online payment, and delivery tracking.

**Expected outputs:**
- Functional and non-functional requirements
- User stories
- Development tasks
- Test cases
- Potential risks

The exact output depends on the requirement and the model response.

## Limitations

- Generated plans may contain incomplete or incorrect assumptions.
- Requirements and test cases should be reviewed by a human before implementation.
- The application depends on API availability, valid credentials, and network connectivity.
- Generated output may occasionally fail JSON parsing and require another attempt.

## Future Improvements

- Export generated plans to PDF or CSV.
- Add downloadable test cases and user stories.
- Allow users to edit and regenerate individual sections.
- Add project-specific templates and persistent history.
- Introduce automated validation of generated requirements.

## Learning Outcomes

This project provided practical experience with API integration, prompt engineering, structured JSON output, Python exception handling, and building interactive applications with Streamlit.

## Disclaimer

This is an educational prototype intended to assist with software planning. Its outputs should be reviewed before being used in a real software development project.