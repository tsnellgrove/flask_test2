# Flask Test 2

from flask import Flask, render_template, request, session, url_for
# from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy as SQLAlchemy # Is this right???
from datetime import datetime

# import the Flask class from the flask module
# from flask import Flask, render_template, request, session

from processing import do_calculation

# create the application object
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "qpueuwrhuqjfn;nWOREJ"

# class Todo(db.Model):
#    id = db.Column(db.Integer, primary_key= True)
#    content = db.Column(db.String(200), nullable=False)
#    date_created = db.Column(db.DateTime, defualt =datetime.utcnow)

#    def __repr__(self):
#        return '<Task %r>' % self.id

# NOTE: Alchemy DB not working yet - commented out - maybe use REDIS instead?

# use decorators to link the function to a url
@app.route('/', methods=["GET", "POST"])

#def home():
#    return "Hello, Big World!"  # return a string

@app.route('/')
def index():

    if "count" in session:
        session["count"] = session.get("count") + 1
    else:
        session["count"] = 1
    if "test_lst" not in session:
        session["test_lst"] = []
    if "game_over" not in session:
        session["game_over"] = True
    if 'player_command' not in session:
        session['player_command'] = "blank"

    if request.method == "POST":
        session['player_command'] = str(request.form['player_command'])
        if session["game_over"]:
            session['player_command'] = "blank"
            session['count'] = 1
#            session.pop('player_command', None)
#            session.pop('count', None)
            session['test_lst'] = []
            session['game_over'] = False
#            session.pop('game_over', None)
            print("Session reset")

    if 'player_command' in session:
        session["buffer_txt"], session["game_over"], session["test_lst"] = do_calculation(session['player_command'], session["test_lst"])
        session.modified = True
        print(session["game_over"])
        print(session["test_lst"])
        print(session["count"])

    return render_template('index.html', output = session["buffer_txt"], my_list = session["test_lst"])


# @app.route('/readme')
# def dark_castle():
#    return render_template('readme.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
#    app.run(debug=True)
    app.run(use_reloader=False, debug=True)


#	*** Ideas ***

# I need to step back and think more about how I really want this to work
#	Wireframes would help... need to plan out exactly what should appear when the player starts and stops the game
# Then after I really know what I want to do, solve it
# Then before going on I need to take some flask YouTube tutorials and learn more about what is really possible

# NEED TO SORT OUT 'QUIT' => 'GOODBYE' => 'ENTER PRIMARY COLOR'
#		Solve with flashed message?

#	Consider adding a clean up routine that runs if the player hits a separate 'quit & close out' button

#	*** NEW CODED TO IMPLEMENT ***
#	New idea: I need a 'Reset' button next to 'Submit'
#	DONE: Change 'game_reset' => 'game_over'
#	Create a new 'game_reset' variable
#	HOW TO SET VARIABLE WITH BUTTON IN TEMPLATE???
# Once 'game_over' == True, any Submit => "Press 'Reset' to start the game over"
#	Reset sets 'game_reset' which resets all variables to initial states (maybe by popping all of them first ??)
# On Submit, if game_over == False, provide content from dark_castle.py
#	*** NEW CODED TO IMPLEMENT ***


#	*** Pseudo Code ***

#	HTML Template in /Templates 
#		TITLE "Dark Castle"
#		Print {{buffer}}
#		Form to accept input 'player_command'

#	Python Code - Dark Castle Program
#		Contains all functions
#		Contains all static dict
#		All print() => 'buffer' via redirect of stdio
#		All end conditions => return 'game_reset' = True
#		Text interpreter function
#			Implements 'quit'
#			Contains timer code
#			Returns: 'buffer', 'game_reset', <all stateful dicts>

#	Flask App
#		Standard opening & closing
#		Route for /
#		Local variables
#			if 'game_reset' not in session: session['game_reset'] = True
#			if session['game_reset'] == True: set 'player_command' to "game_start_xyz" & initialize all stateful dicts
#			session['game_reset'] = False
#		Get input
#			if request.method == 'POST': session['player_command'] = <player_command> (???)
#		Call python app
#			buffer, game_reset, <stateful dicts> = text_interpreter('player_command', <stateful dicts>)
#		return render_template(output = session['buffer'])


