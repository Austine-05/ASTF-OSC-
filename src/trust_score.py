"""
ATSF-OSC Trust Score Module

Computes overall trust scores for software components.
"""

import numpy as np


class TrustScorer:

    def __init__(self, weights=None):

        if weights is None:
            self.weights = {
                "popularity_score": 0.20,
                "maintainer_strength": 0.20,
                "issue_density": 0.20,
                "security_score": 0.20,
                "code_quality": 0.20,
            }
        else:
            self.weights = weights

    def calculate(self, row):

        score = 0.0

        for feature, weight in self.weights.items():

            if feature in row:
                score += row[feature] * weight

        return np.round(score * 100, 2)

    def classify(self, score):

        if score >= 80:
            return "Highly Trusted"

        elif score >= 60:
            return "Trusted"

        elif score >= 40:
            return "Medium Risk"

        return "High Risk"