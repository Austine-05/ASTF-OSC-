"""
community_health.py

ATSF-OSC
Community Health Assessment Module

Evaluates repository governance and community health indicators.
"""

from dataclasses import dataclass


@dataclass
class CommunityHealthScore:
    readme: bool
    license: bool
    security: bool
    contributing: bool
    code_of_conduct: bool
    issue_templates: bool
    pull_request_template: bool

    @property
    def score(self):
        """Return a community health score (0-100)."""

        checks = [
            self.readme,
            self.license,
            self.security,
            self.contributing,
            self.code_of_conduct,
            self.issue_templates,
            self.pull_request_template,
        ]

        passed = sum(checks)

        return round((passed / len(checks)) * 100, 2)


class CommunityHealthAnalyzer:
    """
    Analyse repository governance indicators.
    """

    def analyze(self, repository_metadata):
        """
        Evaluate repository metadata.

        Parameters
        ----------
        repository_metadata : dict

        Returns
        -------
        CommunityHealthScore
        """

        return CommunityHealthScore(
            readme=repository_metadata.get("has_readme", False),
            license=repository_metadata.get("has_license", False),
            security=repository_metadata.get("has_security_policy", False),
            contributing=repository_metadata.get("has_contributing", False),
            code_of_conduct=repository_metadata.get("has_code_of_conduct", False),
            issue_templates=repository_metadata.get("has_issue_templates", False),
            pull_request_template=repository_metadata.get(
                "has_pull_request_template", False
            ),
        )


if __name__ == "__main__":

    sample = {
        "has_readme": True,
        "has_license": True,
        "has_security_policy": True,
        "has_contributing": True,
        "has_code_of_conduct": False,
        "has_issue_templates": True,
        "has_pull_request_template": True,
    }

    analyzer = CommunityHealthAnalyzer()

    result = analyzer.analyze(sample)

    print(f"Community Health Score: {result.score}")