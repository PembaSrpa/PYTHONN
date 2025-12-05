"""
Installing and Configuring Git: A Beginner's Guide

1. Installing Git
-----------------
- On Windows: Download from https://git-scm.com/ and follow the installer.
- On Mac: Use Homebrew:   brew install git
- On Linux: Typically, use your package manager:
    sudo apt-get install git         # Debian/Ubuntu
    sudo yum install git             # Fedora/CentOS

2. Checking If Git Is Installed
------------------------------
Open a terminal or command prompt and run:
    git --version
This should print the installed Git version.

3. Initial Git Configuration
---------------------------
Set your name and email (used for commits):
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"

To check your configuration:
    git config --list

4. Other Useful Global Configurations
------------------------------------
Set your default text editor (e.g., nano, vim, code for VSCode):
    git config --global core.editor nano
Enable colored output:
    git config --global color.ui auto

5. Creating and Cloning Repositories
------------------------------------
Create a new git repository in the current directory:
    git init

Clone an existing repository:
    git clone https://github.com/username/repo.git

6. Example: Script to Initialize a Git Repo (Python subprocess)
--------------------------------------------------------------
"""
import subprocess

# Initialize a new Git repository and set config (example)
def setup_git_repo(repo_dir, user_name, user_email):
    """
    Initializes a git repository in repo_dir and sets user config.
    """
    subprocess.run(['git', 'init', repo_dir], check=True)
    subprocess.run(['git', '-C', repo_dir, 'config', 'user.name', user_name], check=True)
    subprocess.run(['git', '-C', repo_dir, 'config', 'user.email', user_email], check=True)
    print(f"Initialized empty Git repo in '{repo_dir}' with user '{user_name}'.")

# Example usage:
# setup_git_repo('my_project', 'Alice Example', 'alice@example.com')

