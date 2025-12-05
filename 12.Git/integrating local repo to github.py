"""
Integrating a Local Git Repository with GitHub

This script demonstrates the typical workflow for pushing your local git repository to GitHub
for the first time using Python's subprocess module (for command execution).

Prerequisites:
- Git must be installed and configured locally.
- You must have created a new repository on GitHub (without initializing with a README, .gitignore, or License).

Steps Covered:
1. Initialize a local git repo (if not already done)
2. Add all files and make the initial commit
3. Add the remote GitHub URL
4. Push to GitHub (main branch by default)
"""

import subprocess

def integrate_with_github(local_repo_path, github_repo_url, branch="main"):
    """
    Automates adding a remote and pushing initial commit to GitHub.
    """
    # Step 1: Initialize repo (if not already a git repo)
    subprocess.run(['git', 'init'], cwd=local_repo_path, check=True)
    
    # Step 2: Add all files and commit
    subprocess.run(['git', 'add', '.'], cwd=local_repo_path, check=True)
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=local_repo_path, check=True)
    
    # Step 3: Add GitHub remote
    subprocess.run(['git', 'remote', 'add', 'origin', github_repo_url], cwd=local_repo_path, check=True)
    
    # Optional: Set default branch (if needed)
    subprocess.run(['git', 'branch', '-M', branch], cwd=local_repo_path, check=True)
    
    # Step 4: Push to GitHub
    subprocess.run(['git', 'push', '-u', 'origin', branch], cwd=local_repo_path, check=True)
    print(f"Pushed local repo at '{local_repo_path}' to GitHub repo '{github_repo_url}' on branch '{branch}'.")

# Example usage (uncomment and edit paths & URL as needed):
# integrate_with_github('/path/to/your/local/repo', 'https://github.com/yourusername/your-repo.git')

"""
Manual CLI steps this automates (reference):

# If you haven't already:
git init
git add .
git commit -m "Initial commit"

# Add remote origin
git remote add origin https://github.com/yourusername/your-repo.git
git branch -M main  # Rename branch to main if not already main
git push -u origin main
"""
