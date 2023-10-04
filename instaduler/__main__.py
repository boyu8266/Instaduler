import argparse

from instagrapi import Client


def login(username, password):
    client = Client()
    success = client.login(username=username, password=password)
    if not success:
        print(f"Login failed: {username}")
        return

    client.dump_settings("config/session.json")
    print(f"Logging in with user: {username}")


def main():
    parser = argparse.ArgumentParser(description="Login operations")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    # Subcommand: login
    login_parser = subparsers.add_parser(
        "login", help="Perform login operation")
    login_parser.add_argument(
        "-u", "--user", required=True, help="Specify the username")
    login_parser.add_argument(
        "-p", "--psw", required=True, help="Specify the password")

    args = parser.parse_args()

    if args.action == "login":
        login(args.user, args.psw)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
