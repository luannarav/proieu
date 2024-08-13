import requests

GITHUB_API_URL = "https://api.example.com"
REPO_OWNER = "octocat"
REPO_NAME = "Hello-World"
pull_number = 42

url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pull_number}/files"

response = requests.get(url)

if response.status_code == 200:
    files = response.json()
    for file in files:
        print(file['filename'])
else:
    print(f"Failed to fetch files: {response.status_code}")
