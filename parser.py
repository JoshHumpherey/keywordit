""" Python Script for Displaying Comments Based On Keywords """

import praw
SEARCH_TERMS = ["Amazon", "amazon", "OA2"]
CREDENTIALS = []
with open(".gitignore") as f:
    content = f.readlines()
    for item in content:
        item_len = len(item)
        item = str(item[0:item_len-1])
        CREDENTIALS.append(item)
print(CREDENTIALS)
reddit = praw.Reddit(user_agent='Comment Extraction via keywordit',
                     client_id=CREDENTIALS[0], client_secret=CREDENTIALS[1])

submission = reddit.submission(url='https://www.reddit.com/r/cscareerquestions/comments/9mx8r1/big_4_discussion_october_10_2018/')

for top_level_comment in submission.comments:
    for keyword in SEARCH_TERMS:
        if keyword in top_level_comment.body:
            print(top_level_comment.body)
            all_replies = top_level_comment.replies
            for comment in all_replies:
                print("^  " + comment.body)
