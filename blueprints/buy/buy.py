# buy.py
import json
import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app

buy_bp = Blueprint('buy', __name__, template_folder='templates')

SUBMISSIONS_FILE = 'submissions.json'

def load_submissions():
    if os.path.exists(SUBMISSIONS_FILE):
        with open(SUBMISSIONS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_submissions(submissions):
    with open(SUBMISSIONS_FILE, 'w') as f:
        json.dump(submissions, f)

def save_submission(username, content):
    submissions = load_submissions()
    submissions.append({"username": username, "content": content, "likes": 0})
    save_submissions(submissions)

@buy_bp.route('/')
def getData():
    submissions = load_submissions()

    page_config = {
        "main_heading": "Small fis, big sea!",                  
        "heading_color": "blue",                            
        "heading_font": "Arial, sans-serif",                  
        "heading_font_size": "3em",                           
        "heading_font_weight": "bold",                        
        "heading_alignment": "center",                        
        "paragraphs": "keep swimming little guy",  
        "paragraph_color": "blue",                           
        "paragraph_font": "Georgia, serif",                   
        "paragraph_font_size": "1.5em",                       
        "paragraph_alignment": "center",                      
        "background_image": "/static/media/fis.jpg", 

        # Styling for success message, blog form, and submissions
        "success_text": "u fried da fis!",
        "success_text_color": "blue",
        "success_image": "/static/media/fis_fry.jpg",
        "success_image_width": "100%",  

        # Blog form title and styling
        "blog_title": "What do you like about the fis?",
        "blog_title_color": "orange",
        "blog_title_font_size": "3em",
        "blog_title_padding": "10px",
        "form_label_padding": "10px",


        "form_background_color": "blue",

        # Form labels and styling for input fields
        "form_label_username": "Username:",
        "form_label_content": "Comment:  ",
        "form_label_text_color": "orange",
        "form_label_font_size": "2em",
        "button_background_color": "#444",
        "button_text_color": "#fff",

        # Submissions title and styling
        "submissions_title": "Submissions:",
        "submissions_title_color": "black",
        "submissions_font_size": "2em",
        "submissions_background_color": "white",

        # Alignment for blog, form, and submissions content
        "blog_alignment": "center"
    }

    merged_config = {**current_app.config, **page_config}
    return render_template('tab1.html', **merged_config, submissions=submissions)

@buy_bp.route('/submit_blog', methods=['POST'])
def submit_blog():
    username = request.form.get('username')
    content = request.form.get('content')
    save_submission(username, content)
    return redirect(url_for('buy.getData'))

@buy_bp.route('/like_submission/<int:index>', methods=['POST'])
def like_submission(index):
    submissions = load_submissions()
    if 0 <= index < len(submissions):
        submissions[index]['likes'] += 1
        save_submissions(submissions)
    return redirect(url_for('buy.getData'))
