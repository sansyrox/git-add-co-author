import requests
import subprocess
import click

DB_PATH = "/tmp/add-co-author"


def add_co_author(username="", name="", email="", token=""):
    if not name and not email:
        if not token:
            raise ValueError(
                "GitHub token not found. Please provide a token with --token or configure one with `git config --global github.token <token>`"
            )

        if not username:
            raise ValueError(
                "GitHub username not found. Please provide a username as the first argument."
            )

        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"https://api.github.com/users/{username}", headers=headers
        )
        if response.status_code != 200:
            raise ValueError(
                f"Error fetching GitHub profile for {username}: {response.status_code} {response.reason}"
            )
        data = response.json()
        name = data.get("name", "")
        email = data.get("email", "")
        if not name and not email:
            raise ValueError(
                f"GitHub profile for {username} does not have a name or email address"
            )
    author = f"{name} <{email}>" if name and email else f"{name or email}"
    subprocess.call(
        ["git", "commit", "--amend", "--trailer=" + f"Co-Authored-By: { author }"]
    )


def save_token(token):
    subprocess.call(["git", "config", "--global", "github.add-co-author-token", token])


def get_token():
    token = (
        subprocess.check_output(["git", "config", "--global", "github.token"])
        .decode("utf-8")
        .strip()
    )
    return token


@click.command()
@click.option("--username", "-u", help="The GitHub username.")
@click.option("--name", "-n", help="The name of the co-author.")
@click.option("--email", "-e", help="The email address of the co-author.")
@click.option("--token", "-t", help="Your GitHub personal access token.")
def main(username="", name="", email="", token=""):
    if token:
        save_token(token)
    else:
        token = get_token()
        add_co_author(username, name, email, token)


if __name__ == "__main__":
    main()
