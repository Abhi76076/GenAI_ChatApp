# 🧠 GenAI Chat App (with Search Tool)

This is a simple **Streamlit web app** that interacts with Google's Generative AI using the **Gemini 2.0 Flash** model and the **Google Search tool** for real-time data.

---

## ✨ Features

- Gemini 2.0 Flash Model  
- Google Search tool integration (via GenAI tools)  
- Clean browser-based UI (built with Streamlit)  
- Works locally and easy to deploy  

---

## 🚀 Setup Instructions (Windows)

### 1. 📦 Clone the Repository

Download or clone the repo to your machine:

```bash
git clone https://github.com/Abhi76076/GenAI_ChatApp
cd genai
```
2. 🐍 Create Virtual Environment
bash
```bash
python -m venv
```
3. ✅ Activate the Virtual Environment (PowerShell)
```bash
.\venv\Scripts\Activate
```
4. 📥 Install Dependencies
```bash
pip install -r requirements.txt
```
# 5. 🔐 Set Your API Key Securely
- rename example.secrets.toml file as secrets.toml
- Add your Google API key to 
- GOOGLE_API_KEY = "your-real-api-key"
- Alternatively, you can set it as an environment variable:

- set GOOGLE_API_KEY=your-real-api-key  # Windows cmd
- $env:GOOGLE_API_KEY="your-real-api-key"  # PowerShell

# 6. 🛠 If you encounter errors with the GenAI package, try upgrading:
```bash
pip install --upgrade google-generativeai
```
# 7. 🧠 Run the Streamlit App
```bash
streamlit run app.py
```