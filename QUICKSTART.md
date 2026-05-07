# Quick Start Guide - CWF Assignment

## 📋 Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- Jupyter Lab or VS Code with Jupyter extension
- Internet connection (for first-time data download)

## 🚀 Quick Setup (5 minutes)

### Option 1: Using pip (Recommended)

```powershell
# 1. Navigate to project directory
cd "c:\Users\rajit\OneDrive\Documents\sdgai\c1339c"

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Start Jupyter Lab
jupyter lab
```

### Option 2: Using conda

```powershell
# 1. Navigate to project directory
cd "c:\Users\rajit\OneDrive\Documents\sdgai\c1339c"

# 2. Create conda environment
conda create -n ai-course python=3.10

# 3. Activate environment
conda activate ai-course

# 4. Install dependencies
conda install --file requirements.txt -y

# 5. Start Jupyter Lab
jupyter lab
```

## 📖 Running the Notebook

1. **Open Jupyter Lab** (should open automatically)
2. **Select kernel:** Python 3 (or the environment you created)
3. **Run Setup Cell:** Run the "Data Fetch Utility" cell first (Cell 4)
4. **Run Question Cells:** Run Q1, Q2, Q3, Q4 in sequence
5. **Expected Output:**
   - Q1: Summary statistics tables
   - Q2: Price analysis and comparisons
   - Q3: Two professional charts with trends
   - Q4: Reflective report

## 📁 Project Contents Checklist

```
✅ CWF_C1339C_6676831V_WADUGERAJITHNISHADAWADUGE.ipynb  (Main notebook)
✅ hdb_cache/BISHAN.json                                 (Bishan data - auto-cached)
✅ hdb_cache/TAMPINES.json                               (Tampines data - auto-cached)
✅ requirements.txt                                       (Dependencies)
✅ README.md                                              (Full documentation)
✅ QUICKSTART.md                                          (This file)
✅ .gitignore                                             (Git ignore rules)
```

## 🔍 What Each Cell Does

| Cell | Description | Status |
|------|-------------|--------|
| 1-2 | Header & Setup Instructions | ℹ️ Read-only |
| 3 | Data Fetch Utility Function | ⚙️ **RUN FIRST** |
| 4 | Import Statements | ✅ Required |
| 5-6 | Q1: Load & Prepare Data | 📊 Main task |
| 7-8 | Q2: Analyse Data | 📈 Analysis |
| 9-10 | Q3: Visualise Data | 📉 Charts |
| 11-12 | Q4: Reflective Report | 📝 Written |
| 13 | Pre-Submission Checklist | ✓ Verification |

## ⚡ Common Commands

```powershell
# Verify Python is installed
python --version

# Check installed packages
pip list

# Upgrade pip
python -m pip install --upgrade pip

# Install missing package
pip install package_name

# Deactivate virtual environment
deactivate
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | Run `pip install -r requirements.txt` again |
| Data won't download | Check internet; delete `hdb_cache` and retry |
| Jupyter not found | Ensure you activated the environment |
| Kernel error | Restart kernel: Kernel → Restart Kernel |
| Port already in use | Run `jupyter lab --port 8889` |

## 📊 Expected Output Summary

**Q1 Output:**
- 🔹 Bishan: ~430 records
- 🔹 Tampines: ~650 records
- 🔹 Data types properly converted

**Q2 Output:**
- 🔹 Price statistics (Mean, Median, Std Dev)
- 🔹 Price by flat type breakdown
- 🔹 Price per sqm analysis
- 🔹 Written comparison (3+ observations)

**Q3 Output:**
- 🔹 Main chart: Bishan 4-room & 5-room with LOWESS trends
- 🔹 Bonus chart: Bishan vs Tampines 4-room comparison
- 🔹 Professional formatting with legends and labels

**Q4 Output:**
- 🔹 300-400 word reflective report
- 🔹 Problem-solving approach
- 🔹 Package usage explanation
- 🔹 Code quality notes
- 🔹 Data insights and findings

## ✅ Pre-Submission Checklist

Run through this before final submission:

- [ ] All cells execute without errors (Kernel → Restart & Run All)
- [ ] Q1 summary statistics visible
- [ ] Q2 comparison table with 3+ observations
- [ ] Q3 charts display correctly
- [ ] Q4 report is 250-500 words
- [ ] No placeholder text remaining
- [ ] File name matches: `CWF_C1339C_6676831V_WADUGERAJITHNISHADAWADUGE.ipynb`
- [ ] Student name and ID correct
- [ ] AI usage declaration checked
- [ ] PEP 8 guidelines followed

## 🔗 Resources

- 📚 [Pandas Documentation](https://pandas.pydata.org/docs/)
- 🔢 [NumPy Documentation](https://numpy.org/doc/)
- 📉 [Matplotlib Documentation](https://matplotlib.org/)
- 📊 [Seaborn Documentation](https://seaborn.pydata.org/)
- 🏠 [HDB Data](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view)

## 💡 Pro Tips

1. **First run takes longer:** Data download is cached, subsequent runs are instant
2. **Modify town names:** Change `BISHAN` and `TAMPINES` to any valid Singapore town
3. **Customize analysis:** Feel free to add more visualizations or analysis
4. **Save often:** Jupyter auto-saves, but manually save before closing
5. **Check results:** Always verify your statistics make sense

## 🎯 Success Indicators

✅ You're on track if:
- Notebook runs top-to-bottom without errors
- Charts display with proper formatting
- Statistics are logically presented
- Written analysis is coherent and data-supported

---

**Good luck with your assignment! 🚀**

*Last updated: May 6, 2026*
