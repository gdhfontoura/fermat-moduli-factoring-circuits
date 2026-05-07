# fermat-moduli-factoring-circuits - Experimental Baseline for Shor's Order-Finding on NISQ Hardware

This repository contains the source code, experimental framework, and raw data for the paper: **"Factoring some integers using Shor's Algorithm on real quantum hardware"**.

This project provides a transparent, reproducible baseline for evaluating the impact of hardware noise and circuit depth on quantum order-finding routines. By targeting moduli composed of Fermat primes ($N \in \{51, 85, 255, 771\}$), we structurally simplify the modular exponentiation multipliers to bit-shifts and identities. 

## Repository Structure

* `factoring_51.ipynb` to `factoring_771.ipynb`: Self-contained Jupyter Notebooks. Each file constructs the explicit modular exponentiation circuit, runs the Inverse Quantum Fourier Transform (IQFT), and executes the classical continued fractions post-processing for its respective modulus.
* `execs_*.txt`: Automated log files generated during execution. These files contain a historical record of all hardware runs, capturing transpiled circuit depth, exact gate counts (e.g., `cx`, `rz`), backend calibration timestamps, Hellinger fidelities, and empirical order-finding success rates.
* `requirements.txt`: Pinned Python dependencies to guarantee transpiler and environment reproducibility (Qiskit 1.0+ and IBM Runtime).
* `.gitignore`: Configured to prevent accidental uploads of API tokens and local caches.

## Prerequisites

To run these notebooks locally or execute them on IBM's hardware, you will need:
* Python 3.10+
* An active [IBM Quantum](https://quantum-computing.ibm.com/) account.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Securely Configure your IBM Quantum Token:**
   Create a file named `.env` in the root directory of the project. Open it and add your IBM Quantum API token as follows:
   ```env
   IBM_QUANTUM_TOKEN=your_token_here
   ```
   *Note: The `.env` file is heavily git-ignored to keep your credentials secure. Never hardcode your token directly into the notebooks.*

## Usage

Launch Jupyter Notebook or JupyterLab:
```bash
jupyter notebook
```

Open any of the `factoring_*.ipynb` files and execute the cells sequentially. 

When the execution cell is triggered, the code will automatically authenticate using your `.env` token, batch the jobs to the designated IBM Quantum backend, and output the mathematical distribution. Upon completion, it will automatically append the results, success rates, and hardware metadata to the respective `execs_N.txt` log file.

## Authors & Acknowledgments

**Guilherme da Hora Andrade Fontoura, Fábio Gomes dos Santos, Luis Antonio Kowada, Vitor Pio Silva, Gabriela Pinheiro, Jose Victor Soares Scursulim, Samuraí Brito**

*Universidade Federal Fluminense (UFF), Instituto de Computação, Niterói, RJ, Brasil.* *Instituto de Ciência e Tecnologia Itaú (ICTi), São Paulo, Brasil.*
```