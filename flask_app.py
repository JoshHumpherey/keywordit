from flask import Flask, render_template, request, flash, session
import os
import collections
import praw

app = Flask(__name__)
secret_key = str(os.urandom(24))
app.secret_key = secret_key

@app.route("/")
def hello():
    return render_template('mainpage.html')

@app.route('/', methods=['POST'])
def my_form_post():
    url = request.form['Reddit URL']
    search_term = request.form['Keyword']
    top_comment_list = find_relevant_comments(url, search_term)
    parent = get_comment_text(top_comment_list)
    return render_template('mainpage.html', output = parent)

def find_relevant_comments(url, search_term):
    CREDENTIALS = []
    with open("credentials.txt") as f:
        content = f.readlines()
        for item in content:
            CREDENTIALS.append(item)
    try:
        reddit = praw.Reddit(user_agent='Comment Extraction via keywordit',
                             client_id=CREDENTIALS[0], client_secret=CREDENTIALS[1])
    except:
        return [("Invalid Session Information", [])]
    try:
        submission = reddit.submission(url=str(url))
    except:
        return [("Invalid URL", [])]
    result_dict = return_comment_list(submission, search_term)
    return result_dict

def return_comment_list(submission, keyword):
    comment_list = []
    try:
        for top_comment in submission.comments:
            if keyword in top_comment.body:
                comment_list.append(top_comment)
        return comment_list
    except:
        return [("Error while parsing comments", [])]

def get_comment_text(comment_list):
    expanded_comments = []
    try:
        for top_comment in comment_list:
            other_comments = []
            for comment in top_comment.replies:
                other_comments.append(comment.body)
            thread = (top_comment.body, other_comments)
            expanded_comments.append(thread)
        return expanded_comments
    except:
        return [("No Comments Meet Search Criteria", [])]

if __name__ == "__main__":
    app.run()
