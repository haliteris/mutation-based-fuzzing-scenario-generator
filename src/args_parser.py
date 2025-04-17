import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Run script from the terminal with the custom variables")
    parser.add_argument("--iter", type=int, required=True, help="Number of iterations")
    parser.add_argument("--parent_path", type=str, required=True, help="Directory of the parent scenario file")
    parser.add_argument("--mutated_path", type=str, required=True, help="Directory to save mutated outputs")
    parser.add_argument("--log_file_directory", type=str, required=True, help="Directory to save log files")
    return parser.parse_args()