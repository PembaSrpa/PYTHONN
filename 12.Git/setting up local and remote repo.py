"""
Setting Up a Local and Remote Git Repository

This script demonstrates how to:
1. Initialize a local git repository.
2. Add your files and make the first commit.
3. Add a remote repository (e.g., GitHub) and push your commit.

It uses Python's subprocess module to execute git commands.
"""

import subprocess

def setup_local_repo(repo_dir):
    """
    Initializes a git repository in the specified directory.
    """
    subprocess.run(['git', 'init'], cwd=repo_dir, check=True)
    print(f"Initialized git repository in '{repo_dir}'.")

def add_and_commit_all(repo_dir, commit_message="Initial commit"):
    """
    Stages all files and makes an initial commit.
    """
    subprocess.run(['git', 'add', '.'], cwd=repo_dir, check=True)
    subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_dir, check=True)
    print(f"Committed all files with message: '{commit_message}'.")

def add_remote(repo_dir, remote_url, remote_name="origin"):
    """
    Adds a remote repository to the local repo.
    """
    subprocess.run(['git', 'remote', 'add', remote_name, remote_url], cwd=repo_dir, check=True)
    print(f"Added remote '{remote_name}' with URL '{remote_url}' to '{repo_dir}'.")

def push_to_remote(repo_dir, branch="main", remote_name="origin"):
    """
    Pushes commits to the remote repository.
    """
    # Optionally, rename branch to 'main' if needed
    subprocess.run(['git', 'branch', '-M', branch], cwd=repo_dir, check=True)
    subprocess.run(['git', 'push', '-u', remote_name, branch], cwd=repo_dir, check=True)
    print(f"Pushed to {remote_name}/{branch}.")

# Example usage:
if __name__ == "__main__":
    repo_dir = '.'  # Change as needed; the directory you want to initialize
    remote_url = 'https://github.com/yourusername/your-repo.git'  # Change as needed

    # Step 1: Initialize the local repository
    setup_local_repo(repo_dir)

    # Step 2: Add all files and make the initial commit
    add_and_commit_all(repo_dir, "Initial commit")

    # Step 3: Add remote origin
    add_remote(repo_dir, remote_url, "origin")

    # Step 4: Push to remote (default "main" branch)
    push_to_remote(repo_dir, "main", "origin")

"""
Manual CLI reference:

# Initialize repo
git init

# Add and commit all files
git add .
git commit -m "Initial commit"

# Add remote
git remote add origin https://github.com/yourusername/your-repo.git

# Rename branch to main (if necessary) and push
git branch -M main
git push -u origin main
"""
