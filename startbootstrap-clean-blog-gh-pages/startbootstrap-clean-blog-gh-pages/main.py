from flask import Flask, render_template
import requests
from pprint import pprint

posts = requests.get("https://api.npoint.io/f82517dd6df0c3f37b86").json()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/<int:index>')
def show_post(index):
    request_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            request_post = blog_post
    return render_template("post.html", post=request_post)



if __name__ == "__main__":
    app.run(debug=True)

