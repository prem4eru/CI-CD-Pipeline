import requests

def get_new_commits(repo_owner, repo_name, last_commit_sha=None):
    # GitHub API endpoint to list commits
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    
    # Parameters to pass to the API
    params = {}
    if last_commit_sha:
        params['since'] = last_commit_sha
    
    # Send GET request to the GitHub API
    response = requests.get(url, params=params)
    
    # Check if request was successful
    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        return None

def main():
    # GitHub repository details
    repo_owner = 'prem4eru'
    repo_name = 'CI-CD-Pipeline'
    
    # Optional: Last commit SHA to start checking from
    last_commit_sha = None  # Provide the last commit SHA if needed
    
    # Fetch new commits
    commits = get_new_commits(repo_owner, repo_name, last_commit_sha)
    
    # Print new commits
    if commits:
        print(f"New commits in {repo_owner}/{repo_name}:")
        for commit in commits:
            print(f"- {commit['commit']['message']}")
    else:
        print("No new commits found.")

if __name__ == "__main__":
    main()