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

- Energy efficiency is considered a foremost challenge to increase the lifetime of a WBAN. ([bjbas.springeropen.com](https://bjbas.springeropen.com/articles/10.1186/s43088-020-00064-w?utm_source=chatgpt.com))  
- Sensor nodes in WBANs are battery-operated and require energy optimization to prolong their operational lifespan. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9370863/?utm_source=chatgpt.com))  
- Optimized energy consumption reduces the need for frequent battery replacement or recharging, enhancing user comfort and compliance. ([arxiv.org](https://arxiv.org/abs/2109.14546?utm_source=chatgpt.com))  
- Low-power operation enables continuous health monitoring for patients with chronic conditions. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC8786514/?utm_source=chatgpt.com))  
- Efficient energy usage reduces heat generation, improving patient safety and device reliability. ([link.springer.com](https://link.springer.com/article/10.1007/s11277-023-10361-z?utm_source=chatgpt.com))  
- Energy-optimized protocols lower overall network expenditures and maintenance costs. ([onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/full/10.1002/eng2.12841?utm_source=chatgpt.com))  
- Sustainable energy management in WBANs is critical for long-term deployment in wearable medical devices. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S2352484722005613?utm_source=chatgpt.com))  
- Energy optimization supports scalability in multi-sensor systems for comprehensive physiological monitoring. ([researchgate.net](https://www.researchgate.net/publication/357884276_Energy_Efficiency_and_Reliability_Considerations_in_Wireless_Body_Area_Networks_A_Survey?utm_source=chatgpt.com))  
- Minimizing energy consumption aligns with IoT green networking goals. ([link.springer.com](https://link.springer.com/article/10.1007/s11277-019-06651-0?utm_source=chatgpt.com))  
- Reducing energy use decreases the environmental impact of disposable or short-lived devices. ([arxiv.org](https://arxiv.org/abs/1910.05444?utm_source=chatgpt.com))  

By focusing on energy optimization, this project addresses these critical challenges—extending device lifetime, enhancing patient safety, and supporting sustainable, scalable health monitoring solutions.

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
