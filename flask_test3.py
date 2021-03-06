# Flask Test 3

from flask import Flask, render_template, request, session, url_for, redirect, flash
from datetime import datetime, timedelta
from processing import do_calculation

app = Flask(__name__)
app.config["SECRET_KEY"] = "qpueuwrhuqjfn;nWOREJ"
app.permanent_session_lifetime = timedelta(minutes = 120)

@app.route('/', methods=["GET", "POST"])

def index():

    if "id" not in session:
        session['id'] = 123
        session["game_over"] = False
        session['player_command'] = "blank"
        session['buffer_txt'] = ""
        session['test_lst'] = []
        session['restart'] = False
        session["count"] = 0
        session.permanent = True
        flash(f"Welcome to Dark Castle Tester - please enter a primary color", "info")


    if request.method == "POST":

        if request.form['submit_button'] == 'Submit':
            session['player_command'] = str(request.form['player_command'])
            session["count"] = session["count"] + 1
            print(session['count'])
        if request.form['submit_button'] == 'Restart':
            session['restart'] = True

        if session['restart']:
            session.pop('id', None)
            flash(f"Welcome to Dark Castle Tester - please enter a primary color", "info")

        elif not session["game_over"]:
            session["buffer_txt"], session["game_over"], session["test_lst"] = do_calculation(session['player_command'], session["test_lst"])
            session.modified = True

        else: # if session['game_over'] == True
            count = session['count']
            flash(f"Your game has ended after  {count} entries - press 'Restart' to play again", "info")

    else:
        print('How did we get here?')

    return render_template('index.html', output = session["buffer_txt"], my_list = session["test_lst"])

if __name__ == '__main__':
    app.run(use_reloader=False, debug=True)






# Next Steps
# I seem to have a web server issue? Code keeps hanging after 10 - 12 entries
# July 4: Signed up for a pythonanywhere account today to try a differet web server
# July 5: Pushed flask_test2 to GitHub and then manually cloned it to my pythonanywhere account
# July 7: Started working on basch on pythonanywhere
# July 8: Yet more pythonanywhere troubleshooting
# July 9: got flask_test3.py running publicly on pythonanywhere!!
# July 10: Progress! I have flask_test3.py running on pythonanywhere and i have a git update process defined. Here's how it works:
	# 1) Update code on my iPad in Pythonista
	# 2) Commit and auto-push to GitHub using Working Copy
	# 3) 'git pull https://github.com/tsnellgrove/flask_test2' from the bash console on pythonanywhere: https://www.pythonanywhere.com/user/Tsnellgrove/consoles/16388612/
	# 4) Reload the website from here: https://www.pythonanywhere.com/user/Tsnellgrove/webapps/#tab_id_tsnellgrove_pythonanywhere_com

# Jul 11: Flask resources
	#	Bootstrap: https://getbootstrap.com/docs/3.4/
	# Clear form after submitted: https://stackoverflow.com/questions/31945329/clear-valid-form-after-it-is-submitted
	# Git Branching: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
	# *** Tech With Tim - Flask youtube tutorials ***: https://youtu.be/mqhxxeeTbu0
	

# Jul 11: Pythonanywhere resources:
	#	Git at the command line: https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html
	# Python scritp to web site tutorial: https://blog.pythonanywhere.com/169/
	# Basic vi commands: https://www.cs.colostate.edu/helpdocs/vi.html
	# Syncing GitHub with Pythonanywhere: https://stackoverflow.com/questions/48047123/syncing-github-with-pythonanywhere
	# *** Setting up Flask on Pythonanywhere tutorial ***: https://help.pythonanywhere.com/pages/Flask/
	# my pythonanywhere site: http://tsnellgrove.pythonanywhere.com
	

# NEXT: Start planning the re-write of Dark Castle for Flask
	







# CODE CLEANUP

#    if request.method == "GET":
#        return render_template('index.html', output = session["buffer_txt"], my_list = session["test_lst"])

#            print('player hit submit')

#            session["count"] = session.get("count") + 1

#            print('PLAYER HIT RESTART')

#            return render_template('index.html', output = session["buffer_txt"], my_list = session["test_lst"])



# FOR TESTING

#    session.pop('game_over', None)

# next need to test by getting restart button value and then popping game over

#        return render_template('index.html', output = session["buffer_txt"], my_list = session["test_lst"])

#        session["buffer_txt"], session["game_over"], session["test_lst"] = do_calculation(session['player_command'], session["test_lst"])
#        session.modified = True

#            session.pop('player_command', None)
#            session.pop('count', None)

#            session.pop('game_over', None)
#            session.pop('game_over', None)

#        return redirect('/') # change to redirect to "index" ?

#    else:
#        return render_template('index.html', output = session["buffer_txt"], my_list = session["test_lst"])


# JUL 1: Buttons working but need to sort out restart intentions - doesn't work to pop


#def contact():
#    if request.method == 'POST':
#        if request.form['submit_button'] == 'Do Something':
#            pass # do something
#        elif request.form['submit_button'] == 'Do Something Else':
#            pass # do something else
#        else:
#            pass # unknown
#    elif request.method == 'GET':
#        return render_template('contact.html', form=form)



# NEW COMMENTED OUT (July 2, 2020)


#        if request.form['submit_button'] == 'Submit':
#            session['player_command'] = str(request.form['player_command'])
#            session["count"] = session.get("count") + 1
#        if request.form['submit_button'] == 'Restart':
#            session['restart'] = True
#            session.pop('game_over', None)
#        if session["game_over"]:
#            count = session['count']
#            flash(f"Your game has ended after  {count} entries - press 'Restart' to play again", "info")
#            session['player_command'] = "blank"
#            session['count'] = 1
#            session['test_lst'] = []
#            session['game_over'] = False
#            print("Session reset")



#    if 'player_command' in session:
#        session["buffer_txt"], session["game_over"], session["test_lst"] = do_calculation(session['player_command'], session["test_lst"])
#        session.modified = True
#        print(session["game_over"])
#        print(session["test_lst"])
#        print(session["count"])

#    return render_template('index.html', output = session["buffer_txt"], my_list = session["test_lst"])



#	*** Ideas ***

#Finished flash tutuorial... next thing to do is to sort out my logic and get my test code really working.. then after that, time for Alchemy tutorial
# Making progress on the pseudo code



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

#	Another idea - expose moves and score in index.html in table at top

