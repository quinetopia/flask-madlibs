from flask import Flask, request, render_template
import stories

story = stories.story


app = Flask(__name__)

@app.route('/flask-madlibs')
def home_screen():
    """ Returns the homepage
    """
    return render_template("index.html", answers=story.prompts)

@app.route('/story')
def tell_story():
    """
    Tells the madlib story based on answers provided in the post request
    """
    answers = request.args
    text = story.generate(answers) 

    return render_template("story.html", text=text)



