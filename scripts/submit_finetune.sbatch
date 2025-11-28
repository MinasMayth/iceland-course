#!/bin/bash
# Example Slurm script for TerraTorch fine-tuning
# Adjust placeholders (<...>) to your HPC environment (e.g., JSC/JURECA/Booster).

#SBATCH --job-name=iceland-ft
#SBATCH --account=<project_id>
#SBATCH --partition=<gpu_partition>
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err

set -euo pipefail
mkdir -p logs runs/iceland

# Optional: load modules (example)
# module purge
# module load CUDA/12.1 Python/3.10

# Activate environment
# If using venv:
# source .venv/bin/activate
# Or conda:
# source ~/miniconda3/etc/profile.d/conda.sh
# conda activate iceland-ml

# Environment knobs
export WANDB_MODE=offline
export TOKENIZERS_PARALLELISM=false

# Ensure requirements are installed (optional, prefer prebuilt envs)
# pip install -r requirements.txt

# Launch training
CONFIG=${CONFIG:-configs/iceland.yaml}
OUTPUT_DIR=${OUTPUT_DIR:-runs/iceland}

echo "Starting training with $CONFIG -> $OUTPUT_DIR"

# If terratorch provides a CLI entrypoint named 'terratorch'
# srun terratorch train --config "$CONFIG" --output "$OUTPUT_DIR"

# Otherwise call your Python entrypoint
srun python -m terratorch.train --config "$CONFIG" --output "$OUTPUT_DIR"
