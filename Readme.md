# WBAN Optimization

Wireless Body Area Networks (WBANs) consist of sensor nodes placed on or around the human body to monitor vital signs and other physiological data. This repository implements and compares energy consumption in WBANs using both non-genetic and genetic algorithms. In addition, it includes a simple interactive website showcasing the simulation results.

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

## 📁 Repository Structure

WBAN-Optimization/             # Root directory
 - ├── Architecture Design-01.pdf # System design diagrams
 - ├── Documents/                 # Supporting documentation and notes
 - ├── Notes/                     # Experimental observations and logs
 - ├── Energy without GA.py       # Non-genetic energy model implementation
 - ├── Engergy Using GA.py        # GA-based energy model (no dataset)
 - ├── Genetic Algorithm without DataSet.py
 - ├── Genetic Algorithm with DataSet.py
 - ├── carbon_nanotubes.csv       # Sample dataset for GA convergence tests
 - ├── Website/                   # Interactive front-end & backend for web demo
 - │ ├── index.html               # Landing page and input form
 - │ ├── energycode.py            # Backend energy computation script
 - │ └── result.html              # Displays computed energy values
 - └── README.md                  # ← This file


## 📌 Why This Matters

Optimizing energy consumption in WBANs is more than a technical objective—it’s critical for enabling efficient, safe, and sustainable health monitoring. Here's why:

- 🩺 **Prolongs Device Life**  
  Energy-efficient nodes increase battery longevity, allowing for longer operation without maintenance. [[1]](https://bjbas.springeropen.com/articles/10.1186/s43088-020-00064-w)

- 🔋 **Reduces Battery Dependence**  
  Minimizes the need for frequent battery replacements or recharges, especially in hard-to-reach implantables. [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9370863/)

- 😊 **Improves User Comfort**  
  Less frequent interactions and smoother operation enhance patient comfort and usability. [[3]](https://arxiv.org/abs/2109.14546)

- 🏥 **Supports Continuous Monitoring**  
  Enables long-term monitoring of vital signs in patients with chronic conditions or during recovery. [[4]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8786514/)

- 🌡️ **Enhances Safety**  
  Lower energy usage means reduced heat dissipation, making devices safer for long-term skin contact. [[5]](https://link.springer.com/article/10.1007/s11277-023-10361-z)

- 💸 **Lowers Maintenance Costs**  
  Less frequent intervention translates to significant cost savings in large-scale medical deployments. [[6]](https://onlinelibrary.wiley.com/doi/full/10.1002/eng2.12841)

- 🌱 **Fosters Sustainability**  
  Energy-aware designs reduce electronic waste and align with eco-conscious health tech practices. [[7]](https://www.sciencedirect.com/science/article/pii/S2352484722005613)

- 🧪 **Scales with Complexity**  
  Optimization makes it feasible to deploy more nodes without exponential increases in power needs. [[8]](https://www.researchgate.net/publication/357884276_Energy_Efficiency_and_Reliability_Considerations_in_Wireless_Body_Area_Networks_A_Survey)

- 🌍 **Aligns with Green IoT Goals**  
  WBANs are part of the broader Internet of Things, where energy efficiency is key. [[9]](https://link.springer.com/article/10.1007/s11277-019-06651-0)

- ♻️ **Minimizes Waste**  
  Efficient energy use leads to longer device lifespans, which reduces medical tech turnover and environmental impact. [[10]](https://arxiv.org/abs/1910.05444)

This project directly tackles these concerns, advancing both practical performance and sustainable design in next-generation healthcare monitoring.
