# fermat-moduli-factoring-circuits - Experimental Baseline for Shor's Order-Finding on NISQ Hardware

This repository contains the source code, experimental framework, and raw data for the paper: **"Factoring some integers using Shor's Algorithm on real quantum hardware"**.

This project provides a transparent, reproducible baseline for evaluating the impact of hardware noise and circuit depth on quantum order-finding routines. By targeting moduli composed of Fermat primes ($N \in \{51, 85, 255, 771\}$), we structurally simplify the modular exponentiation multipliers to bit-shifts and identities.

## Repository Structure

* `factoring_51.ipynb` to `factoring_771.ipynb`: Self-contained Jupyter Notebooks. Each file constructs the explicit modular exponentiation circuit, runs the Inverse Quantum Fourier Transform (IQFT), and executes the classical continued fractions post-processing for its respective modulus.
* `pipeline.py`: The core automation script using `papermill`. It dynamically injects parameters (such as `QFT_SIZE`, `SHOTS_PER_RUN`, and `BACKEND_NAME`) into the notebooks, executing a sweeping matrix of tests across different IBM Quantum backends until the noise threshold is reached.
* `execs_*.txt`: Automated log files generated during execution. These files contain a historical record of all hardware runs, capturing transpiled circuit depth, exact gate counts (e.g., `cx`, `rz`), backend calibration timestamps, Hellinger fidelities, and dual success rates (Total and Expected Peak).
* `execution_checkpoint.json`: A dynamically generated state-saver file that allows the automation to resume exactly where it left off in case of API timeouts or network failures.
* `requirements.txt`: Pinned Python dependencies to guarantee transpiler and environment reproducibility (Qiskit 1.0+, IBM Runtime, and Papermill).
* `.gitignore`: Configured to prevent accidental uploads of API tokens, execution checkpoints, and local caches.

## Key Features & Methodology

To ensure maximum statistical rigor and address the stochastic nature of quantum execution, this framework includes:

1. **Automated Parameter Sweeping:** The orchestration script autonomously scales the QFT size bit by bit until the hardware noise threshold overtakes the signal, providing a clear degradation curve.
2. **Dual Success Metrics:** Beyond measuring the *Hellinger Fidelity* of the phase distribution, the post-processing evaluates both the **Total Success Rate** (overall hardware performance) and the **Expected Peak Success Rate** (algorithmic efficiency on theoretically valid states).
3. **Statistical Variance:** Executions are batched (Standard, High Precision, and Fast Tests) to calculate mean and standard deviation across runs, allowing for precise error bars.
4. **Reproducible Compilation:** All transpiler calls are strictly seeded (`seed_transpiler = 42`) with predefined optimization levels.

## Prerequisites

To run these notebooks locally or execute them on IBM's hardware, you will need:

* Python 3.10+
* An active [IBM Quantum](https://quantum-computing.ibm.com/) account.

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gdhfontoura/fermat-moduli-factoring-circuits.git
   cd fermat-moduli-factoring-circuits
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

   > **Note:** The `.env` file is heavily git-ignored to keep your credentials secure. Never hardcode your token directly into the notebooks.

## Usage

### Option A: Automated Matrix Execution (Recommended)

To run the full suite of experiments across multiple backends and QFT sizes, simply execute the orchestrator. It will automatically handle batching, scaling, and logging.

```bash
python pipeline.py
```

> If the execution is interrupted by a timeout or network error, simply rerun the command. The script will read the `execution_checkpoint.json` file and safely resume from the exact batch that failed.

### Option B: Manual Execution

If you prefer to test a specific modulus manually, launch Jupyter Notebook or JupyterLab:

```bash
jupyter notebook
```

Open any of the `factoring_*.ipynb` files, set your desired parameters in the tagged parameter cell (e.g., `NUM_RUNS`, `SHOTS_PER_RUN`, `QFT_SIZE`, `BACKEND_NAME`), and execute the cells sequentially.

When the execution cell is triggered, the code will automatically authenticate using your `.env` token, batch the jobs to the designated IBM Quantum backend, and output the mathematical distribution. Upon completion, it will automatically append the results, success rates, and hardware metadata to the respective `execs_N.txt` log file.

## Authors & Acknowledgments

**Guilherme da Hora Andrade Fontoura, Fábio Gomes dos Santos, Luis Antonio Kowada, Vitor Pio Silva, Gabriela Pinheiro, Jose Victor Soares Scursulim, Samuraí Brito**

*Universidade Federal Fluminense (UFF), Instituto de Computação, Niterói, RJ, Brasil.*  
*Instituto de Ciência e Tecnologia Itaú (ICTi), São Paulo, Brasil.*