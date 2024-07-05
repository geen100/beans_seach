
from openai import OpenAI
from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

sheet_db = 'https://sheetdb.io/api/v1/ojb9x97cdlf9k'


@app.route('/', methods=['GET', 'POST'])
def home():
    beans = None

    if request.method == 'POST':
        prompt = request.form['prompt']

        completion = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Tully's clerk. Please use the following spread sheet to answer the following questions about beans"},
            {"role": "user", "content": prompt}
        ])

        # 返答を取得
        beans = completion.choices[0].message.content

    return render_template('index.html', beans=beans)

if __name__ == '__main__':
    app.run(debug=False)










