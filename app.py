from google import genai
from dotenv import load_dotenv
import os
import mysql.connector
from tabulate import tabulate

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_key)

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = connection.cursor()

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

print("=== Text-to-SQL AI Assistant ===")
print("Type 'exit' to quit\n")

while True:
    user_question = input("Apna sawaal poochho: ")

    if user_question.lower() == "exit":
        print("Dhanyavaad! Band kar rahe hain...")
        break

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
        print("\nGenerated SQL:", sql_query)

        cursor.execute(sql_query)
        results = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        print("\nResult:")
        print(tabulate(results, headers=column_names, tablefmt="grid"))
        print()

    except Exception as e:
        print("Error aaya:", e)
        print("Zara sawaal ko different tarike se poochho.\n")

cursor.close()
connection.close()