# import the Flask class from the flask module
from flask import Flask, render_template, request, session
from scram_sol_fcns import *
import numpy as np
#from helpers import login_required, generate_scramble, average, bestsolve

# create the application object
app = Flask(__name__)
app.secret_key = 'secret'

# default cube scramble length
default_length = 15

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if not request.form.get("length"):
            length = default_length
        else:
            length = request.form.get("length")
            length = int(length)
        scramble = generate_scramble(length)
        scrambled = exec_scramble(scramble)

    else:
        length = default_length
        scramble = generate_scramble(default_length)
        scrambled = exec_scramble(scramble)

    return render_template('home.html', scramble=scramble,
                           top=scrambled['top'],
                           left=scrambled['left'],
                           front=scrambled['front'],
                           right=scrambled['right'],
                           back=np.fliplr(scrambled['back']),
                           bottom=scrambled['bottom'])


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)