# fermat-moduli-factoring-circuits - Experimental Baseline for Shor's Order-Finding on NISQ Hardware

This repository contains the source code and experimental data for the paper: **"Factoring some integers using Shor's Algorithm on real quantum hardware"**.

This project provides a transparent, reproducible baseline for evaluating the impact of hardware noise and circuit depth on quantum order-finding routines. By targeting moduli composed of Fermat primes ($N \in \{51, 85, 255, 771\}$), we structurally simplify the modular exponentiation multipliers to bit-shifts and identities. This approach allows us to maintain explicit arithmetic circuits on near-term IBM superconducting hardware, isolating the signal degradation caused by accumulated gate errors without relying on black-box compilation shortcuts.

## Repository Structure

* `factoring_51.ipynb`: Circuit construction, execution, and phase extraction for $N=51$ ($A=2, r=8$).
* `factoring_85.ipynb`: Circuit construction, execution, and phase extraction for $N=85$ ($A=2, r=8$).
* `factoring_255.ipynb`: Circuit construction, execution, and phase extraction for $N=255$ ($A=2, r=8$).
* `factoring_771.ipynb`: Circuit construction, execution, and phase extraction for $N=771$ ($A=2, r=16$).
* `requirements.txt`: Python dependencies and Qiskit versioning.

## Prerequisites

To run these notebooks, you will need:
* Python 3.10+
* Qiskit (see `requirements.txt` for exact versions to ensure transpiler reproducibility)
* An active [IBM Quantum](https://quantum-computing.ibm.com/) account with access to the backends.

## Usage and Reproducibility

Each notebook is self-contained. To reproduce the experiments:
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Add your IBM Quantum API token in your local environment.
4. Execute the cells sequentially.


Universidade Federal Fluminense (UFF) & Instituto de Ciência e Tecnologia Itaú (ICTi).