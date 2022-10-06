import requests

response = requests.get("https://api.github.com/users/dafidakk/repos")

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} Project Url: {project['html_url']}")

