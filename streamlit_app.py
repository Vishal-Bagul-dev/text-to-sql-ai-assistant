import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
import mysql.connector
import pandas as pd

load_dotenv()

# Gemini client
gemini_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_key)

# Database schema
schema = """
Table name: employees
Columns: EmployeeNumber, Age, Attrition (Yes/No), BusinessTravel, DailyRate,
Department, DistanceFromHome, Education, EducationField, EmployeeCount,
EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel,
JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate,
NumCompaniesWorked, Over18, OverTime (Yes/No), PercentSalaryHike,
PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel,
TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany,
YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager
"""

# Page setup
st.set_page_config(page_title="Text-to-SQL AI Assistant", page_icon="🤖", layout="centered")
st.title("🤖 Text-to-SQL AI Assistant")
st.write("Ask questions about employee data in plain English — AI will convert it to SQL and fetch the answer.")

# Input box
user_question = st.text_input("Ask your question:", placeholder="e.g. Which department has the highest attrition rate?")

if st.button("Get Answer") and user_question:
    with st.spinner("AI is thinking..."):
        prompt = f"""
You are a MySQL expert. Given this table schema:
{schema}

Convert this question into a single valid MySQL SQL query.
Question: {user_question}

Rules:
- Return ONLY the SQL query, nothing else
- No explanation, no markdown, no ```sql``` formatting
- Just the raw SQL query ending with a semicolon
"""
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )
            sql_query = response.text.strip()

            st.subheader("Generated SQL")
            st.code(sql_query, language="sql")

            connection = mysql.connector.connect(
             host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
            )
            cursor = connection.cursor()
            cursor.execute(sql_query)
            results = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            cursor.close()
            connection.close()

            st.subheader("Result")
            df = pd.DataFrame(results, columns=column_names)
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(f"Error: {e}")