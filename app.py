from flask import Flask,render_template,request
import openai

app = Flask(__name__)

# openai.api_key =

chat_log = []
messages = [{"role": "system", "content": "Welcome."}]


@app.route('/', methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":
        response = request.form["input"]

        messages = [{"role": "user", "content": f"{response}"}]

        # Call the OpenAI API to get the chat response
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Append the chat response to a list
        chat_log.append([{"role": "user", "content": response}, {"role": "assistant", "content": chat.choices[0]["message"]["content"]}])

    return render_template("index.html", chat_log=chat_log)


if __name__ == '__main__':
    app.run()