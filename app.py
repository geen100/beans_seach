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
            
            beans_info = "以下は利用可能な豆のリストである:\n"
            for bean in beans_data:
                beans_info += f"name: {bean.get('name', 'N/A')}, Details: {bean.get('Details', 'N/A')}\n"

            prompt_with_context = (
                "あなたはタリーズの店員です。以下のビーンズ情報を使って、ユーザーの質問に答えてください.\n"
                f"{beans_info}\n\n"
                f"User's question: {prompt}"
            )
            
            
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは役に立つん店員である。"},
                    {"role": "user", "content": prompt_with_context}
                ]
            )

            beans = completion.choices[0].message.content
        else:
            beans = "メッセージを入力してください"

    return render_template('index.html', beans=beans)

if __name__ == '__main__':
    app.run(debug=True)










