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

#### Add SLiM to your bashrc/zshrc
Add the following block to your bashrc/zshrc, depending on which shell you prefer:
```
slim() {
    /your/path/to/slim $1
}
```

### Script Generation
There are two entry points to generate scripts: single_generator_entry and multiple_generator_entry. To generate scripts, run `python3 <script name>.py <flags>` within the script_generator directory. For a quick description of each flag, run `python3 multiple_generator_entry.py -h`. 
Example:
```
python3 multiple_generator_entry.py -d ../scripts -n 30 -s 1044878 -mr 0.00000001 -cr 0.00095 -ml 0.00000002 -cl 0.00105 -rr 0.00000001 -rl 0.00000002 -pl 10000 -pr 10000 -lll 0 -llr 2500 -lrl 50000 -lrr 52500 -gl 100000 -gr 100000 -dl 0.5 -dr 0.5
```


### Run Simulation
Make a copy of run_scripts_parallel.bash in the scripts directory created by the script generator, then run that copy.
