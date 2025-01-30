import requests

GITHUB_USERNAME = "Mwaurasammy"
url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100"

response = requests.get(url)
repos = response.json()

with open("repos.txt", "w") as file:
    for repo in repos:
        file.write(repo["git_url"] + "\n")

print("Extracted repository URLs have been saved to repos.txt!")
