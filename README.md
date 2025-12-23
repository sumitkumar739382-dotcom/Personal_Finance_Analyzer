# 📊 Personal Finance Analyzer

## 📌 Overview

**Personal Finance Analyzer** is a beginner-friendly Python project that analyzes **monthly personal expenses and work hours** using **descriptive and bivariate statistical methods**.

The project is developed in alignment with **B.Sc. Statistics Semester I (STAMJ11 – Descriptive Statistics)** and focuses on **manual implementation of statistical formulas**, without using external libraries such as **NumPy** or **Pandas**.

The main objective is to understand **how statistical theory is translated into Python logic**, rather than building a production-level finance application.

---

## 🎯 Objectives

* Analyze daily **expenses** and **work hours**
* Apply **measures of central tendency** (Mean, Median)
* Apply **measures of dispersion** (Standard Deviation, Min–Max)
* Study the **relationship between work hours and expenses** using correlation
* Strengthen understanding of **Python fundamentals** (functions, loops, conditionals)
* Build a foundation for **statistical computing**

---

## 📚 Syllabus Relevance (STAMJ11)

### Unit I – Data & Variables (Conceptual)

* Primary data collection through user input
* Quantitative and continuous variables
* Time-based (daily) observations aggregated monthly

### Unit III – Descriptive Statistics

**Measures of Central Tendency**

* Arithmetic Mean
* Median

**Measures of Dispersion**

* Variance (population-based)
* Standard Deviation
* Minimum and Maximum values

### Bivariate Data Analysis

* Covariance (internal computation)
* Pearson’s Product Moment Correlation Coefficient
* Interpretation of correlation using |r|

All computations are performed using **explicit mathematical formulas**, implemented step by step in Python.

---

## 🛠 Current Implementation

* **Language:** Python 3.x
* **Libraries Used:** None (pure Python)
* **Data Input:**

  * Daily expenses (₹)
  * Daily work hours
* **Data Structures:**

  * Dictionaries for date-wise input
  * Lists for statistical computation

### Statistical Methods Implemented

* Arithmetic Mean
* Median
* Standard Deviation (population)
* Minimum & Maximum
* Pearson Correlation Coefficient

The program generates a **monthly analytical report** summarizing expense behavior and its relationship with work hours.

---

## ▶ How to Run

1. Ensure **Python 3.x** is installed.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the script:

```bash
python finance_analyzer.py
```

---

## 🧪 Notes

* All statistical formulas use **population definitions** (division by *N*).
* A sentinel input (`13`) is used during testing to exit early and avoid repeated data entry.
* The project is designed to be **incrementally extensible** as new concepts are learned.

---

## 🚀 Future Scope

As learning progresses, this project may be extended to include:

* Measures of skewness and kurtosis
* Simple linear regression and prediction

---

## 📌 Disclaimer

This project is intended for **academic learning and practice**.
It prioritizes **clarity and conceptual understanding** over optimization or real-world financial planning.
