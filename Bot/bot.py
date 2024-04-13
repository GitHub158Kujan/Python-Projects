import praw
import random

client_id = "bMjn6u-4kBj9ru1ch0bdrg"
client_secret = "WAaIgrk2avzdUKGb3CT6F0HSUIGeow"
username = "SilentSyntax158"
password = "e@jBhhr9z3ieZ$l"
user_agent="<Programmer>"

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                     username=username, password=password, user_agent=user_agent)

list1 = [ "Book recommendation: Fantasy :Harry Potter series by J.K. Rowling",
    "Book recommendation: Science Fiction : Dune by Frank Herbert",
    "Book recommendation: Mystery : The Girl with the Dragon Tattoo by Stieg Larsson",
    "Book recommendation: Thriller : Gone Girl by Gillian Flynn",
    "Book recommendation: Romance : Pride and Prejudice by Jane Austen",
    "Book recommendation: Historical Fiction : The Nightingale by Kristin Hannah",
    "Book recommendation: Horror : The Shining by Stephen King",
    "Book recommendation: Biography : Steve Jobs by Walter Isaacson",
    "Book recommendation: Self-Help : The Subtle Art of Not Giving a F*ck by Mark Manson",
    "Book recommendation: Classic : To Kill a Mockingbird by Harper Lee",
    "Book recommendation: Young Adult :The Hunger Games series by Suzanne Collins",
    "Book recommendation: Non-Fiction: Sapiens: A Brief History of Humankind by Yuval Noah Harari"]

subreddit = reddit.subreddit("booksuggestions")
for post in subreddit.new(limit=15):
    for comments in post.comments:
        if hasattr(comments, "body"):
            comment_lower = comments.body.lower()
            if " books " or " book " in comment_lower:
                random_index = random.randint(0, len(list1) - 1)
                comments.reply(list1[random_index])
