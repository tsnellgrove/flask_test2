# Flask Test 2
# import the Flask class from the flask module
from flask import Flask, render_template, request, session

from processing import do_calculation

# create the application object
app = Flask(__name__)
app.config["SECRET_KEY"] = "qpueuwrhuqjfn;nWOREJ"

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
    if "exit_now" not in session:
        session["exit_now"] = False
    if 'player_command' not in session:
        session['player_command'] = "blank"

    if request.method == "POST":
        session['player_command'] = str(request.form['player_command'])
        if session["exit_now"]:
            session.pop('player_command', None)
            session.pop('count', None)
            session['test_lst'] = []
            session.pop('exit_now', None)
            print("Session Popped")

    if 'player_command' in session:
        session["buffer_txt"], session["exit_now"], session["test_lst"] = do_calculation(session['player_command'], session["test_lst"])
        session.modified = True
        print(session["exit_now"])
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

#	Consider adding a clean up routine that runs if the player hits a separate 'quit & close out' button

