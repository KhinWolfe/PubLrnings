from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



if __name__ == "__main__":  # if name of the current file is main, then execute code
    app.run(debug=True) # allows active running/rerunning of code change on website


# make a chrome page editable
# from the console in dev tools enter the next line and press enter
# document.body.contentEditable=true
# from here you can close dev tools and edit anything in website

# to delete elements, open chrome dev tools
# use the select tool, click on the part you dont want, then press delete

# to save the changes, right click and save the html, move to your project


