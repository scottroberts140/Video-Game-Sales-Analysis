# Development Setup Guide

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/scottroberts140/Video-Game-Sales-Analysis.git
cd "Video Game Sales Analysis"
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scipy scikit-learn jupyter
```

### 4. Install DSR Libraries (if developing locally)
If you have the DSR libraries installed locally:
```bash
pip install -e "path/to/dsr-utils"
pip install -e "path/to/dsr-data-tools"
pip install -e "path/to/dsr-feature-eng-ml"
```

If installing from PyPI (production):
```bash
pip install dsr-utils dsr-data-tools dsr-feature-eng-ml
```

### 5. Verify Installation
```bash
python3 << EOF
import pandas as pd
import numpy as np
from dsr_data_tools import analyze_dataset
from dsr_feature_eng_ml import DataSplits, ModelEvaluation
print("✓ All imports successful!")
EOF
```

---

## Running the Notebook

### Using Jupyter Notebook
```bash
jupyter notebook
```
Then open `Video Sales Analysis project.ipynb` in your browser.

### Using VS Code
1. Install "Jupyter" extension
2. Open `Video Sales Analysis project.ipynb`
3. Select Python interpreter: `./venv/bin/python`
4. Run cells with Shift+Enter

---

## Project Structure

```
Video Game Sales Analysis/
├── Video Sales Analysis project.ipynb    # Main notebook
├── README.md                             # Project documentation
├── DEVELOPMENT_SETUP.md                  # This file
├── REFACTORING_GUIDE.md                  # Refactoring notes
├── refactor_notebook.py                  # Notebook generation script
├── datasets/
│   └── games.csv                         # Source data
├── venv/                                 # Virtual environment
└── .gitignore                            # Git ignore rules
```

---

## Environment Information

**Tested Configuration:**
- **OS:** macOS
- **Python:** 3.13.7
- **Jupyter:** 1.1.1
- **Pandas:** 2.3.3
- **NumPy:** 2.3.5
- **scikit-learn:** 1.8.0
- **matplotlib:** 3.10.8
- **seaborn:** 0.13.2

---

## Updating Dependencies

To update all packages:
```bash
source venv/bin/activate
pip install --upgrade pip
pip install --upgrade pandas numpy matplotlib seaborn scipy scikit-learn jupyter
```

To update DSR libraries (if in development mode):
```bash
pip install --upgrade --force-reinstall -e "path/to/dsr-libraries"
```

---

## Troubleshooting

### Import Errors
**Problem:** `ModuleNotFoundError: No module named 'dsr_data_tools'`

**Solution:**
```bash
source venv/bin/activate
pip install -e "path/to/dsr-data-tools"
```

### Jupyter Kernel Issues
**Problem:** Kernel not found or wrong Python version

**Solution:**
```bash
source venv/bin/activate
python -m ipykernel install --user --name "Video Game Sales" --display-name "Python (Video Game Sales)"
```

Then select the new kernel in Jupyter.

### Data File Not Found
**Problem:** `FileNotFoundError: './datasets/games.csv' not found`

**Solution:** Ensure you're running notebook from project root directory:
```bash
cd "/Users/scottroberts/Documents/Developer/Projects/Video Game Sales Analysis"
jupyter notebook
```

---

## Working with DSR Libraries

### Development Mode
If developing the DSR libraries locally:

1. Install with `-e` flag:
   ```bash
   pip install -e "/path/to/dsr-utils"
   ```

2. Make changes to the library source code
3. Changes automatically reflected in notebook (no reinstall needed)

### Import Verification
Test that libraries load correctly:
```python
from dsr_data_tools import analyze_dataset
from dsr_feature_eng_ml import DataSplits, ModelEvaluation

# Quick test
test_data = ...  # your data
results = analyze_dataset(test_data, generate_recs=True)
```

---

## Best Practices

### Virtual Environment
- Always activate venv before working: `source venv/bin/activate`
- Never modify files in venv/ directly
- Use `pip freeze > requirements.txt` to track changes

### Git Workflow
```bash
# Before starting
git pull origin main

# Work on notebook...

# When ready to save
git add .
git commit -m "Descriptive message"
git push origin main
```

### Notebook Organization
- Keep markdown cells for section headers
- One task per code cell
- Use descriptive variable names
- Add comments for complex logic

---

## Performance Tips

### Faster Model Evaluation
- Reduce `n_iter` in `ModelEvaluation` for quick tests
- Use smaller data subsets for prototyping
- Set `n_jobs=-1` to use all CPU cores

### Memory Optimization
- Close other applications before running
- Consider filtering dataset for large operations
- Monitor memory with: `ps aux | grep python`

---

## Additional Resources

- [Jupyter Documentation](https://jupyter.org/documentation)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

Last Updated: December 18, 2025
