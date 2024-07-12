from flask import Flask
import random

rand_num = random.randint(0, 9)

app = Flask(__name__)
IMG = '<iframe src="https://giphy.com/embed/3oGRFlpAW4sIHA02NW" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cinder-libcinder-craig-pickard-3oGRFlpAW4sIHA02NW"></a></p>'
HIGH_IMG = '<iframe src="https://giphy.com/embed/0WDHw9NXHFAqqzhYTi" width="476" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/new-york-falling-big-apple-0WDHw9NXHFAqqzhYTi">via GIPHY</a></p>'
LOW_IMG = '<iframe src="https://giphy.com/embed/U52j0YphKRTEs" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/scooter-low-rider-U52j0YphKRTEs"></a></p>'
CORRECT_IMG = '<iframe src="https://giphy.com/embed/UXgf6pu1LlQp6CPDi0" width="426" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/mrnigelng-cooking-show-uncle-roger-UXgf6pu1LlQp6CPDi0"></a></p>'

@app.route('/')
def hello_world():
    return ('<h1>Guess a number between 0 and 9</h1>'
            f'{IMG}')

@app.route('/<int:num>')
def eval_guess(num):
    colors = ["blue", "red", "green"]
    color = random.choice(colors)
    if num > rand_num:
        return_text = "Your guess is too high"
        return_img = HIGH_IMG
    elif num < rand_num:
        return_text = "Your guess is too low"
        return_img = LOW_IMG
    else:
        return_text = "CORRECT!"
        return_img = CORRECT_IMG
    return (f'<h1 style="color:{color}">{return_text}</h1>'
            f'{return_img}')

if __name__ == "__main__":
    app.run(debug=True)