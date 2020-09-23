import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/')
def index():
    num = random.randint(1, 20)
    birthday = "08/23/1999"
    return flask.render_template(
        "index.html", 
        random_number=num, # if this is confusing, look up ‘python kwaargs’
        birth_date=birthday
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)