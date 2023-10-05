import argparse
import glob
import json
import os

from instagrapi import Client
from model import Post, PostList

schedule_file = 'config/schedule.json'
session_file = 'config/session.json'


def login(username, password):
    client = Client()
    success = client.login(username=username, password=password)
    if not success:
        print(f"Login failed: {username}")
        return

    client.dump_settings(session_file)
    print(f"Logging in with user: {username}")


def post(folder, text):
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        return

    files = glob.glob(os.path.join(folder, "*.jpg")) + \
        glob.glob(os.path.join(folder, "*.jpeg")) + \
        glob.glob(os.path.join(folder, "*.mp4"))
    post = Post(files=files, caption=text)

    try:
        postlist = PostList.parse_file(schedule_file)
    except:
        postlist = PostList()

    try:
        if not isinstance(postlist.posts, list):
            postlist.posts = []

        postlist.posts.append(post)
        with open(schedule_file, 'w', encoding='utf-8') as file:
            json.dump(postlist.dict(), file, ensure_ascii=False, indent=4)
        print(f"Post from folder: {folder}, with caption: {text}")
    except:
        print(f"An exception occurred while saving the JSON file.")


def main():
    parser = argparse.ArgumentParser(description="Login and Post operations")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    login_parser = subparsers.add_parser(
        "login", help="Perform login operation")
    login_parser.add_argument(
        "-u", "--user", required=True, help="Specify the username")
    login_parser.add_argument(
        "-p", "--psw", required=True, help="Specify the password")

    post_parser = subparsers.add_parser("post", help="Perform post operation")
    post_parser.add_argument(
        "--folder", "-f", required=True,  help="Specify the folder containing media to post")
    post_parser.add_argument(
        "--text", "-t", required=True,  help="Specify the caption for the post")

    args = parser.parse_args()

    if args.action == "login":
        login(args.user, args.psw)
    elif args.action == "post":
        post(args.folder, args.text)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
