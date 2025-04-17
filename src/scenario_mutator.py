import json_parser
import random
import os
from args_parser import parse_args
from mutation_config import parameters_to_mutate_B, value_pools_firstgen

def absolution_method(min, max):
    # Generate a random value in the specified range
    random_value = random.uniform(min, max)
    
    # Ensure the value is non-negative
    mutant_value = abs(random_value)
    
    # If the absolute value exceeds the max, cap it at max
    if mutant_value > max:
        mutant_value = max
    
    return mutant_value

def sumproduct_method(min, max):
    # Generate a random integer within the range [min, max)
    random_value = random.uniform(min, max)  # Change to `random.uniform` to handle floats correctly.
    
    # First gen: Mutate the value by ±10%, Second gen: Mutate the value by ±15% of the mutated value
    mutant_value = random_value + random.uniform(-0.05 * random_value, 0.05 * random_value)
    
    # Check if the mutated value is within the bounds
    if min <= mutant_value < max:  # Use proper float comparison
        return mutant_value
    else:
        return random_value

def minmaxmid_method(min, max, include_mid=False):
    choices = [min, max]
    if include_mid:
        midpoint = (min + max) / 2
        choices.append(midpoint)
    mutant_value = random.choice(choices)
    return mutant_value

def flip_method(min, max):
    # Generate a random value within the range
    random_value = random.uniform(min, max)
    
    # Convert the float to a string to prepare for flipping
    value_str = f"{random_value:.10g}"  # Limits precision for consistency
    
    # Extract digits (ignoring the decimal point)
    digits = [c for c in value_str if c.isdigit()]  # Collect digits only
    if len(digits) < 2:
        raise ValueError("Not enough digits to flip.")  # Handle edge case
    
    # Randomly choose two indices to swap
    idx1, idx2 = random.sample(range(len(digits)), 2)
    
    # Swap the selected digits
    digits[idx1], digits[idx2] = digits[idx2], digits[idx1]
    
    # Reconstruct the flipped value as a string
    new_value_str = ""
    digit_index = 0
    for char in value_str:
        if char.isdigit():
            new_value_str += digits[digit_index]
            digit_index += 1
        else:
            new_value_str += char  # Add non-digit characters like '.'
    
    # Convert the flipped value back to float
    flipped_value = float(new_value_str)
    
    # Check if the flipped value is within the range
    if min <= flipped_value <= max:
        return flipped_value
    else:
        return random_value  # Return original value if flipped value is out of range

def setzero_method(min, max):
    # Check if 0 is within the range
    if min <= 0 < max:
        return 0
    else:
        return min

def invertsign_method(min, max):
    random_value = random.uniform(min, max)
    mutant_value = -random_value
    if min <= mutant_value < max:  # Use proper float comparison
        return mutant_value
    else:
        return random_value

def switchblock_weather(value_pools):
    # Access the list of strings for 'weather.Precipitation.precipitationType'
    weather_conditions = value_pools.get('weather.Precipitation.precipitationType', [])
    
    if not weather_conditions:
        raise ValueError("No string-based weather conditions found in the value pool.")
    
    mutant_weather = random.choice(weather_conditions)
    # Randomly select one of the weather conditions
    return mutant_weather


# Function to apply random mutations to parameters within specified value pools
def mutate_parameters(data, key_path, value_pool):
    new_value = mutate_value(data, key_path, value_pool)
    old_value = json_parser.change_parameter(data, key_path, new_value)
    return old_value, new_value

# Mutation function that respects value pools and ranges
def mutate_value(data, key_path, value_pool, sep='.'):
    keys = key_path.split(sep)
    sub_data = data

    # Traverse JSON to locate the target key
    for key in keys[:-1]:
        if key.isdigit():
            key = int(key)
        try:
            sub_data = sub_data[key]
            print(f"Accessing key '{key}': {sub_data}")  # Debugging line to check access
        except (KeyError, IndexError, TypeError) as e:
            print(f"Error accessing key '{key}' in {sub_data}: {e}")
            raise

    last_key = keys[-1]
    if last_key.isdigit():
        last_key = int(last_key)

    # Check if the last key exists before accessing it
    if last_key not in sub_data:
        print(f"Error: Last key '{last_key}' not found in {sub_data}")
        raise KeyError(f"Key '{last_key}' not found")

    value = sub_data[last_key]

    # Helper function to apply mutations
    def apply_mutation(value, min_value, max_value):
        return random.choice([
            absolution_method(min_value, max_value),
            sumproduct_method(min_value, max_value),
            minmaxmid_method(min_value, max_value),
            flip_method(min_value, max_value),
            setzero_method(min_value, max_value),
            invertsign_method(min_value, max_value),
        ])

    # Handle different value types
    if isinstance(value, (int, float)):
        min_value, max_value = value_pool
        return apply_mutation(value, min_value, max_value)
    elif isinstance(value, list) and all(isinstance(i, (int, float)) for i in value):
        min_value, max_value = value_pool
        return [apply_mutation(i, min_value, max_value) for i in value]
    elif isinstance(value, str):
        if not value_pool:
            raise ValueError(f"No valid choices in value pool for string parameter '{key_path}'")
        return random.choice(value_pool)
    else:
        raise ValueError(f"Unsupported value type '{type(value)}' for mutation in parameter '{key_path}'")


def main(args):
    
    # Reading the initial JSON data
    json_data = json_parser.read_json_from_local(args.parent_path)

    # Prepare a list to hold log messages, starting with the original file name
    modification_messages = [f"Parent file: {args.parent_path}"]

    # Fetch all parameters
    fetched_parameters = json_parser.fetch_all_parameters(json_data)
        
    print(f"Running {args.iter} iterations")
    # Mutating logic for each iter:
    for iteration in range(args.iter):
        print(f"Iteration {iteration + 1}")

        # Reload actually kinda reset the original JSON data before each mutation
        json_data = json_parser.read_json_from_local(args.parent_path)

        # Prepare a list to hold log messages, starting with the original file name
        modification_messages = [f"Parent file: {args.parent_path}, Iteration: {args.iter + 1}"]

        # A custom randomizer for our parameters, generated here to have a different num in each iter, 
        # CAREFUL! for A its (1,40) for B its (1,25)
        random_param_number = random.randrange(1,25)
        
        # Apply mutations only to the selected parameters
        for param_key in (random.sample(parameters_to_mutate_B, random_param_number)):
            if param_key in value_pools_firstgen:
                try:
                    old_value, new_value = mutate_parameters(json_data, param_key, value_pools_firstgen[param_key])
                    modification_messages.append(f"Mutated {param_key} from '{old_value}' to '{new_value}'")
                except ValueError as e:
                    print(f"Error: {e}")
                except KeyError as e:
                    print(f"KeyError: {e}")

        # Save the updated data back to a file with a unique name
        unique_file_name, current_index = json_parser.save_json_to_local(json_data, args.mutated_path, args.iter + 1)
        print(f"Updated data saved to: {unique_file_name}")

        # Log all modifications to a file in the specified directory
        log_file_path = json_parser.log_modification(args.log_file_directory, modification_messages, current_index)
        print(f"Modifications logged to: {log_file_path}")

        # Update the index
        json_parser.update_index(args.mutated_path, current_index + 1)


if __name__ == "__main__":
    args = parse_args()
    main(args)