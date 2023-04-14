import praw
import time

# Set up the Reddit instance
reddit = praw.Reddit(client_id=input("Client ID: "), client_secret=input("Client Secret: "),
                     user_agent='your_user_agent', username=input("Username: "), password=input("Password: "))

# Get the excluded subreddits from user input
excluded_subs = []
while True:
    sub = input("Enter an excluded subreddit (leave blank to continue): ")
    if not sub:
        break
    excluded_subs.append(sub)

# Delete all comments
for comment in reddit.user.me().comments.new(limit=None):
    comment.delete()
    print(f"Comment deleted! - {comment}")

# Delete all non-excluded posts
for submission in reddit.user.me().submissions.new(limit=None):
    if submission.subreddit.display_name in excluded_subs:
        print(f"Skipping post in excluded subreddit: {submission}")
        continue

    submission.delete()
    print(f"Post deleted! - {submission}")

# Print "Done" when finished
print("Done")
