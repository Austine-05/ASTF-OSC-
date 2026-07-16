"""
github_client.py

ATSF-OSC
GitHub Repository Metadata Collector

This module retrieves repository metadata from the GitHub REST API.
"""

import requests


class GitHubClient:
    """Client for retrieving GitHub repository metadata."""

    BASE_URL = "https://api.github.com"

    def __init__(self, token=None):
        self.headers = {
            "Accept": "application/vnd.github+json"
        }

        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def get_repository(self, owner, repo):
        """
        Retrieve metadata for a GitHub repository.

        Parameters
        ----------
        owner : str
            Repository owner.
        repo : str
            Repository name.

        Returns
        -------
        dict
            Repository metadata.
        """

        url = f"{self.BASE_URL}/repos/{owner}/{repo}"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return {
            "name": data.get("name"),
            "owner": data.get("owner", {}).get("login"),
            "description": data.get("description"),
            "language": data.get("language"),
            "license": (
                data.get("license", {}).get("name")
                if data.get("license")
                else None
            ),
            "stars": data.get("stargazers_count"),
            "forks": data.get("forks_count"),
            "watchers": data.get("subscribers_count"),
            "issues": data.get("open_issues_count"),
            "size": data.get("size"),
            "default_branch": data.get("default_branch"),
            "created_at": data.get("created_at"),
            "updated_at": data.get("updated_at")
        }


if __name__ == "__main__":

    client = GitHubClient()

    repository = client.get_repository(
        "pallets",
        "flask"
    )

    print(repository)