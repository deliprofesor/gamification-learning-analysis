# Analysis of Teaching-Learning Gamification Strategies

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains an exploratory data analysis (EDA) and visualization of gamification's impact on educational processes.

##  About the Dataset
The dataset compiles quantitative and qualitative information on gamification strategies, focusing on student motivation, role performance, and collaborative dynamics.

- **Source:** [Mendeley Data](https://data.mendeley.com/datasets/yc4np572zs/1)
- **Institution:** Universidad de Las Americas
- **Contributors:** Patricia Acosta-Vargas, Cristian Uchima-Marin, Luis Salvador-Acosta

## Recent Updates
- **Automated Data Pipeline:** Developed `src/data_cleaning.py` to handle raw Excel files.
- **Numerical Mapping:** Standardized categorical Spanish evaluations into a 1-4 numerical scale.
- **Professional Refactoring:** Organized the workspace into a standard data science project structure.

##  Repository Structure

```text
gamification-learning-analysis/
├── data/
│   ├── raw/                # Original Excel datasets from Mendeley Data
│   └── processed/          # Cleaned and numerically transformed CSV files
├── src/
│   └── data_cleaning.py    # Python script for data preprocessing and mapping
├── .gitignore              # Prevents tracking of venv and cache files
├── LICENSE                 # CC BY 4.0 License
└── README.md               # Project documentation
```

### Translation & Standardization
To ensure global accessibility and ease of coding, all Spanish headers and categorical values have been mapped to English equivalents.
- **Source Language:** Spanish (ES)
- **Target Language:** English (EN)

### Qualitative to Quantitative Conversion
Student evaluations were originally recorded as categorical feedback. These have been transformed into a numerical scale to enable statistical analysis and multidimensional profiling:

| Qualitative Level (ES) | Qualitative Level (EN) | Numerical Value |
|:-----------------------|:-----------------------|:---------------:|
| **BAJO** | Low                    | **1** |
| **BÁSICO** | Basic                  | **2** |
| **ALTO** | High                   | **3** |
| **SUPERIOR** | Superior               | **4** |

##  Evaluation Metrics
The analysis focuses on 5 core dimensions:
1. **Group Motivation** (Engagement levels)
2. **Role Performance** (How well roles are adopted)
3. **Task Completion** (Timeliness and quality)
4. **Learning & Interaction** (Knowledge sharing)
5. **Group Integration** (Harmony and conflict resolution)

##  Analysis & Methodology
- Conversion of qualitative scales (Low, Basic, High, Superior) to numerical values (1-4).
- Descriptive statistics and multidimensional radar profiling.
- Visualizing trends across different gamification missions.

##  Citation
If you use this project, please cite the original dataset:
> Acosta-Vargas, Patricia; Uchima-Marin, Cristian; Salvador-Acosta, Luis (2025), “Dataset on Teaching-Learning Gamification”, Mendeley Data, V1, doi: 10.17632/yc4np572zs.1
