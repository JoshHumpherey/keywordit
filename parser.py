""" Python Script for Displaying Comments Based On Keywords """
import praw

def find_relevant_comments(url, search_term):
    CREDENTIALS = []
    with open(".gitignore") as f:
        content = f.readlines()
        for item in content:
            item_len = len(item)
            item = str(item[0:item_len-1])
            CREDENTIALS.append(item)
    try:
        reddit = praw.Reddit(user_agent='Comment Extraction via keywordit',
                             client_id=CREDENTIALS[0], client_secret=CREDENTIALS[1])
    except:
        return "Invalid Session Information"
    try:
        submission = reddit.submission(url=str(url)):
    except:
        return "Invalid URL"
    return return_comment_list(submission, keyword)

def return_comment_list(submission, keyword):
    try:
        for top_level_comment in submission.comments:
            if keyword in top_level_comment.body:
                print(top_level_comment.body)
                all_replies = top_level_comment.replies
                for comment in all_replies:
                    print("^  " + comment.body)
        return
    except:
        return "Error while parsing comments"
