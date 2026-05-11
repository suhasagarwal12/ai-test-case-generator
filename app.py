import requests
import streamlit as st

from src.exporter import to_excel, to_markdown

# -----------------------------------------------------------------------------
# Streamlit Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="AI-Based Test Case Generator",
    page_icon="🤖",
    layout="wide",
)

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
st.title("🤖 AI-Based Test Case Generator")
st.caption(
    "Generate structured software test cases locally using Ollama and Llama 3.2."
)

# -----------------------------------------------------------------------------
# Sidebar Configuration
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Generation Settings")

    model_name = st.text_input(
        "Ollama Model",
        value="llama3.2",
        help="Any model available in your local Ollama installation.",
    )

    num_cases = st.number_input(
        "Number of Test Cases",
        min_value=1,
        max_value=50,
        value=10,
        step=1,
        help="Recommended range: 5–20 for best results.",
    )

    test_type = st.selectbox(
        "Test Type",
        [
            "Functional",
            "API",
            "UI",
            "Regression",
            "Security",
            "Performance",
        ],
    )

    include_boundary = st.checkbox("Include Boundary Value Cases", value=True)
    include_negative = st.checkbox("Include Negative Scenarios", value=True)
    include_validation = st.checkbox("Include Validation Checks", value=True)

# -----------------------------------------------------------------------------
# Main Input
# -----------------------------------------------------------------------------
requirement = st.text_area(
    "📝 Enter Requirement / User Story",
    value=(
        "As a banking customer, I should be able to transfer funds between "
        "accounts so that I can manage my money efficiently."
    ),
    height=180,
)

# -----------------------------------------------------------------------------
# Prompt Builder
# -----------------------------------------------------------------------------
def build_prompt(
    requirement_text: str,
    case_count: int,
    selected_test_type: str,
    boundary: bool,
    negative: bool,
    validation: bool,
) -> str:
    scenario_types = []

    if boundary:
        scenario_types.append("Boundary Value Cases")
    if negative:
        scenario_types.append("Negative Scenarios")
    if validation:
        scenario_types.append("Validation Checks")

    scenario_section = ""
    if scenario_types:
        scenario_section = (
            "\nInclude a balanced mix of the following scenario categories:\n- "
            + "\n- ".join(scenario_types)
        )

    return f"""
Generate {case_count} detailed {selected_test_type} test cases for the following requirement.

Requirement:
{requirement_text}

For each test case include:
1. Test Case ID
2. Scenario
3. Preconditions
4. Steps
5. Expected Result
6. Priority
7. Severity

{scenario_section}

Format the response in clean Markdown using headings and bullet points.
"""


# -----------------------------------------------------------------------------
# Ollama API Call
# -----------------------------------------------------------------------------
def generate_test_cases(prompt: str, model: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
        },
        timeout=300,
    )

    response.raise_for_status()
    data = response.json()
    return data.get("response", "").strip()


# -----------------------------------------------------------------------------
# Main Action
# -----------------------------------------------------------------------------
if st.button("🚀 Generate Test Cases", type="primary"):
    if not requirement.strip():
        st.warning("Please enter a requirement or user story.")
        st.stop()

    prompt = build_prompt(
        requirement_text=requirement,
        case_count=num_cases,
        selected_test_type=test_type,
        boundary=include_boundary,
        negative=include_negative,
        validation=include_validation,
    )

    with st.expander("🧠 Generated Prompt", expanded=False):
        st.code(prompt)

    try:
        with st.spinner(
            f"Generating {num_cases} {test_type.lower()} test cases using {model_name}..."
        ):
            result = generate_test_cases(prompt, model_name)

        if not result:
            st.error("The model returned an empty response.")
            st.stop()

        st.success("✅ Test cases generated successfully!")

        # ---------------------------------------------------------------------
        # Display Generated Output
        # ---------------------------------------------------------------------
        st.subheader("📋 Generated Test Cases")
        st.markdown(result)

        # ---------------------------------------------------------------------
        # Export Section
        # ---------------------------------------------------------------------
        st.subheader("📥 Download Results")

        excel_data = to_excel(result)
        markdown_data = to_markdown(result)

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="📊 Download Excel",
                data=excel_data,
                file_name="generated_test_cases.xlsx",
                mime=(
                    "application/vnd.openxmlformats-officedocument."
                    "spreadsheetml.sheet"
                ),
            )

        with col2:
            st.download_button(
                label="📝 Download Markdown",
                data=markdown_data,
                file_name="generated_test_cases.md",
                mime="text/markdown",
            )

        # ---------------------------------------------------------------------
        # Jira/Xray Placeholder
        # ---------------------------------------------------------------------
        st.subheader("🔗 Jira / Xray Integration")
        st.info(
            "Jira/Xray integration module is ready. "
            "You can connect this output to Jira Test issues using "
            "src/jira_xray.py."
        )

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Unable to connect to Ollama.\n\n"
            "Please ensure Ollama is installed and running.\n\n"
            "Start it in another terminal using:\n\n"
            "    ollama run llama3.2"
        )

    except requests.exceptions.Timeout:
        st.error(
            "⏱️ The request timed out. "
            "Try reducing the number of test cases or using a smaller model."
        )

    except requests.exceptions.HTTPError as e:
        st.error(f"🌐 HTTP error while calling Ollama: {e}")

    except Exception as e:
        st.error(f"⚠️ Unexpected error: {e}")

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.divider()
st.caption(
    "Built with Streamlit, Ollama, Llama 3.2, and Python for AI-assisted "
    "software quality engineering."
)