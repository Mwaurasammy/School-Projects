import os
import subprocess

# Set your main repository details
MAIN_REPO = "School-Projects"  # Change to your actual repo name
GITHUB_USERNAME = "Mwaurasammy"  # Change to your GitHub username

# # Change directory to the main repo
# os.chdir(MAIN_REPO)

# Read repo URLs from repos.txt, convert git:// to https://, and add as submodules
with open("repos.txt", "r") as file:
    for repo in file:
        repo = repo.strip()
        if repo:
            # Convert git:// URLs to https://
            repo = repo.replace("git://", "https://")
            
            folder_name = os.path.basename(repo).replace(".git", "")
            subprocess.run(["git", "submodule", "add", repo, folder_name])

# Commit and push the changes
subprocess.run(["git", "commit", "-m", "Added all repositories as submodules"])
subprocess.run(["git", "push", "origin", "main"])

print("✅ All repositories have been added as submodules using HTTPS!")
