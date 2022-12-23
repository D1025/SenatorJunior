import os
import openai

tokens_used = 0


def get_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def api_prepare():
    openai.api_key = os.environ['API_KEY']
    global tokens_used
    f = open("management/API/tokens.txt", "r")
    for line in f:
        tokens_used = int(line)
    f.close()


def propt_text(text):
    global tokens_used
    if (tokens_used < 5000):
        tokens_used += 100
        responce = get_response(text)
    else:
        responce = "Not enough tokens"
    return responce


def api_out():
    global tokens_used
    f = open("management/API/tokens.txt", "w")
    f.write(str(tokens_used))
    f.close()
