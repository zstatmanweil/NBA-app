from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import json
from nba.app_functions import display_table, convert_to_players, users_choice

#npaplayers.json found here: http://data.nba.net/10s/prod/v1/2017/players.json
json_file = open('./data/nbaplayers.json')
json_str = json_file.read()
json_data = json.loads(json_str)

#accessing each player's dictionary and name
players = json_data['league']['standard']

# Get list of player objects
players_list = convert_to_players(players)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/start", methods=['GET'])
def start():
    first_table = display_table(players_list)
    first_question = """\nAre you curious which players were drafted in a specific year? Of \
course you are! Enter a year, and a list of players drafted that year will be provided."""

    return render_template('choice_form.html', first_table=first_table.to_html(), first_question=first_question)

@app.route("/choice", methods=['GET'])
def choice():
    return render_template('choice_form.html')

@app.route("/result", methods=['POST'])
def result():
    choice = request.form['choice']
    result = users_choice(players_list, choice)

    return render_template('show_result.html', result=result)

if __name__ == "__main__":
    app.run()