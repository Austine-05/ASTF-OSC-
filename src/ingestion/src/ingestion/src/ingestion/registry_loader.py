"""
registry_loader.py

ATSF-OSC
Package Registry Metadata Loader

Retrieves metadata from software package registries.
"""

import requests


class RegistryLoader:
    """
    Retrieves package metadata from supported registries.
    """

    def __init__(self):
        self.pypi_url = "https://pypi.org/pypi"

    def get_pypi_package(self, package_name):
        """
        Retrieve package information from PyPI.
        """

        url = f"{self.pypi_url}/{package_name}/json"

        response = requests.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        info = data.get("info", {})

        return {
            "name": info.get("name"),
            "version": info.get("version"),
            "summary": info.get("summary"),
            "license": info.get("license"),
            "author": info.get("author"),
            "home_page": info.get("home_page"),
            "project_url": info.get("project_url"),
            "requires_python": info.get("requires_python"),
        }


if __name__ == "__main__":

    loader = RegistryLoader()

    package = loader.get_pypi_package("requests")

    print(package)