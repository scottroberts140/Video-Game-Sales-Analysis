# Video Game Sales Analysis

## Project Overview

This project analyzes video game sales data to identify patterns and characteristics that determine commercial success in the gaming industry. By examining trends across platforms, genres, regions, and critical metrics, the analysis provides insights into what drives video game market performance.

**Key Objective:** Develop predictive models to determine which factors most strongly correlate with successful game sales globally.

---

## Dataset Description

**Source:** Video game sales and ratings dataset

**Key Statistics:**
- **Total Records:** 16,715 video games
- **Time Period:** 1980-2016
- **Geographic Coverage:** North America, Europe, Japan, and Global data
- **Sales Metric:** Millions of units sold

**Features:**
| Feature | Type | Description |
|---------|------|-------------|
| Name | Categorical | Game title |
| Platform | Categorical | Gaming platform (PS2, Xbox, DS, etc.) |
| Year_of_Release | Numerical | Year the game was released |
| Genre | Categorical | Game category (Action, Sports, RPG, etc.) |
| Publisher | Categorical | Company that published the game |
| NA_Sales | Numerical | Sales in North America (millions) |
| EU_Sales | Numerical | Sales in Europe (millions) |
| JP_Sales | Numerical | Sales in Japan (millions) |
| Global_Sales | Numerical | Total worldwide sales (millions) |
| Critic_Score | Numerical | Aggregated critic score (0-100) |
| User_Score | Numerical | Aggregated user score (0-10) |

---

## Project Structure

```
Video Game Sales Analysis/
├── Video Sales Analysis project.ipynb    # Main analysis notebook (18 cells)
├── README.md                             # This file
├── DEVELOPMENT_SETUP.md                  # Environment setup guide
├── REFACTORING_GUIDE.md                  # Refactoring documentation
├── refactor_notebook.py                  # Notebook generation script
├── datasets/
│   └── games.csv                         # Video game sales data
├── venv/                                 # Python virtual environment
└── .gitignore                            # Git configuration
```

---

## Methodology

### 1. Data Loading & Analysis
- Load video game sales data
- Generate automated recommendations for data handling
- Identify missing values and data type issues
- Document key statistics and characteristics

### 2. Data Preparation
- Clean and validate data
- Handle missing values appropriately
- Create target variable (success classification based on sales)
- Prepare features for modeling

### 3. Data Splitting
- Stratified train/validation/test split
- Maintain class distribution across splits
- Enable robust model evaluation

### 4. Model Evaluation
- Train multiple algorithms with hyperparameter optimization:
  - **Decision Tree:** max_depth tuning (3-7)
  - **Random Forest:** n_estimators optimization (50-200)
  - **Logistic Regression:** Regularization tuning (C: 0.1-10)
- Cross-validation (5-fold) for robust performance estimates
- F1-score as primary evaluation metric

### 5. Results & Insights
- Compare model performance across validation and test sets
- Identify the most predictive features
- Document findings and recommendations

---

## Results

**Model Performance Summary:**
- Detailed results available in notebook cell output
- Model rankings by F1-score
- Test set evaluation metrics
- Feature importance analysis

**Key Insights:**
- [Will be updated after model evaluation]
- Critical success factors in video game sales
- Regional variation patterns
- Platform and genre trends

---

## Dependencies

### Core Libraries
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization
- **scipy** - Statistical analysis
- **scikit-learn** - Machine learning models

### DSR Custom Libraries (Development Mode)
- **dsr-utils** (v0.0.1) - Utility functions and formatting
- **dsr-data-tools** (v0.0.2) - `analyze_dataset()` function for automated analysis and recommendations
- **dsr-feature-eng-ml** (v0.0.1) - `DataSplits` and `ModelEvaluation` classes for model development

### Development Tools
- **jupyter** - Interactive notebook environment

---

## Setup Instructions

### Prerequisites
- Python 3.13+
- macOS (or adjust paths for your OS)
- Git

### Installation

1. **Navigate to project directory:**
   ```bash
   cd "/Users/scottroberts/Documents/Developer/Projects/Video Game Sales Analysis"
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install pandas numpy matplotlib seaborn scipy scikit-learn jupyter
   ```

4. **Install DSR libraries in development mode:**
   ```bash
   pip install -e "../Python Libraries/dsr-utils"
   pip install -e "../Python Libraries/dsr-data-tools"
   pip install -e "../Python Libraries/dsr-feature-eng-ml"
   ```

5. **Verify installation:**
   ```bash
   python3 -c "from dsr_data_tools import analyze_dataset; from dsr_feature_eng_ml import DataSplits, ModelEvaluation; print('✓ Ready to analyze')"
   ```

### Running the Analysis

1. **Start Jupyter notebook:**
   ```bash
   jupyter notebook
   ```

2. **Open:** `Video Sales Analysis project.ipynb`

3. **Run cells** in order (Shift+Enter)

---

## Usage

### Notebook Workflow

**Cell 1-2:** Project title and overview
- Sets context for the analysis

**Cell 3-4:** Environment setup and imports
- Loads all required libraries and DSR tools

**Cell 5-8:** Data loading and analysis
- Loads games.csv
- Generates automated recommendations
- Displays suggestion for data handling

**Cell 9:** Data analysis summary
- Documents findings and decisions made

**Cell 10-11:** Data preparation
- Cleans data and creates target variable
- Reports dataset shape after cleaning

**Cell 12-13:** Data splitting
- Creates stratified train/validation/test splits
- Reports split sizes

**Cell 14-17:** Model evaluation
- Trains models with hyperparameter grids
- Displays results and rankings

**Cell 18-19:** Test set evaluation
- Final performance metrics on held-out test data

---

## Key Features

✓ **Automated Analysis:** `analyze_dataset()` generates data quality recommendations
✓ **Modular Design:** Clean separation of data prep, splitting, and modeling
✓ **Hyperparameter Optimization:** Grid search across multiple algorithms
✓ **Cross-Validation:** Robust 5-fold CV prevents overfitting
✓ **Reproducible:** Fixed random seed (42) for consistent results
✓ **Well-Documented:** Markdown cells explain methodology at each stage

---

## Technologies & Tools

| Category | Tool |
|----------|------|
| **Language** | Python 3.13.7 |
| **Environment** | Jupyter Notebook |
| **Data Processing** | Pandas, NumPy |
| **Analysis** | SciPy |
| **ML Framework** | scikit-learn |
| **Visualization** | Matplotlib, Seaborn |
| **Custom Libraries** | dsr-utils, dsr-data-tools, dsr-feature-eng-ml |
| **Version Control** | Git + GitHub |

---

## Development Notes

### Environment
- **Python Version:** 3.13.7
- **Virtual Environment:** `venv/` (isolated dependencies)
- **Development Mode:** All DSR libraries installed with `-e` flag for live code changes

### Refactoring History
- **Original:** 165 cells with ~1,600 lines of custom code
- **Refactored:** 19 cells using DSR libraries
- **Improvement:** 88% cell reduction, cleaner analysis structure
- **Date:** December 18, 2025

### Installation Method
Three DSR libraries installed in **development mode** (`pip install -e`):
- Changes to source code immediately reflected in notebooks
- Ideal for active development and library testing
- Located at: `/Users/scottroberts/Documents/Developer/Projects/Python Libraries/`

---

## Known Issues & Limitations

### Current Limitations
1. **Data Completeness:** Some records have missing critic and user scores
2. **Time Period:** Older games (pre-2000) may have incomplete sales data
3. **Regional Gaps:** Lesser-covered regions not included in analysis
4. **L1_Ratio Deprecation:** LogisticRegression shows FutureWarning in scikit-learn 1.8
   - Warning only; does not affect current execution
   - Will require library update when scikit-learn 1.10 releases

---

## Future Enhancements

### Recommended Library Improvements
- [ ] **dsr-data-tools:** Add integer conversion recommendation type
- [ ] **dsr-data-tools:** Decimal precision optimization analysis
- [ ] **dsr-feature-eng-ml:** Fix LogisticRegression l1_ratio deprecation

### Potential Analysis Extensions
- [ ] Feature importance visualization
- [ ] Regional sales trend analysis
- [ ] Platform evolution over time
- [ ] Genre performance comparison
- [ ] Correlation analysis between critic/user scores and sales

---

## License

This project is part of the TripleTen Data Science program.

---

## Contact & Attribution

**Author:** Scott Roberts  
**Created:** December 2025  
**Repository:** [github.com/scottroberts140/Video-Game-Sales-Analysis](https://github.com/scottroberts140/Video-Game-Sales-Analysis)

---

**Last Updated:** December 18, 2025
