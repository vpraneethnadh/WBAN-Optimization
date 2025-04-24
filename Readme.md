```markdown
# WBAN Optimization

Wireless Body Area Networks (WBANs) consist of sensor nodes placed on or around the human body to monitor vital signs and other physiological data. This repository implements and compares energy consumption in WBANs using both non-genetic and genetic algorithms, and provides an interactive website showcasing simulation results.

## 🔍 Project Overview

- **Energy Models**  
  - **Non-Genetic Algorithm**: Computes energy consumption per bit based on a fixed distance and power model.  
  - **Genetic Algorithm**: Evolves node positions to minimize total energy consumption.  

- **Data & Code**  
  - Python scripts for both approaches (see files at root).  
  - Sample dataset (`carbon_nanotubes.csv`) for testing GA convergence.  

- **Website**  
  - Interactive front-end to enter network parameters and visualize energy results.  
  - Located in the [`Website`](./Website) folder.

## 📌 Why This Matters

Optimizing energy consumption in WBANs is not just a technical challenge—it is essential for real-world applications in healthcare and beyond:

- 🩺 **Prolongs Device Life**: Energy-efficient designs extend the battery life of sensor nodes. [[1]](https://bjbas.springeropen.com/articles/10.1186/s43088-020-00064-w)
- 🔋 **Reduces Battery Dependence**: Minimizes the need for frequent recharging or replacement. [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9370863/)
- 😊 **Improves User Comfort**: Fewer disruptions increase patient comfort and compliance. [[3]](https://arxiv.org/abs/2109.14546)
- 🏥 **Supports Continuous Monitoring**: Enables long-term health tracking for chronic patients. [[4]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8786514/)
- 🌡️ **Enhances Safety**: Reduces heat generation for safer device operation. [[5]](https://link.springer.com/article/10.1007/s11277-023-10361-z)
- 💸 **Lowers Maintenance Costs**: Less frequent intervention lowers total network costs. [[6]](https://onlinelibrary.wiley.com/doi/full/10.1002/eng2.12841)
- 🌱 **Fosters Sustainability**: Promotes green practices in wearable medical tech. [[7]](https://www.sciencedirect.com/science/article/pii/S2352484722005613)
- 🧪 **Scales with Complexity**: Efficient energy use helps scale systems with many sensors. [[8]](https://www.researchgate.net/publication/357884276_Energy_Efficiency_and_Reliability_Considerations_in_Wireless_Body_Area_Networks_A_Survey)
- 🌍 **Aligns with Green IoT Goals**: Contributes to low-power, eco-friendly IoT. [[9]](https://link.springer.com/article/10.1007/s11277-019-06651-0)
- ♻️ **Minimizes Waste**: Less energy usage = fewer disposable or short-lived devices. [[10]](https://arxiv.org/abs/1910.05444)

By focusing on energy optimization, this project addresses these challenges—extending device lifetime, enhancing patient safety, and supporting sustainable, scalable health monitoring.

## 📁 Repository Structure

```
WBAN-Optimization/
├── Architecture Design-01.pdf    # System design diagrams
├── Documents/                   # Supporting docs and notes
├── Notes/                       # Experimental observations
├── Energy without GA.py         # Non-genetic energy model
├── Engergy Using GA.py          # GA-based model (without dataset)
├── Genetic Algorithm without DataSet.py
├── Genetic Algorithm with DataSet.py
├── carbon_nanotubes.csv         # Sample dataset
├── Website/                     # Front-end & backend code for website
└── README.md                    # ← You are here
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.7+  
- pip (Python package manager)

### Install Dependencies

```bash
pip install numpy pandas matplotlib
```

*(If you add more libraries, list them here or provide a `requirements.txt`.)*

### Running the Simulations

1. **Non-Genetic Model**  
   ```bash
   python "Energy without GA.py"
   ```

2. **Genetic Algorithm Model**  
   ```bash
   python "Genetic Algorithm with DataSet.py"
   ```

Each script will output energy consumption statistics to the console and/or generate plots in the working directory.

## 🌐 Website

To explore the interactive website:
Navigate to the [`Website`](./Website) folder.  

