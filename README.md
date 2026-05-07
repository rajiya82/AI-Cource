# C1339C: Programming for Artificial Intelligence - CWF Assignment

## Project Overview

This project contains the Coursework assignment for **C1339C: Programming for Artificial Intelligence** (AY2026 Term 2). The assignment focuses on HDB resale price analysis in Singapore using real government data from data.gov.sg.

## Project Structure

```
c1339c/
├── CWF_C1339C_6676831V_WADUGERAJITHNISHADAWADUGE.ipynb  # Main assignment notebook
├── hdb_cache/                                            # Cache folder for downloaded data
│   ├── BISHAN.json                                       # Bishan HDB data
│   └── TAMPINES.json                                     # Tampines HDB data
├── requirements.txt                                      # Python dependencies
├── README.md                                             # This file
└── Lesson*/                                              # Course lesson materials
```

## Setup Instructions

### 1. Install Dependencies

Using pip:
```bash
pip install -r requirements.txt
```

Or using conda:
```bash
conda install numpy pandas matplotlib seaborn statsmodels requests jupyterlab -y
```

### 2. Run the Notebook

```bash
jupyter lab CWF_C1339C_6676831V_WADUGERAJITHNISHADAWADUGE.ipynb
```

Or use VS Code with the Jupyter extension.

## Dataset

The project uses Singapore HDB resale flat price data from **data.gov.sg** (July 2022 to present).

- **Data Source:** Singapore government open data API
- **Towns Analyzed:** Bishan and Tampines
- **Cache Location:** `hdb_cache/` folder
- **Auto-Download:** First run downloads data from the internet (~20-40 seconds), subsequent runs use cached JSON files for instant access

### Valid Town Names

ANG MO KIO, BEDOK, BISHAN, BUKIT BATOK, BUKIT MERAH, BUKIT PANJANG, BUKIT TIMAH, CENTRAL AREA, CHOA CHU KANG, CLEMENTI, GEYLANG, HOUGANG, JURONG EAST, JURONG WEST, KALLANG/WHAMPOA, MARINE PARADE, PASIR RIS, PUNGGOL, QUEENSTOWN, SEMBAWANG, SENGKANG, SERANGOON, TAMPINES, TOA PAYOH, WOODLANDS, YISHUN

## Assignment Questions

### Question 1: Load and Prepare HDB Data (20 marks)
- Download data for two Singapore towns
- Convert to pandas DataFrames
- Convert data types appropriately
- Display summary statistics

### Question 2: Analyse Data (30 marks + 5 bonus)
- Calculate price statistics (mean, median, std dev) using NumPy
- Analyze prices by flat type
- **Bonus:** Calculate price per square metre analysis

### Question 3: Visualise Data (20 marks + 5 bonus)
- Create professional matplotlib charts with LOWESS trend lines
- Show price trends by flat type
- **Bonus:** Compare towns using seaborn with 95% confidence intervals

### Question 4: Reflective Report (20 marks)
- Problem-solving approach
- Python packages used
- Code quality and structure
- Data insights and learning

## Code Standards

The project adheres to **PEP 8** style guidelines:
- 4 spaces per indentation level
- Max line length: 79 characters (code), 72 (comments/docstrings)
- One import per line
- `snake_case` for functions/variables, `UPPER_CASE` for constants
- Docstrings for all custom functions

## Key Packages

| Package | Purpose |
|---------|---------|
| **pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **matplotlib** | Chart creation and formatting |
| **seaborn** | Statistical data visualization |
| **statsmodels** | LOWESS smoothing for trend lines |
| **requests** | API requests for data download |

## Student Information

- **Student Name:** Waduge Rajith Nishada Waduge
- **Student ID:** 6676831V
- **Module:** C1339C: Programming for Artificial Intelligence
- **Term:** AY2026 Term 2
- **Submission Date:** 06 May 2026

## Academic Integrity

✅ **AI Usage Declared:** This project was completed with assistance from generative AI tools (GitHub Copilot).

## Running the Full Pipeline

```python
# The notebook handles everything automatically:
# 1. Imports all required libraries
# 2. Downloads/loads HDB data from cache
# 3. Performs statistical analysis
# 4. Generates visualizations
# 5. Provides interpretations

# Just run all cells: Shift + A (select all) → Shift + Enter (run all)
```

## Troubleshooting

### Cache Not Working
- Delete `hdb_cache/` folder and re-run cell 3 to re-download
- Ensure network connection is stable

### Missing Packages
```bash
pip install --upgrade -r requirements.txt
```

### Kernel Issues
Restart kernel in Jupyter: Kernel → Restart Kernel

## References

- [HDB Resale Dataset](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view)
- [data.gov.sg API Guide](https://guide.data.gov.sg/developers/api-v2)
- [PEP 8 Style Guide](https://pep8.org/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [matplotlib Documentation](https://matplotlib.org/)

---

*Created: May 6, 2026*
