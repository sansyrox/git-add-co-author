# Git Add Co-Author

## Demo
![git-add-co-author](https://user-images.githubusercontent.com/29942790/235253455-12d5d664-7ff8-43ad-b1fe-63db986120aa.gif)


## Overview

Git Add Co-Author is a simple Python script that allows you to easily add co-authors to your Git commits, ensuring proper credit is given to all contributors involved in the development process. This can be particularly useful for open-source projects, where multiple contributors are working together, or for pair programming sessions where two developers contribute to the same commit.

## Installation

1. Install the package using pip:

```bash
pip install git-add-co-author
```

2. Obtain a personal access token from GitHub. You can generate one by following the instructions in the [GitHub documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

3. Configure the script with your GitHub token:

```bash
python -m git_add_co_author --token <your_token>
```

## Usage

To add a co-author to your commit, simply run the script with the co-author's GitHub username:

```bash
python -m git_add_co_author <co_author_username>
```

For example:

```bash
python -m git_add_co_author sansyrox
```

If you do not want to authorize a token, you can add the co-author's name and email address directly:

```bash
python -m git_add_co_author --name "John Doe" --email "john.doe@example.com"
```

### Optional Configuration

I alias this command as `alias gac="python -m git_add_co_author"` in my `.zshrc` file, so I can simply run `gac <co_author_username>` to add a co-author to my commit.

## Rationale

The motivation behind creating this script is to provide an easy way to give credit to contributors in various situations:

- In open-source projects, when a pull request (PR) is closed without merging but the idea or code is later implemented.
- During pair programming sessions, where two or more developers work together on a single commit.

Existing solutions were either too complicated or didn't work as expected, so Git Add Co-Author was developed as a simple, easy-to-use alternative.

## License

This project is licensed under the MIT License.
