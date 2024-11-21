# chart.py
import json
import os
from flask import Blueprint, render_template, request, jsonify, current_app

chart_bp = Blueprint('chart', __name__, template_folder='templates')

# Define the path for the votes file
VOTES_FILE = 'votes.json'

# Load votes from JSON file
def load_votes():
    if os.path.exists(VOTES_FILE):
        with open(VOTES_FILE, 'r') as file:
            return json.load(file)
    return {"rug_it": 0, "moon_it": 0}  # Default vote counts if file doesn't exist

# Save votes to JSON file
def save_votes(votes):
    with open(VOTES_FILE, 'w') as file:
        json.dump(votes, file)

@chart_bp.route('/')
def tab2_home():
    page_config = {
        "background_image": "/static/media/main_back.png",
        
        # Customizable text, color, and font size for headings and buttons
        "chart_heading_text": "trenches live!",
        "chart_heading_color": "black",
        "chart_heading_font_size": "8em",
        
        "vote_moon_text": "trench",
        "vote_moon_color": "black",
        "vote_moon_font_size": "1.2em",

        "vote_grape_text": "tate",
        "vote_grape_color": "black",
        "vote_grape_font_size": "1.2em"
    }
    merged_config = {**current_app.config, **page_config}
    return render_template('tab2.html', **merged_config)

@chart_bp.route('/votes', methods=['GET', 'POST'])
def handle_votes():
    votes = load_votes()
    if request.method == 'POST':
        vote_type = request.json.get('vote_type')
        if vote_type in votes:
            votes[vote_type] += 1
            save_votes(votes)
            return jsonify(success=True, votes=votes)
        return jsonify(success=False, message="Invalid vote type")

    return jsonify(votes)

@chart_bp.route('/get_votes', methods=['GET'])
def get_votes():
    votes = load_votes()
    return jsonify(votes)
