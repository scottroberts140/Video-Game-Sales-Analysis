#!/usr/bin/env python3
"""
Refactor Video Game Sales notebook to use DSR libraries.
Creates a clean 18-cell notebook structure.
"""

import json
from pathlib import Path

# Define the notebook cells structure (18 cells total)
cells = [
    # 1. Title (markdown)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Video Game Sales Analysis\n",
            "## Identifying Patterns That Determine Game Success"
        ]
    },
    # 2. Project Overview (markdown with styled border)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "═" * 80 + "\n",
            "\n",
            "**Project Goal:** Analyze video game sales data to identify patterns and characteristics\n",
            "that determine commercial success in the gaming industry.\n",
            "\n",
            "**Analysis Approach:** Data exploration → feature analysis → data preparation →\n",
            "model evaluation → recommendations\n",
            "\n",
            "═" * 80
        ]
    },
    # 3. Environment Setup heading (markdown)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## Environment Setup"]
    },
    # 4. Imports - Clean library imports (python)
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from scipy import stats as st\n",
            "from dsr_data_tools import analyze_dataset\n",
            "from dsr_feature_eng_ml import DataSplits, ModelEvaluation"
        ]
    },
    # 5. "## 1 Load and Analyze Dataset" heading (markdown)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 1 Load and Analyze Dataset"]
    },
    # 6. Load data + analyze with recommendations (python)
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "games = pd.read_csv('./datasets/games.csv')\n",
            "games_analysis, recommendations = analyze_dataset(games, generate_recs=True)"
        ]
    },
    # 7. Display recommendations (python)
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "if recommendations:\n",
            "    print('\\n=== Data Recommendations ===\\n')\n",
            "    for key, value in recommendations.items():\n",
            "        if isinstance(value, dict):\n",
            "            print(f'{key}:')\n",
            "            for sub_key, sub_value in value.items():\n",
            "                print(f'  {sub_key}: {sub_value}')\n",
            "        else:\n",
            "            print(f'{key}: {value}')"
        ]
    },
    # 8. "### 1.1 Data Analysis Summary" heading (markdown)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 1.1 Data Analysis Summary"]
    },
    # 9. Analysis summary (markdown - user will add manual notes)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "**Dataset Overview:**\n",
            "- Total Records: 16,715 video games\n",
            "- Time Period: 1980-2016\n",
            "- Global and regional sales data (in millions)\n",
            "\n",
            "**Key Data Characteristics:**\n",
            "- Missing values detected in certain columns\n",
            "- Sales data shows high variation across regions\n",
            "- Platform and genre are critical categorical features\n",
            "\n",
            "**Data Decisions:**\n",
            "- [To be updated with specific findings from analysis]"
        ]
    },
    # 10. "## 2 Data Preparation" heading (markdown)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 2 Data Preparation"]
    },
    # 11. Data preparation steps (python)
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Handle missing values\n",
            "games_clean = games.dropna()\n",
            "\n",
            "# Create target variable (success: global sales above median)\n",
            "median_sales = games_clean['Global_Sales'].median()\n",
            "games_clean['success'] = (games_clean['Global_Sales'] > median_sales).astype(int)\n",
            "\n",
            "print(f'Dataset shape after cleaning: {games_clean.shape}')\n",
            "print(f'Success distribution:\\n{games_clean[\"success\"].value_counts()}')"
        ]
    },
    # 12. "## 3 Create Data Splits" heading (markdown)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 3 Create Data Splits"]
    },
    # 13. DataSplits creation (python)
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Select features for modeling\n",
            "feature_columns = ['Year_of_Release', 'Critic_Score', 'User_Score']\n",
            "\n",
            "# Create data splits\n",
            "splits = DataSplits.from_data_source(\n",
            "    games_clean,\n",
            "    target_column='success',\n",
            "    feature_columns=feature_columns,\n",
            "    test_size=0.2,\n",
            "    random_state=42\n",
            ")\n",
            "\n",
            "print(f'Training set size: {len(splits.train_data)}')\n",
            "print(f'Validation set size: {len(splits.val_data)}')\n",
            "print(f'Test set size: {len(splits.test_data)}')"
        ]
    },
    # 14. "### 3.1 Evaluate Models" heading (markdown)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 3.1 Evaluate Models"]
    },
    # 15. Model evaluation (python)
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Define hyperparameter grids\n",
            "hyperparameter_grids = {\n",
            "    'decision_tree': {'max_depth': [3, 4, 5, 6, 7]},\n",
            "    'random_forest': {'n_estimators': [50, 100, 150, 200]},\n",
            "    'logistic_regression': {'C': [0.1, 1, 10]}\n",
            "}\n",
            "\n",
            "# Evaluate models\n",
            "results = ModelEvaluation.evaluate_dataset(\n",
            "    splits,\n",
            "    hyperparameter_grids=hyperparameter_grids,\n",
            "    cv=5,\n",
            "    n_iter=5,\n",
            "    scoring='f1',\n",
            "    n_jobs=-1,\n",
            "    viable_f1_gap=0.05\n",
            ")"
        ]
    },
    # 16. "### 3.2 Model Results" heading (markdown)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 3.2 Model Results"]
    },
    # 17. Display results (python)
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "print(results.summary_text)"
        ]
    },
    # 18. "## 4 Test Set Evaluation" heading (markdown)
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 4 Test Set Evaluation"]
    },
    # 19. Test set evaluation (python)
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "test_report = results.test_report\n",
            "print(test_report)"
        ]
    }
]

# Create the notebook structure
notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.13.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Write the notebook
output_path = Path("/Users/scottroberts/Documents/Developer/Projects/Video Game Sales Analysis/Video Sales Analysis project.ipynb")
with open(output_path, 'w') as f:
    json.dump(notebook, f, indent=1)

print(f"✓ Refactored notebook created: {output_path}")
print(f"✓ Total cells: {len(cells)}")
