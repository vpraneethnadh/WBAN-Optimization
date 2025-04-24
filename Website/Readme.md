# WBAN Optimization

Wireless Body Area Networks (WBANs) connect sensor nodes on or around the human body to monitor vital signs and other physiological data. This repository implements and compares energy consumption in WBANs using both non-genetic and genetic algorithms, and provides an interactive Flask-powered website to visualize the results.

## 🔍 Project Overview

- **Energy Models**  
  - **Non-Genetic Algorithm**: Uses a fixed-distance model where  
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
│   ├── energycode.py                 # Flask backend & energy routines
│   ├── index.html                    # Landing page & input form
│   ├── page2.html                    # Optional extra form/page
│   ├── result.html                   # Displays computed energy values
│   └── src/                          # Static assets
│       ├── css/
│       │   ├── index.css
│       │   ├── page2.css
│       │   └── result.css
│       └── js/
│           ├── effect.js
│           ├── effect2.js
│           ├── result.js
│           └── script.js
└── README.md                         # ← This file

## 📌 Why This Matters

Optimizing energy consumption in WBANs is critical for practical, safe, and sustainable health monitoring:

- 🩺 **Prolongs Device Life** — Extends battery lifespan for long-term deployments  
- 🔋 **Reduces Battery Dependence** — Fewer recharges/replacements increase reliability  
- 😊 **Improves User Comfort** — Minimizes interruptions and heat build-up  
- 🏥 **Supports Continuous Monitoring** — Enables chronic-care tracking without downtime  
- 🌡️ **Enhances Safety** — Lower dissipation reduces skin-contact risks  
- 💸 **Lowers Maintenance Costs** — Reduces operational expenses for large networks  
- 🌱 **Fosters Sustainability** — Aligns with eco-friendly, low-power IoT goals  
- 🧪 **Scales with Complexity** — Supports dense sensor deployments efficiently  
- 🌍 **Aligns with Green IoT** — Contributes to global low-power initiatives  
- ♻️ **Minimizes E-Waste** — Longer device lifespan lessens environmental impact  

## 🏁 Getting Started Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/vpraneethnadh/WBAN-Optimization.git
   ```
2. **Enter the Website folder**  
   ```bash
   cd WBAN-Optimization/Website
   ```
3. **Create & activate a virtual environment** (strongly recommended)  
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows PowerShell: venv\Scripts\activate
   ```
4. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up Flask environment**  
   ```bash
   export FLASK_APP=energycode.py        # Windows PowerShell: $env:FLASK_APP="energycode.py"
   export FLASK_ENV=development          # Enables debug & auto-reload
   ```
6. **Run the server**  
   ```bash
   flask run                             # Launches at http://127.0.0.1:5000/
   ```
7. **Open in your browser**  
   Visit `http://127.0.0.1:5000/` to interact!


## ⚙️ How It Works

1. **User Input** on `index.html` (form)  
2. **Backend Processing** (`energycode.py`):  
   - **Non-Genetic**:  
     ```python
     energy = power_constant × distance
     ```  
   - **Genetic Algorithm**:  
     Initializes a population of node layouts, evolves them over generations to minimize total energy.  
3. **Results Display**  
   - `/compute` returns JSON:  
     ```json
     {
       "non_genetic": [...],
       "genetic":    [...],
       "stats":      {"min":…, "max":…, "avg":…}
     }
     ```  
   - `result.html` & `src/js/result.js` render charts via Chart.js.

## 🎨 Customization

- **Styles**: Tweak `src/css/*.css`  
- **Charts**: Modify `src/js/*.js` (uses Chart.js)  
- **Algorithms**: Extend or swap functions in `energycode.py`
