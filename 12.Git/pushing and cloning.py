"""
Git: Pushing to Remote and Cloning Repositories

This script demonstrates how to push to a remote repository and how to clone a git repository
using Python's subprocess module.

Prerequisites:
- Git must be installed.
- For pushing: You must have a local repo with a configured remote.

"""

import subprocess

def push_to_remote(repo_dir, remote='origin', branch='main'):
    """
    Pushes local commits to the specified remote and branch.
    """
    subprocess.run(['git', 'push', remote, branch], cwd=repo_dir, check=True)
    print(f"Pushed to {remote}/{branch} from {repo_dir}")

def clone_repo(git_url, clone_dir=None):
    """
    Clones the specified git repository URL into the given directory.
    If clone_dir is None, it is cloned into the current directory using the repo name.
    """
    cmd = ['git', 'clone', git_url]
    if clone_dir:
        cmd.append(clone_dir)
    subprocess.run(cmd, check=True)
    print(f"Cloned {git_url} {'into ' + clone_dir if clone_dir else ''}")

# Example usage:
# To push local changes:
# push_to_remote('/path/to/your/local/repo', remote='origin', branch='main')

# To clone a repository:
# clone_repo('https://github.com/username/repository.git', 'my-repo-dir')

"""
Manual equivalents (reference):

# Push to remote
git push origin main

# Clone a repository
git clone https://github.com/username/repository.git [optional-directory-name]
"""
