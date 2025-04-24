# WBAN Optimization

Wireless Body Area Networks (WBANs) connect sensor nodes on or around the human body to monitor vital signs and other physiological data. This repository implements and compares energy consumption in WBANs using both non-genetic and genetic algorithms, and provides an interactive Flask-powered website to visualize the results.

## 🔍 Project Overview

- **Energy Models**  
  - **Non-Genetic Algorithm**: Uses a fixed‐distance model where  
    ```text
    energy = power_constant × distance
    ```  
  - **Genetic Algorithm**: Evolves node positions over generations to minimize total energy.  

- **Data & Code**  
  - Core routines in `energycode.py` for both models.  
  - Sample dataset (`carbon_nanotubes.csv`) for GA testing.  

- **Website**  
  - Frontend in HTML/CSS/JS.  
  - Backend in Flask (`energycode.py`).  
  - Compare non-GA vs. GA side-by-side with interactive charts.

## 📁 Repository Structure

```text
WBAN-Optimization/                    # Root directory
├── Architecture Design-01.pdf        # System design diagrams
├── Documents/                        # Supporting docs and notes
├── Notes/                            # Experimental observations and logs
├── Energy without GA.py              # Non-genetic energy model
├── Engergy Using GA.py               # GA-based model (no dataset)
├── Genetic Algorithm without DataSet.py
├── Genetic Algorithm with DataSet.py
├── carbon_nanotubes.csv              # Sample dataset
├── Website/                          # Interactive web application
│   ├── src/
│   │   ├── css/
│   │   │   ├── index.css             # Styles for index.html
│   │   │   ├── page2.css             # Styles for page2.html
│   │   │   └── result.css            # Styles for result.html
│   │   └── js/
│   │       ├── effect.js             # UI effects
│   │       ├── effect2.js            # Secondary UI effects
│   │       ├── result.js             # Chart rendering logic
│   │       └── script.js             # Form handling and AJAX
│   ├── energycode.py                 # Flask backend & energy routines
│   ├── index.html                    # Landing page & input form
│   ├── page2.html                    # Extended parameter page
│   └── result.html                   # Displays non-GA vs. GA charts
└── README.md                         # ← This file
