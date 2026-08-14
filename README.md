# 🤖 Text-to-SQL AI Assistant

🔗 **[Live Demo](https://text-to-sql-ai-assistant-bfiymvscvasjlvty8pqj7v.streamlit.app/)**
An AI-powered tool that converts plain English questions into SQL queries and fetches answers from a MySQL database in real-time — no SQL knowledge required to query the data.

## 🎯 Problem it Solves
Business users and analysts often need quick answers from data but don't know SQL. This tool bridges that gap using Google's Gemini AI to translate natural language questions into accurate SQL queries, executed instantly against a live database.

## 🛠️ Tech Stack
- **Python** — core application logic
- **Google Gemini API (gemini-3.6-flash)** — natural language to SQL conversion
- **MySQL** — database backend
- **Streamlit** — interactive web interface
- **Pandas** — result formatting

## ✨ Features
- Ask questions in plain English (e.g. "Which department has the highest attrition rate?")
- AI generates accurate MySQL queries automatically
- Real-time query execution against a live database
- Clean, interactive web UI with syntax-highlighted SQL and sortable result tables
- Error handling for invalid or ambiguous questions

## 📊 Dataset
Uses the IBM HR Analytics Employee Attrition dataset (1,470 employees, 34 attributes) — the same dataset from my [HR Employee Attrition Analysis](https://github.com/Vishal-Bagul-dev/hr-employee-attrition-analysis) project.

## 🚀 How It Works
1. User asks a question in plain English via the web interface
2. The question + database schema is sent to Gemini AI
3. Gemini generates a valid MySQL query
4. The query executes against the MySQL database
5. Results are displayed in an interactive table

## 📷 Screenshots
*(Add your Streamlit screenshots here)*

## ⚙️ Setup Instructions
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file (see `.env.example`) with your Gemini API key and MySQL credentials
4. Run the web app: `streamlit run streamlit_app.py`

## 🔮 Future Improvements
- Support for more complex multi-table queries
- Query history/chat memory
- Voice input support

## 👤 Author
**Vishal Bagul**
- GitHub: [Vishal-Bagul-dev](https://github.com/Vishal-Bagul-dev)
- LinkedIn: [vishal-bagul-b47701222](https://linkedin.com/in/vishal-bagul-b47701222)