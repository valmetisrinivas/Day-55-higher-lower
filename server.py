from flask import Flask
import random

random_number = random.choice(range(0, 100))
print(random_number)
colors = ['Tomato', 'Orange', 'DodgerBlue', 'MediumSeaGreen', 'Gray', 'SlateBlue', 'Violet', 'LightGray']

app = Flask(__name__)


@app.route('/')
def higher_lower():
    col = random.choice(colors)
    return f"<h1 style='color:{col}'>Guess a number between 0 and 100</h1>" \
           "<img src='https://media1.giphy.com/media/xUn3CftPBajoflzROU/200w.webp?cid=ecf05e47ex5ibnwof5cd68y9mmyywtdno6pto6ht3puokqju&rid=200w.webp&ct=g'>"


@app.route('/<int:number>')
def guess_number(number):
    col = random.choice(colors)
    if number > random_number:
        return f"<h1 style='color:{col}'>Too high. Try Again!!</h1><img src='https://media3.giphy.com/media/l2JhAgiGSvMordxQs/200w.webp?cid=ecf05e472b25i5fkcjsx40c5uejy7cz245xf6laxmi56o3n8&rid=200w.webp&ct=g'>"
    elif number < random_number:
        return f"<h1 style='color:{col}'>Too Low. Try Again!!</h1><img src='https://media0.giphy.com/media/qv50XIiLWonsZG9ZNh/200w.webp?cid=ecf05e47j2ox8cdmt4zcr5eiec0v1q6pbi80ame2f7shpdm8&rid=200w.webp&ct=g'>"
    else:
        return f"<h1 style='color:{col}'>Congratulations. You guessed it Right!!</h1><img src='https://media2.giphy.com/media/T0WzQ475t9Cw/200w.webp?cid=ecf05e47k16ywm3zgg6o0f2cvl6vy6gkls2ol09gpy22sjba&rid=200w.webp&ct=g'>"


if __name__ == "__main__":
    app.run(debug=True)
