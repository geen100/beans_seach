from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
from openai import OpenAI  # 正しいインポート方法
import requests

# .envファイルから環境変数を読み込む
load_dotenv()

# OpenAI クライアントの初期化
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

sheet_db = os.getenv("sheet_db")

app = Flask(__name__, static_folder="static")

@app.route("/", methods=["GET", "POST"])
def home():
    beans = None

    if request.method == "POST":
        prompt = request.form["prompt"]
        print(f"Received prompt: {prompt}")

        try:
            # シートDBからデータを取得
            response = requests.get(sheet_db)
            response.raise_for_status()
            beans_data = response.json()

            # 豆情報を構成
            beans_info = "以下は利用可能な豆のリストである:\n"
            for bean in beans_data:
                beans_info += f"name: {bean.get('name', 'N/A')}, Details: {bean.get('Details', 'N/A')}\n"

            prompt_with_context = (
                "あなたはタリーズの店員です。以下のビーンズ情報を使って、ユーザーの質問に答えてください.\n"
                f"{beans_info}\n\n"
                f"User's question: {prompt}"
            )
            print(f"Prompt with context: {prompt_with_context}")

            # GPT-4 の呼び出し
            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "あなたは役に立つ店員です。"},
                    {"role": "user", "content": prompt_with_context},
                ],
            )

            # 正しいレスポンスの取得
            # ChatCompletion のレスポンスがオブジェクトの場合、属性アクセスに変更
            beans = completion.choices[0].message.content
            print(f"GPT response: {beans}")

        except requests.exceptions.RequestException as e:
            beans = "シートDBにアクセスできませんでした。"
            print(f"Requests error: {e}")
        except Exception as e:
            beans = "予期しないエラーが発生しました。"
            print(f"その他のエラー: {e}")

    return render_template("index.html", beans=beans)


if __name__ == "__main__":
    app.run(debug=True)
