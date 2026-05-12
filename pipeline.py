import papermill as pm
import json
import os
import re

Ns = [51, 85, 255, 771]
backends = ['ibm_kingston']

batches = [
    {"id": "batch_1_standard", "runs": 5, "shots": 1024},
    {"id": "batch_2_high_precision", "runs": 5, "shots": 4096},
    {"id": "batch_3_fast_test", "runs": 1, "shots": 5}
]

CHECKPOINT_FILE = "execution_checkpoint.json"
NOISE_THRESHOLD = 1.0 

if os.path.exists(CHECKPOINT_FILE):
    with open(CHECKPOINT_FILE, "r") as f:
        completed_executions = json.load(f)
else:
    completed_executions = {}

def extract_latest_rate(file_path):
    if not os.path.exists(file_path):
        return 0.0
    with open(file_path, "r", encoding="utf-8") as f:
        for line in reversed(f.readlines()):
            if "Total Success Rate =" in line:
                m = re.search(r"Total Success Rate = ([\d\.]+)%", line)
                if m:
                    return float(m.group(1))
    return 0.0

print("Starting Automation...")

active_configs = { (N, backend): True for N in Ns for backend in backends }
qft_offset = 0

while any(active_configs.values()):
    print(f"\n{'='*50}")
    print(f"Starting execution block for QFT Offset: +{qft_offset}")
    print(f"{'='*50}")
    
    for N in Ns:
        for backend in backends:
            if not active_configs[(N, backend)]:
                continue
                
            qft_size = (5 if N == 771 else 4) + qft_offset
            success_rates = []
            
            for batch in batches:
                run_id = f"N{N}_QFT{qft_size}_{backend}_{batch['id']}"
                
                if run_id in completed_executions:
                    print(f"Skipping {run_id} - Already executed (Rate: {completed_executions[run_id]}%)")
                    success_rates.append(completed_executions[run_id])
                    continue
                    
                print(f"\nExecuting {run_id}...")
                
                try:
                    pm.execute_notebook(
                        f"factoring_{N}.ipynb",
                        f"factoring_{N}_executed.ipynb",
                        parameters=dict(
                            NUM_RUNS=batch['runs'],
                            SHOTS_PER_RUN=batch['shots'],
                            OPT_LEVEL=3,
                            SEED_TRANSPILER=42,
                            QFT_SIZE=qft_size,
                            BACKEND_NAME=backend
                        )
                    )
                    
                    rate = extract_latest_rate(f"execs_{N}.txt")
                    completed_executions[run_id] = rate
                    
                    with open(CHECKPOINT_FILE, "w") as f:
                        json.dump(completed_executions, f)
                        
                    success_rates.append(rate)
                    print(f"Success! Recorded rate: {rate}%")
                    
                except Exception as e:
                    print(f"\nCRITICAL ERROR in {run_id}. Pausing automation.")
                    exit(1)
            
            if not success_rates or max(success_rates) < NOISE_THRESHOLD:
                print(f"\n>>> Noise threshold reached for {backend} with N={N} (QFT={qft_size}). Stopping increments for this combination. <<<\n")
                active_configs[(N, backend)] = False
                
    qft_offset += 1

print("\nAll matrix executions have been completed")