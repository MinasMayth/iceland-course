# Lab 1 — Judoor & HPC Access (2 hours)

**Notebook:** [notebooks/iceland-ml/lab1_judoor_hpc_access.ipynb](../../notebooks/iceland-ml/lab1_judoor_hpc_access.ipynb)

## ⏱️ Time Allocation (2 hours)
- **15 min:** Introduction + Judoor account setup
- **30 min:** SSH key configuration and first connection
- **30 min:** Filesystem exploration and SLURM basics
- **25 min:** Hands-on exercises and troubleshooting
- **15 min:** Advanced topics (optional) + Q&A
- **5 min:** Wrap-up and next steps

## Goals
### Core (Essential)
- Activate Judoor account and join training project
- Configure SSH keys and connect to JURECA
- Understand home/project/scratch layout
- Create workspace directory structure

### Optional (Time Permitting)
- Explore SLURM job submission basics
- Test interactive vs batch jobs
- Configure SSH config file for easier access
- Set up tmux/screen for persistent sessions

## Outputs
### Required
- Working SSH access to JURECA
- Workspace directories created under project/scratch
- SSH config file (optional but recommended)

### Bonus
- SLURM sanity checks completed
- Sample batch job submitted
- Terminal multiplexer configured

## 📚 Session Structure

### Part 1: Setup (45 min)
1. **Judoor Account** (15 min)
   - Create account at https://judoor.fz-juelich.de
   - Join `training2600` project
   - Verify email and access

2. **SSH Keys** (30 min)
   - Generate SSH key pair (ed25519 recommended)
   - Add public key to Judoor
   - Test SSH connection to JURECA
   - **Troubleshooting:** Common connection issues

### Part 2: HPC Environment (45 min)
3. **Filesystem Layout** (20 min)
   - HOME vs PROJECT vs SCRATCH
   - Storage quotas and performance
   - Create workspace structure
   - **Exercise:** Navigate and check disk usage

4. **SLURM Basics** (25 min)
   - Job scheduler overview
   - Basic commands: `squeue`, `sinfo`, `sbatch`, `srun`
   - Check partition availability
   - **Exercise:** Submit a test job

### Part 3: Advanced & Wrap-up (30 min)
5. **Optional Advanced Topics** (15 min)
   - SSH config file for aliases
   - Terminal multiplexers (tmux/screen)
   - File transfer methods (scp, rsync, Globus)
   - VS Code Remote SSH

6. **Hands-on Practice** (10 min)
   - Self-guided exercises
   - Partner troubleshooting

7. **Q&A and Next Steps** (5 min)

## 🎯 If You Finish Early
- Configure SSH config with jump hosts
- Set up VS Code Remote SSH connection
- Explore module system (`module avail`, `module load`)
- Practice advanced SLURM features (job arrays, dependencies)
- Set up bash aliases for common commands

## ✂️ If Running Out of Time
**Priority 1 (Must Complete):**
- Judoor account active
- SSH connection working
- Basic directory structure created

**Can Skip:**
- Detailed SLURM tutorial (provide cheat sheet)
- SSH config file (can do later)
- Terminal multiplexers

**Minimal Viable Lab:**
- Get everyone connected via SSH (60 min)
- Create workspace directories (15 min)
- Quick filesystem tour (15 min)
- Assign SLURM tutorial as homework (30 min saved)
