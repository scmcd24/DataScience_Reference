
# SLURM - Basics

#### Useful Commands:
 - Show current node usage (short): ```sinfo``
 - Show current node useage (long): ```scontrol show nodes```
 - Show cpu per node: ```sinfo -o "%g %.10R %.20l %.10c"```
 - Go to node where job is running: ```ssh $nodename```
    - Semi-useful if you want to see what modules are installed there
 - List running jobs: ```squeue --me``` or ```squeue -u $USER```
 - List jobs running/run today: ```sacct```
 - Cancel job: ```scancel $jobid``` or cancel all jobs: ``` 

 - Launching jobs:
    - interactive job, sbatch, srun, job script
    - Interactive job (gpu):
        ```srun --partition=gpuq \```
        ```--time=00:10:00 \```
        ```--gres=gpu:1 \```
        ```--pty /bin/bash -i```
    - Launch job from terminal (cpu)
        ```cmd='echo "$my_name"` 
        ```sbatch -J 'jobname' \```
        ```-N 1 \```
        ```--time=00:03:00 \```
        ```--mem-per-cpu=8000 \```
        ```——out='jobname.out.txt' \```
        ```—error='jobname.err.txt' \```
        ```wrap="$cmd"```
 - Job behaviors:
    - Write to sterr: ```echo "Last executed line: $LINENO" >&2```

#### Defined commands (my fav):
 - sacctl: sacctl, but format as list and ignore non-helpful batch/extern jobs: 
    ```alias sacctl="sacct --format=JobName%40,State,Start,JobID%10 | grep -Ev 'batch|extern'"```
 - swatch: opens a terminal window, prints running jobs every 2 seconds
    - Ctrl+C to exit
    ```alias swatch="watch \"squeue --me --format='%.18i %.9P %.30j %.8u %.2t %.10M %.6D %R' \" "```
 - sscancel: cancels all jobs with names that are NOT 'sbatch'
    ```alias sscancel="squeue --me --noheader | grep -v 'sbatch' | awk '{print \$1}' | xargs -I {} scancel {}"```
    - sbatch: default name for cron jobs, don't want to cancel those/ forget to
      restart them every time we cancel jobs