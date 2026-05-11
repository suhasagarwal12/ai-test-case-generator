# AI-Powered Test Case Generator Using Ollama

> Generate high-quality software test cases automatically using a local Large Language Model (LLM) powered by Ollama and Llama 3.2 — with zero API cost.

## 📌 Overview

This project demonstrates how Generative AI can be applied to software quality engineering by automatically generating structured test cases from user stories, requirements, or feature descriptions.

The application uses:

- **Ollama** for local LLM inference
- **Llama 3.2** as the underlying language model
- **Streamlit** for an interactive web interface
- **Pytest** for unit testing
- **Pandas/OpenPyXL** for Excel export
- **Jira/Xray APIs** for enterprise test management integration
- **Python3** for backend logic and response parsing

This solution runs entirely on your local machine, ensuring:

- ✅ Zero API cost
- ✅ Full data privacy
- ✅ Offline capability
- ✅ Fast experimentation with prompt engineering
---

## 🎯 Key Features

### 🧠 AI-Powered Test Case Generation
- Generate test cases from plain English requirements
- Select the number of test cases (1–50)
- Choose test types:
  - Functional
  - API
  - UI
  - Regression
  - Security
  - Performance

### 🧪 Advanced Test Coverage Options
- Boundary Value Cases
- Negative Scenarios
- Validation Checks

### 📥 Export Capabilities
- Download results as Excel (`.xlsx`)
- Download results as Markdown (`.md`)

### 🔗 Enterprise Integration
- Create Test issues directly in Jira/Xray

### 🧰 Engineering Best Practices
- Modular Python architecture
- Robust error handling
- Unit tests with Pytest

---

## 🏗️ Architecture

```text
User Requirement
       │
       ▼
Streamlit Web UI
       │
       ▼
Prompt Builder
       │
       ▼
Ollama Local API
       │
       ▼
Llama 3.2 Model
       │
       ▼
Generated Markdown
       │
       ├── Excel Export (.xlsx)
       ├── Markdown Export (.md)
       └── Jira/Xray Integration

## Project Structure

ai-test-case-generator/
├── src/
├── prompts/
├── samples/
├── tests/
├── output/
├── requirements.txt
├── README.md
└── .gitignore
├── app.py

## 🚀 Installation

1. Clone the Repository : git clone https://github.com/suhasagarwal112/ai-test-case-generator.git
cd ai-test-case-generator
2. Create Virtual Environment : python -m venv venv
3. Activate Virtual Environment : venv\Scripts\activate
4. Install Dependencies : pip install -r requirements.txt
5. Install Ollama : Download from: https://ollama.com/download
6. Pull and Start the Model : ollama run llama3.2
7. Launch the Application : python -m streamlit run app.py

If cases needs to be generated locally without launching web ui then use : python -m src.cli -f samples/login_requirement.txt
** login_requirement.txt contains sample scenario with acceptance criteria to generate cases via ollama integration

🧪 Running Unit Tests : python -m pytest -v

## Example requirement : 
As a banking customer, I should be able to transfer funds between accounts so that I can manage my money efficiently.

## Example Output
Positive transfer scenario
Insufficient balance validation
Invalid account number check
Zero amount boundary case
Daily transfer limit exceeded

## 📥 Export Outputs

The application allows users to download generated results as:

generated_test_cases.xlsx
generated_test_cases.md
🔗 Jira/Xray Integration

The src/jira_xray.py module enables automated creation of Test issues in Jira/Xray.

### Typical use cases:
Create AI-generated test cases directly in enterprise test management systems
Accelerate test design workflows
Reduce manual effort

## 📈 Future Enhancements
1. AI Failure Analyser
2.a GitHub Actions CI workflow
2.b DockerFile
2.c Multi-model support
3.a Jira credential UI in Streamlit
3.b Xray step-level import
4.a Playwright script generation
4.b Test data generation
4.c Prompt versioning
5.a FastAPI REST API
5.b RAG with domain knowledge

## Author
Suhas Agarwal
