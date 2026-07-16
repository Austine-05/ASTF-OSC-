"""
dependency_graph.py

ATSF-OSC
Dependency Graph Builder

Builds dependency graphs for software components.
"""

from dataclasses import dataclass
from typing import Dict, List
import networkx as nx


@dataclass
class DependencyNode:
    """
    Represents a software component in the dependency graph.
    """
    name: str
    version: str


class DependencyGraphBuilder:
    """
    Builds and analyses dependency graphs.
    """

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_package(self, name: str, version: str):
        """Add a package node."""
        self.graph.add_node(name, version=version)

    def add_dependency(self, package: str, dependency: str):
        """Add a dependency relationship."""
        self.graph.add_edge(package, dependency)

    def number_of_packages(self):
        return self.graph.number_of_nodes()

    def number_of_dependencies(self):
        return self.graph.number_of_edges()

    def graph_statistics(self) -> Dict:

        return {
            "packages": self.number_of_packages(),
            "dependencies": self.number_of_dependencies(),
            "density": nx.density(self.graph),
        }


if __name__ == "__main__":

    builder = DependencyGraphBuilder()

    builder.add_package("ATSF-OSC", "1.0")

    builder.add_package("requests", "2.32")

    builder.add_package("networkx", "3.2")

    builder.add_dependency(
        "ATSF-OSC",
        "requests"
    )

    builder.add_dependency(
        "ATSF-OSC",
        "networkx"
    )

    print(builder.graph_statistics())