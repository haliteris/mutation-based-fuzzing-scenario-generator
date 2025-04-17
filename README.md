# Mutation-based Scenario Fuzzer

## Overview
The **Mutation-based Scenario Fuzzer-v2** is a tool designed to generate mutated scenarios for the CARLA simulator. This fuzzer utilizes predefined scenarios from EURONCAP and SafetyPool as a base, mutates their parameters, and logs the changes for further analysis. The tool is versatile, allowing customization of the number of iterations and directory paths for input and output files.

This tool was developed as a study which was funded by the Ministry of Science, Research, and the Arts of the Federal State of Baden-Württemberg as part of the financial support for the project SdMobi5—TESSOF within the Innovation Campus Mobility of the Future. For more details: https://www.icm-bw.de/forschung/projektuebersicht/detailseite/sdmobi5-tessof

The paper is accepted and results are shared in:https://www.sae.org/publications/technical-papers/content/2025-01-0297/

---

## Repository Structure

```plaintext
├── log_files/
│   ├── Contains the log files of the mutated scenarios, including:
│       - Mutated parameters
│       - Details of the changes
│       - Log file IDs
├── mutated_scenarios/
│   ├── Directory for the mutated scenario output files.
├── parent_scenarios/
│   ├── Contains the main scenarios prepared from EURONCAP and SafetyPool.
├── src/
│   ├── json_parser.py        # Reads, writes, and saves JSON files.
│   ├── args_parser.py        # Enables terminal execution using argparse.
│   ├── scenario_mutator.py   # Main script for generating mutated scenarios.
│   ├── requirements.py       # Manages dependencies (currently argparse only).
```

# Prerequisites

    Python Version: 3.9.18

# Install dependencies:

- pip install -r requirements.txt

# Usage

The mutation process is controlled through terminal commands. Customize the number of iterations and directory paths as needed.

Command Syntax:

```bash
python scenario_mutator.py --iter [Custom iteration number] --parent_path [directory_of_parent_json] --mutated_path [directory_of_output_json] --log_file_directory [directory_of_log_files]
```

## Example Command:

```bash
python scenario_mutator.py --iter 600 --parent_path /My-Directories/git/Mutation-based-Scenario-Generator-v2/parent_scenarios/logical_scenario_testcase_1.json --mutated_path /My-Directories/git/Mutation-based-Scenario-Generator-v2/mutated_scenarios --log_file_directory /My-Directories/git/Mutation-based-Scenario-Generator-v2/log_files
```

### Output Details
- **Log Files**: Stored in the `log_files` directory with details of mutations and changes.
- **Mutated Scenarios**: Saved in the `mutated_scenarios` directory, ready for CARLA simulation.

## Features

- **Customizable Mutations**: Adjust iteration count and directory paths with command-line arguments.
- **Logging**: Generate detailed log files tracking all mutations.
- **Compatibility**: Designed for integration with CARLA simulator for autonomous driving scenario testing.

## Author
**Halit Eriş, Research Assistant, Chair of Software Engineering, Technical University of Munich, halit.eris@tum.de**
