import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def analyze_test_results():
    with open('build/result.log', 'r') as file:
        test_results = file.read()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"테스트 결과를 분석하고 피드백을 제공합니다: {test_results}"}
        ]
    )

    feedback = response.choices[0].message['content'].strip() 
    with open('feedback.log', 'w') as file:
        file.write(feedback)

if __name__ == "__main__":
    analyze_test_results()
