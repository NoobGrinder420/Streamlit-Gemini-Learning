BuildingBloCS 2025 - Streamlit & Gemini Demos
This repository contains a collection of Streamlit applications and code snippets developed during the 2025 BuildingBloCS June Conference. These demos showcase various functionalities and best practices for building interactive data applications with Streamlit, particularly focusing on integrations with Gemini. The content covers topics discussed throughout the conference, highlighting how to leverage both technologies effectively.

🚀 Features & Highlights
Interactive Dashboards: Examples of dynamic dashboards for data exploration.

Data Visualization: Custom visualizations using Streamlit's charting capabilities and integration with libraries like Plotly, Matplotlib, or Altair.

Machine Learning Demos: Simple ML model deployments and inference UIs.

Component Usage: Demonstrations of various Streamlit widgets and components (sliders, buttons, text inputs, etc.).

Session State Management: Examples of managing application state effectively.

Gemini API Integrations: Demonstrations of calling the Gemini API within Streamlit apps for text generation, image understanding, or structured responses.

Deployment Ready: Code structured with deployment in mind (e.g., on Streamlit Cloud).

🛠️ Installation & Usage
To run these Streamlit applications locally, follow these steps:

Clone the repository:

git clone https://github.com/NoobGrinder420/BBCS-2025-Streamlit-and-Gemini-code.git
cd BBCS-2025-Streamlit-and-Gemini-code

Create a virtual environment (recommended):

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

Install the required dependencies:

pip install streamlit pandas numpy google-generativeai python-dotenv

After running your apps, you can generate a requirements.txt file using pip freeze > requirements.txt.

Run a specific Streamlit application:

Navigate to the directory containing the app you want to run and execute:

streamlit run your_app_name.py

Replace your_app_name.py with the actual filename of the Streamlit application you wish to launch.

The app will open in your default web browser (usually at http://localhost:8501).

📁 Project Structure
.
├── 01_Text/              # Demonstrations related to text manipulation and display
├── 02_Pages/             # Examples of multi-page Streamlit applications
├── 03_Media/             # Demos involving images, audio, and video
├── 04_Widgets/           # Examples showcasing various Streamlit widgets
├── 05_Data/              # Applications focusing on data handling and display
├── 06_Layout/            # Demos illustrating different layout options in Streamlit
├── 07_Sessions/          # Examples of Streamlit session state management
├── 08_LLM_Integration/   # Integrations with Large Language Models (Gemini)
├── 10_Tutor_Bot_Full/    # A complete end-to-end tutor bot application
├── .gitignore
├── README.md             # This file
└── requirements.txt      # Python dependencies

