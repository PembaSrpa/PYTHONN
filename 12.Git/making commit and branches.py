"""
Git: Making Commits and Working with Branches

This script demonstrates basic git workflows using Python's subprocess module,
including making commits and working with branches programmatically.

Prerequisite:
- Git must be installed on your system.
- The current working directory should be a git repository.

This does NOT cover advanced branching strategies (like rebasing, merging conflicts, etc.).
"""

import subprocess

def make_commit(commit_message, cwd=None):
    """
    Stages all changes and makes a commit with the given commit_message.
    """
    subprocess.run(['git', 'add', '.'], cwd=cwd, check=True)
    subprocess.run(['git', 'commit', '-m', commit_message], cwd=cwd, check=True)
    print(f"Committed: {commit_message}")

def create_and_checkout_branch(branch_name, cwd=None):
    """
    Creates a new branch and checks it out.
    """
    subprocess.run(['git', 'checkout', '-b', branch_name], cwd=cwd, check=True)
    print(f"Created and switched to branch: {branch_name}")

def checkout_branch(branch_name, cwd=None):
    """
    Checks out an existing branch.
    """
    subprocess.run(['git', 'checkout', branch_name], cwd=cwd, check=True)
    print(f"Switched to branch: {branch_name}")

def list_branches(cwd=None):
    """
    Lists all branches in the repository.
    """
    print("Your branches:")
    subprocess.run(['git', 'branch'], cwd=cwd, check=True)

# Example usage:
if __name__ == "__main__":
    repo_dir = '.'  # Change to your repo path if needed

    # 1. Make a commit
    # make_commit("Describe your changes here", cwd=repo_dir)

    # 2. Create and switch to a new branch
    # create_and_checkout_branch("feature/new-feature", cwd=repo_dir)

    # 3. Checkout an existing branch
    # checkout_branch("main", cwd=repo_dir)

    # 4. List all branches
    # list_branches(cwd=repo_dir)

"""
Manual commands equivalent:

# Stage all changes and commit
git add .
git commit -m "Your commit message"

# Create and switch to a new branch
git checkout -b feature/new-feature

# Switch to an existing branch
git checkout main

# List all branches
git branch
"""
