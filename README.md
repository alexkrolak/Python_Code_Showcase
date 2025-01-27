# Python Data Pipeline & Modeling Demonstration

This repository showcases my **Python coding ability** and **statistical modeling expertise** using entirely **simulated data**. The workflow follows a typical data science pipeline:

1. **Data Generation**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Engineering & Final Preparation**
4. **Modeling & Evaluation**

Since the data is randomly generated, results are purely illustrative—demonstrating code structure and methodology rather than real-world predictive power.

---

## Table of Contents
1. [Overview](#overview)
2. [Project Notebooks](#project-notebooks)
3. [Requirements & Setup](#requirements--setup)
4. [Usage](#usage)
5. [License](#license)
6. [Contact](#contact)

---

## Overview
The primary goal is to show how I:
- Generate synthetic data for demonstration.
- Identify and clean issues programmatically (invalid IDs, missing values, etc.).
- Engineer final features for modeling.
- Fit both **basic** and **advanced** models (linear regression, advanced methods) to illustrate coding patterns and best practices.

---

## Project Notebooks

1. **Generate_Data.ipynb**  
   - Creates **fake random data** to analyze.
   - Exports this simulated dataset as CSV.

2. **EDA.ipynb**  
   - Loads the CSV data.
   - Performs **Exploratory Data Analysis** to detect, summarize, and programmatically clean data issues.

3. **Feature_Engineering.ipynb**  
   - **Final data preparation** for modeling.
   - Adds or encodes new features (e.g., time-based, categorical encodings).
   - Merges data from different sources into a single modeling dataset.

4. **Modeling.ipynb**  
   - **Fits a basic linear model** (and more sophisticated models).
   - Evaluates model performance, avoiding overfitting.
   - Summarizes findings (though the random data means no real “insights”).

---

## Requirements & Setup
- **Python 3.8+** recommended.
- Core libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `statsmodels`
  - `xgboost` (optional, for advanced modeling)

Install dependencies:

```bash
pip install -r requirements.txt
