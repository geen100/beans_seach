import requests
from openai import OpenAI
from flask import Flask, render_template, request

client = OpenAI()

app = Flask(__name__)

sheet_db = 'https://sheetdb.io/api/v1/ojb9x97cdlf9k'


@app.route('/', methods=['GET', 'POST'])
def home():
    beans = None

    if request.method == 'POST':
        prompt = request.form['prompt']
        
        response = requests.get(sheet_db)
        if response.status_code == 200:
            beans_data = response.json()
            
            beans_info = "Here is the list of available beans:\n"
            for bean in beans_data:
                beans_info += f"name: {bean.get('name', 'N/A')}, Details: {bean.get('Details', 'N/A')}\n"

            prompt_with_context = (
                "You are a Tully's clerk. Please use the following beans information to answer the user's question.\n\n"
                f"{beans_info}\n\n"
                f"User's question: {prompt}"
            )
            
            
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt_with_context}
                ]
            )

            beans = completion.choices[0].message.content
        else:
            beans = "Failed to retrieve beans data from the sheet"

    return render_template('index.html', beans=beans)

if __name__ == '__main__':
    app.run(debug=False)










