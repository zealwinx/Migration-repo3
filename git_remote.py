import subprocess
import os

# Set repository details
BITBUCKET_USER = os.getenv("BITBUCKET_USER")
BITBUCKET_PASSWORD = os.getenv("BITBUCKET_PASSWORD")
GITHUB_USER = os.getenv("GITHUB_USER")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Construct repository URLs
bitbucket_repo = f"https://{BITBUCKET_USER}:{BITBUCKET_PASSWORD}@bitbucket.org/{BITBUCKET_USER}/repo3.git"
github_repo = f"https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/Migration-repo3.git"

try:
    # Clone the Bitbucket repository as a mirror
    subprocess.run(["git", "clone", "--mirror", bitbucket_repo], check=True)

    # Navigate into the cloned repo directory
    repo_dir = "repo3.git"

    # Push the mirrored repo to GitHub
    subprocess.run(["git", "-C", repo_dir, "push", "--mirror", "--force", github_repo], check=True)

    print("Migration from Bitbucket to GitHub completed successfully!")

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
