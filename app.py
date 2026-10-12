import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="AI SDLC Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI SDLC Assistant")

st.write(
    "Convert software requirements into structured SDLC outputs using Generative AI."
)

# User input
requirement = st.text_area(
    "Enter your software requirement:",
    placeholder=(
        "Example: Build an online food delivery application "
        "with customer registration, restaurant browsing, "
        "online payment and delivery tracking."
    ),
    height=150
)

# Generate button
if st.button("🚀 Generate SDLC Plan"):

    if requirement.strip() == "":
        st.warning("Please enter a software requirement.")

    else:

        # Prompt for Gemini
        prompt = f"""
You are an experienced software analyst and software architect.

Analyze this software requirement:

{requirement}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "functional_requirements": [],
    "non_functional_requirements": [],
    "user_stories": [],
    "development_tasks": [],
    "test_cases": [],
    "risks": []
}}

Instructions:

- functional_requirements:
  List the main features the system must provide.

- non_functional_requirements:
  Include performance, security, scalability, reliability or usability requirements.

- user_stories:
  Write user stories using:
  "As a [user], I want [feature], so that [benefit]."

- development_tasks:
  Give practical tasks that developers need to perform.

- test_cases:
  Give clear test cases with what should be tested and the expected result.

- risks:
  List realistic technical or business risks.

Keep every item concise and practical.
Do not add markdown.
Do not add explanations outside the JSON.
"""

        # Call Gemini
        with st.spinner("🤖 Generating SDLC plan..."):

            try:

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                # Convert Gemini response into Python dictionary
                result_text = response.text.strip()

                # Remove possible markdown code fences
                if result_text.startswith("```"):
                    result_text = result_text.replace("```json", "")
                    result_text = result_text.replace("```", "")
                    result_text = result_text.strip()

                data = json.loads(result_text)

                # Display results
                st.success("SDLC plan generated successfully!")

                st.subheader("📋 Functional Requirements")

                for item in data["functional_requirements"]:
                    st.write("• " + item)

                st.subheader("⚙️ Non-Functional Requirements")

                for item in data["non_functional_requirements"]:
                    st.write("• " + item)

                st.subheader("👤 User Stories")

                for item in data["user_stories"]:
                    st.write("• " + item)

                st.subheader("💻 Development Tasks")

                for item in data["development_tasks"]:
                    st.write("• " + item)

                st.subheader("🧪 Test Cases")

                for item in data["test_cases"]:
                    st.write("• " + item)

                st.subheader("⚠️ Potential Risks")

                for item in data["risks"]:
                    st.write("• " + item)

            except json.JSONDecodeError:

                st.error(
                    "The AI returned an unexpected format. Please try again."
                )

            except Exception as e:

                error_message = str(e)

                if "503" in error_message or "UNAVAILABLE" in error_message:
                    st.warning(
                        "Gemini is temporarily busy. "
                        "Please try again in a few seconds."
                    )

                else:
                    st.error(
                        "Something went wrong while communicating with Gemini."
                    )
                    st.write(f"Error: {e}")