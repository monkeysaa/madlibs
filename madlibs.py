"""A madlib game that compliments its users."""

from random import choice, sample
from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

user = "User"

@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    user = request.args.get("person") 
    # This doesn't update the global user value. How do I fix this?

    compliment = choice(AWESOMENESS)
    nice_things = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           user=user,
                           compliment=compliment,
                           compliments=nice_things)

#each of these is known as an endpoint (decorator + view function)
@app.route('/game')
def show_madlib_form():
    """ """
    response = request.args.get("game?")

    if response == "yes":
        return render_template("game.html", 
                                user=user,
                                compliment=choice(AWESOMENESS))
    elif response == "no": 
        return render_template("goodbye.html",
                                user=user,
                                compliment=choice(AWESOMENESS))

@app.route('/madlib')
def show_madlib(**keyword_dict):
    name = request.args.get("person")
    adjective = request.args.get("adjective")
    noun = request.args.get("noun")
    color = request.args.get("color")
    new_pets = request.args.getlist("pet-names")

    return render_template("madlib.html",
                           noun=noun, person=name, user=user, color=color, 
                           adjective=adjective, compliment=choice(AWESOMENESS),
                           new_pets=new_pets, num_pets=len(new_pets))

# question: Is there a good way to pass variables on one page to another page?

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
