# Population Generator Recent Frequency-Dependent Balancing Selection
## Overview
This tool uses SLiM 3 (Haller, Messer 2019) to simulate populations undergoing recent frequency-dependent selection.

## Usage
If you have previously used the tool, please skip to Script Generation. This tool is meant for Unix-based systems, but should also work in Windows with proper setup.

### Prerequisites/Setup

#### Install Python3
Follow the instructions on the Python documentation:
https://www.python.org/downloads/

#### Install SLiM
Follow the instructions in the SLiM Manual:
https://messerlab.org/slim/ > SLiM Manual > Installation


### Script Generation
The entry point to generating populations and their corresponding summary statistics is full_pipeline.py. To access descriptions of each flag, run `python3 full_pipeline.py -h`. 
In order to detach the processes from your current instance, prepend the command with nohup and append an & at the end, as shown below. This will allow the process to continue even after exiting the terminal.
As of now, the scripts will output in a directory named big_scripts (will be updated to user input). This directory will be structured as follows, with the summary statistics in the sum_stats folder, the generator scripts in each subdirectory, and the output VCF files in their corresponding subdirectory/output.
big_scripts/
├─ test1/
│  ├─ outputs/
├─ test2/
│  ├─ outputs/
├─ sum_stats/
Example:
```
nohup python3  full_pipeline.py -d test1 test2 -n 5 10 -s 894117536 -mr 0.0000001 0.0000001 -ml 0.00000008 0.00000008 -cl 0.00095 0.00045 -cr 0.00105 0.00055 -rr 0.00000001 0.00000001 -rl 0.00000002 0.00000002 0.00000002 -pl 1000 1000 -pr 1000 1000 -lll 1 490 -llr 20 510 -lrl 240 740 -lrr 260 760 -gl 1000 1000 -gr 1000 1000 -dl 0.5 0.5 -dr 0.5 0.5 -sd sum_stats %
```
