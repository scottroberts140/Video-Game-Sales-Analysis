# Refactoring Guide: Video Game Sales Notebook

## Overview

This notebook was refactored from **165 cells** with ~1,600 lines of custom code down to **19 cells** using DSR (Data Science Resources) libraries. This guide documents the refactoring process and key decisions.

---

## Original State

**Cell Count:** 165 cells
**Structure:**
- 50+ markdown cells (documentation and headers)
- 115+ code cells (custom functions, analysis, and visualizations)
- ~1,600 lines of custom code
- Multiple custom classes (DataframeColumn, DataframeInfo, etc.)
- Embedded analysis logic throughout

**Custom Code Patterns:**
- Helper classes for dataframe inspection
- Manual data quality analysis
- Custom visualization functions
- Inline data preparation logic
- Repeated code patterns for similar operations

---

## Refactored State

**Cell Count:** 19 cells
**Structure:**
- 10 markdown cells (clear section organization)
- 9 code cells (focused, library-driven analysis)
- ~200 lines of code
- All analysis delegated to DSR libraries
- Clean, readable progression

**Key Improvements:**
- ✓ 88% reduction in cell count
- ✓ 87% reduction in code lines
- ✓ Eliminated custom helper classes
- ✓ Standardized data analysis workflow
- ✓ Better code reusability

---

## Refactoring Strategy

### Phase 1: Analysis & Planning
1. Examined original 165-cell structure
2. Identified analysis stages:
   - Data loading and exploration
   - Data cleaning and preparation
   - Feature engineering
   - Model building and evaluation
   - Results presentation
3. Mapped existing code to DSR library capabilities
4. Planned cell consolidation

### Phase 2: Custom Code Replacement
**Deleted ~115 code cells containing:**
- Custom DataframeColumn class
- Custom DataframeInfo class
- Manual data quality checks
- Redundant visualization code
- Custom helper functions

**Replaced with DSR libraries:**
- `analyze_dataset()` from dsr-data-tools
- `DataSplits` from dsr-feature-eng-ml
- `ModelEvaluation` from dsr-feature-eng-ml

### Phase 3: Notebook Restructuring
Created clean, logical 19-cell structure:

| Cell | Type | Purpose |
|------|------|---------|
| 1 | MD | Title |
| 2 | MD | Project overview with styled border |
| 3 | MD | Environment setup section header |
| 4 | Code | Clean library imports |
| 5 | MD | Data loading section header |
| 6 | Code | Load data + analyze with recommendations |
| 7 | Code | Display recommendations |
| 8 | MD | Analysis summary header |
| 9 | MD | Data findings and decisions (manual notes) |
| 10 | MD | Data preparation section header |
| 11 | Code | Data cleaning and target variable |
| 12 | MD | Data splits section header |
| 13 | Code | Create stratified train/val/test splits |
| 14 | MD | Model evaluation header |
| 15 | Code | Train models with hyperparameter grids |
| 16 | MD | Results header |
| 17 | Code | Display model comparison results |
| 18 | MD | Test evaluation header |
| 19 | Code | Test set performance metrics |

---

## Key Architectural Changes

### 1. Automated Analysis
**Before:**
```python
# 10+ custom functions for data inspection
class DataframeInfo:
    def __init__(self, ...): ...
    def get_description(self): ...
    # 50+ lines of methods

# Manual usage in cells
```

**After:**
```python
from dsr_data_tools import analyze_dataset

games_analysis, recommendations = analyze_dataset(games, generate_recs=True)
```

### 2. Data Splitting
**Before:**
```python
# Manual train/test split code
# Custom stratification logic
# 20+ lines per split operation
```

**After:**
```python
from dsr_feature_eng_ml import DataSplits

splits = DataSplits.from_data_source(
    games_clean,
    target_column='success',
    feature_columns=feature_columns,
    test_size=0.2,
    random_state=42
)
```

### 3. Model Evaluation
**Before:**
```python
# Individual model training code
# Manual hyperparameter grid setup
# Custom cross-validation logic
# 100+ lines across multiple cells
```

**After:**
```python
from dsr_feature_eng_ml import ModelEvaluation

results = ModelEvaluation.evaluate_dataset(
    splits,
    hyperparameter_grids=hyperparameter_grids,
    cv=5,
    n_iter=5,
    scoring='f1',
    n_jobs=-1,
    viable_f1_gap=0.05
)
```

---

## DSR Libraries Used

### dsr-data-tools (v0.0.2)
**Function:** `analyze_dataset(data, generate_recs=True)`
- Analyzes data structure and quality
- Generates actionable recommendations
- Returns analysis dict and recommendations dict
- Replaces ~25 custom functions

**Key Parameters:**
- `data` - Input DataFrame
- `generate_recs=True` - Generate recommendations (default: False)

### dsr-feature-eng-ml (v0.0.1)
**Classes:** `DataSplits`, `ModelEvaluation`

**DataSplits:**
- Creates stratified train/validation/test splits
- Handles feature/target separation
- Maintains class distribution

**ModelEvaluation:**
- Trains and evaluates multiple algorithms
- Performs grid search or randomized search
- Supports cross-validation
- Generates comparison results

---

## Manual Steps Required

### 1. Data Loading Path
Update CSV path from course structure to project structure:
```python
# Before (course path):
games = pd.read_csv('/datasets/games.csv')

# After (project path):
games = pd.read_csv('./datasets/games.csv')
```

### 2. Analysis Notes
Add manual observations in Cell 9 based on `analyze_dataset()` recommendations:
```markdown
**Data Findings:**
- [Manual notes from recommendations]

**Decisions Made:**
- [Rationale for data handling choices]
```

### 3. Feature Selection
Customize feature columns based on project needs:
```python
feature_columns = ['Year_of_Release', 'Critic_Score', 'User_Score']
```

### 4. Hyperparameter Grids
Adjust model grids for your specific problem:
```python
hyperparameter_grids = {
    'decision_tree': {'max_depth': [3, 4, 5, 6, 7]},
    'random_forest': {'n_estimators': [50, 100, 150, 200]},
    'logistic_regression': {'C': [0.1, 1, 10]}
}
```

---

## Quality Assurance

### Verification Checklist
- [x] All 19 cells created with correct IDs
- [x] Markdown cells properly formatted
- [x] Code cells executable without errors
- [x] Imports verified (all DSR libraries available)
- [x] Data path configured (relative path to datasets/)
- [x] No unused imports
- [x] Comments clear and concise

### Testing
```bash
# Run all cells in order
jupyter nbconvert --to notebook --execute notebook.ipynb
```

---

## Benefits of Refactoring

### Code Quality
- Reduced complexity from 1,600 → 200 lines
- Eliminated duplicate code patterns
- Standardized analysis workflow
- Improved readability

### Maintainability
- Single source of truth (DSR libraries)
- Easier to update analysis logic
- Bug fixes in libraries benefit all projects
- Clear separation of concerns

### Scalability
- Easier to add new datasets
- Simple to adjust hyperparameters
- Reusable across similar projects
- Faster to iterate on models

### Performance
- Optimized library implementations
- Parallel processing (n_jobs=-1)
- Efficient data structures
- Better memory management

---

## Known Limitations

### Current Constraints
1. Feature columns must be manually specified
2. Hyperparameter grids are project-specific
3. Target variable logic currently manual
4. Visualization code minimal (focus on ML)

### Future Improvements
- [ ] Auto feature column detection
- [ ] Intelligent grid suggestions based on data
- [ ] Built-in plotting utilities
- [ ] Model comparison visualizations

---

## Troubleshooting

### Cell Execution Errors

**ImportError: No module named 'dsr_data_tools'**
```bash
# Reinstall DSR libraries
pip install -e "path/to/dsr-data-tools"
pip install -e "path/to/dsr-feature-eng-ml"
```

**FileNotFoundError: ./datasets/games.csv**
```bash
# Ensure running from project root
cd "/Users/scottroberts/Documents/Developer/Projects/Video Game Sales Analysis"
jupyter notebook
```

**ValueError in DataSplits.from_data_source()**
```python
# Ensure target_column exists in data
# Ensure feature_columns are all numeric or properly encoded
# Verify no NaN values in selected columns
```

---

## Reference Implementation

See [Mobile Carrier Subscriber Analysis](../Mobile%20Carrier%20Subscriber%20Analysis/README.md) for reference implementation using the same refactoring pattern.

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2025-12-18 | 1.0 | Initial refactoring (165 → 19 cells) |

---

## Questions or Issues?

- **DSR Libraries:** See respective README files in Python Libraries folder
- **Notebook Structure:** Refer to Cell-by-Cell breakdown above
- **Data Preparation:** Check DEVELOPMENT_SETUP.md for environment details

---

Last Updated: December 18, 2025
