from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
@app.route('/hello')
def hello():
    page = """
    <h1>Here's a random number: {0}</h1>
    <form>
        <button>New Number</button>
    </form>
    """
    num = random.randint(1, 25)
    return page.format(num)


@app.route('/form')
def form():
    return render_template("favorite_form.html")


@app.route('/results', methods=["POST"])
def results():

    color = request.form['color'].lower().strip()
    luck_num = request.form['luck_num']
    fav_class = request.form['fav_class']
    best_pix = request.form['best_pix'].lower().strip()

    films = [
        "toy story", "a bug's life", "toy story 2", "monsters, inc.",
        "finding nemo", "the incredibles", "cars", "ratatouille",
        "wall-e", "up", "toy story 3", "cars 2", "brave",
        "monsters university", "inside out", "the good dinosaur",
        "finding dory", "cars 3", "coco", "incredibles 2",
        "toy story 4", "onward", "soul"
    ]

    colors = ["red", "green", "blue"]

    if color not in colors:
        color = "Invalid color. Choose red, green, or blue."
    else:
        color = color.title()

    if best_pix not in films:
        best_pix = "Sorry, that is not a Pixar movie."
    else:
        best_pix = best_pix.title()

    return render_template(
        "form_results.html",
        color=color,
        luck_num=luck_num,
        fav_class=fav_class,
        best_pix=best_pix
    )


def valid_hex_chars(code):
    valid = "0123456789ABCDEF"

    for char in code.upper():
        if char not in valid:
            return False

    return True


@app.route('/hex_form', methods=["GET", "POST"])
def hex_form():

    if request.method == "POST":
        hex = request.form['hex']

        if len(hex) != 6:
            feedback = "Hex code must be exactly 6 characters."
            hex = "FF0000"

        elif not valid_hex_chars(hex):
            feedback = "Use only numbers 0-9 and letters A-F."
            hex = "FF0000"

        else:
            feedback = "Valid hex code!"

    else:
        hex = "FF0000"
        feedback = ""

    return render_template(
        "hex_form.html",
        hex=hex,
        feedback=feedback
    )


if __name__ == "__main__":
    app.run()
