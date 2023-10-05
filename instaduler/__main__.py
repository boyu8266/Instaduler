import argparse
import glob
import json
import os

from instagrapi import Client

from instaduler.const import *
from instaduler.model import Post, PostList
from instaduler.pipeline import InstaPipeline


def login(username, password):
    client = Client()
    success = client.login(username=username, password=password)
    if not success:
        print(f"Login failed: {username}")
        return

    client.dump_settings(SESSION_FILE)
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
        postlist = PostList.parse_file(SCHEDULE_FILE)
    except:
        postlist = PostList()

    try:
        if not isinstance(postlist.posts, list):
            postlist.posts = []

        postlist.posts.append(post)
        with open(SCHEDULE_FILE, 'w', encoding='utf-8') as file:
            json.dump(postlist.dict(), file, ensure_ascii=False, indent=4)
        print(f"Post from folder: {folder}, with caption: {text}")
    except:
        print(f"An exception occurred while saving the JSON file.")


def run():
    try:
        postlist = PostList.parse_file(SCHEDULE_FILE)
        post = postlist.posts[0]
    except:
        print(f"Please set up the schedule through 'post' first.")
        return

    pipeline = InstaPipeline()
    pipeline.run(post)


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

    run_parser = subparsers.add_parser(
        "run", help="Run Schedule Post")

    args = parser.parse_args()

    if args.action == "login":
        login(args.user, args.psw)
    elif args.action == "post":
        post(args.folder, args.text)
    elif args.action == "run":
        run()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
