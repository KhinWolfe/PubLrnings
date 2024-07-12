from flask import Flask, render_template, request
import requests
import smtplib
import os

MY_EMAIL = os.environ["my_email"]
MY_PASS = os.environ["my_pass"]
TO_EMAIL = os.environ["to_email"]
print(MY_PASS)
print(MY_EMAIL)
print(TO_EMAIL)

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    sent = False
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        sent = True
    return render_template("contact.html", sent=sent)

@app.route("/form-entry", methods=["POST"])
def receive_data():
    return "<h1>Successfully sent your message!</h1>"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def send_email(name, email, phone, message):
    msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=msg
        )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
