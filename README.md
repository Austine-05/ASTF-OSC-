# ATSF-OSC

## AI-Powered Trust Scoring Framework for Open-Source Software Components

ATSF-OSC is an AI-driven framework for assessing the trustworthiness of Open-Source Software (OSS) components used in modern software supply chains. The framework combines machine learning, graph neural networks, transformer-based code representation, and explainable artificial intelligence to generate an interpretable trust score for OSS packages.

The framework integrates:

- XGBoost for tabular risk prediction
- GraphSAGE for dependency graph analysis
- CodeBERT for commit anomaly detection
- Ridge Meta-Learner for ensemble trust scoring
- SHAP Explainable AI for feature attribution
- SPDX 2.3 and CycloneDX 1.6 SBOM trust attestation
- REST API for CI/CD integration

---

## Highlights

- Multi-modal AI trust scoring
- Supply-chain risk assessment
- Explainable predictions
- SBOM-compatible trust attestation
- CI/CD policy enforcement
- Graph-based dependency analysis
- Commit behaviour analysis
- Statistical validation framework

---

## Repository Structure

```
ATSF-OSC/
│
├── api/
├── data/
├── docs/
├── experiments/
├── figures/
├── models/
├── notebooks/
├── results/
├── src/
├── tests/
│
├── README.md
├── LICENSE
├── requirements.txt
├── Dockerfile
└── CITATION.cff
```

---

## System Architecture

The ATSF-OSC framework consists of four major layers:

1. Multi-source Data Ingestion
2. Feature Engineering and Graph Construction
3. Multi-model Ensemble Learning
4. Trust Score Aggregation and Explainability

---

## Experimental Evaluation

The framework is designed for rigorous evaluation using:

- Stratified five-fold cross-validation
- Package-family leakage prevention
- Statistical significance testing
- SHAP explainability
- Ablation analysis
- ROC analysis
- Confusion matrix evaluation

---

## Citation

If you use this repository in your research, please cite the accompanying paper.

---

## License

MIT License

---

## Author

**Augustine Ndudi Egere**

Department of Computer Science

Federal Polytechnic Bali

Taraba State, Nigeria
