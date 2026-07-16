"""
gitlab_client.py

ATSF-OSC
GitLab Repository Metadata Collector
"""

import requests


class GitLabClient:
    """
    Client for retrieving GitLab repository metadata.
    """

    BASE_URL = "https://gitlab.com/api/v4"

    def __init__(self, token=None):

        self.headers = {}

        if token:
            self.headers["PRIVATE-TOKEN"] = token

    def get_project(self, project_id):
        """
        Retrieve GitLab project metadata.

        Parameters
        ----------
        project_id : str
            GitLab project ID or URL-encoded namespace/project.

        Returns
        -------
        dict
        """

        url = f"{self.BASE_URL}/projects/{project_id}"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return {
            "name": data.get("name"),
            "description": data.get("description"),
            "default_branch": data.get("default_branch"),
            "visibility": data.get("visibility"),
            "stars": data.get("star_count"),
            "forks": data.get("forks_count"),
            "open_issues": data.get("open_issues_count"),
            "last_activity": data.get("last_activity_at"),
            "created_at": data.get("created_at"),
        }


if __name__ == "__main__":

    client = GitLabClient()

    # Example:
    # project_id = "gitlab-org%2Fgitlab"

    print("GitLab client ready.")