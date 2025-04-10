from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("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")

@app.route("/")
def chat():
    try:
        user_input = request.json.get("message")

        client = openai.OpenAI()  # New OpenAI SDK client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a badminton expert assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        return jsonify({"reply": response.choices[0].message.content})

    except Exception as e:
        print("🔥 ERROR:", str(e))
        return jsonify({"error": str(e)}), 500
