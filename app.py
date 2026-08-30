from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def generate_report(topic):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"""
Write a short report about {topic}.

Include:
1. Introduction
2. Main points
3. Benefits
4. Conclusion

Use simple and clear language.
"""
        )

        return response.text

    except Exception as e:
        print("Something went wrong:", e)
        return None

def save_report(topic, report):
    with open("AI_Report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    report_data = {
        "topic": topic,
        "report": report
    }

    with open("AI_Report.json", "w", encoding="utf-8") as file:
        json.dump(report_data, file, indent=4)

    print("Report saved successfully!")
    print("JSON report saved successfully!")

def main():
    topic = input("Enter a topic: ")

    report = generate_report(topic)

    if report:
        save_report(topic, report)


if __name__ == "__main__":
    main()