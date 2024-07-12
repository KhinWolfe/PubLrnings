from flask import Flask, render_template
import random
import datetime
import requests


cur_year = datetime.datetime.now().year
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, year=cur_year) # here i am using num as a kwarg, index will reference num

@app.route('/guess/<guess_name>')
def predict_name(guess_name):
    response = requests.get(url=f"https://api.agify.io?name={guess_name}")
    guess_age = response.json()["age"]
    response = requests.get(url=f"https://api.genderize.io?name={guess_name}")
    guess_gender = response.json()["gender"]
    print(response.json()["gender"])
    return render_template("guess.html", name=guess_name, gender=guess_gender, age=guess_age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)




if __name__ == '__main__':
    app.run(debug=True)

