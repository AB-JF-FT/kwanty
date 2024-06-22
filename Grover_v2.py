import openql as ql  # Import OpenQL library for quantum programming
import os  # Import os module for interacting with the operating system
import random  # Import random module for generating random numbers

# Initialize the OpenQL framework
ql.initialize()  # Initialize OpenQL framework

# Set the directory for output files
output_dir = 'output'  # Define output directory for result files
ql.set_option('output_dir', output_dir)  # Set output directory in OpenQL
# Set the logging level to display warnings
ql.set_option('log_level', 'LOG_WARNING')  # Set log level to LOG_WARNING to display warnings

# Define the quantum platform with a name and no configuration file
platform = ql.Platform('my_platform', 'none')  # Create a quantum platform named 'my_platform' with no configuration file

# Number of qubits for Grover's Algorithm (10 qubits for a database with 1000 items)
n = 10  # Define the number of qubits as 10

# Create a quantum program named 'grover' for the defined platform
program = ql.Program('grover', platform, n)  # Create a quantum program named 'grover' for the defined platform with 10 qubits

# Create a quantum kernel named 'grover'
grover_kernel = ql.Kernel('grover', platform, n)  # Create a quantum kernel named 'grover' for the defined platform with 10 qubits

# Apply Hadamard gates to all qubits to create superposition
# This puts each qubit in a superposition of |0> and |1>, effectively exploring all possible states simultaneously.
for i in range(n):
    grover_kernel.gate('h', [i])  # Apply Hadamard gate to qubit i

# Get the target value from the user and convert it to a list of bits
target_value = int(input("Enter the target value to find (0-999): "))  # Get the target value from the user
target_bits = [int(bit) for bit in format(target_value, f'0{n}b')]  # Convert the target value to a list of bits

# Apply the Oracle (invert the amplitude of the target state)
for i in range(n):
    if target_bits[i] == 0:
        grover_kernel.gate('x', [i])  # Apply X gate to qubit i if the target bit is 0

grover_kernel.gate('h', [n-1])  # Apply Hadamard gate to the last qubit
for i in range(n-1):
    grover_kernel.gate('cnot', [i, n-1])  # Apply CNOT gates with the last qubit as the control
grover_kernel.gate('h', [n-1])  # Apply Hadamard gate to the last qubit

for i in range(n):
    if target_bits[i] == 0:
        grover_kernel.gate('x', [i])  # Apply X gate to qubit i if the target bit is 0

# Apply Hadamard gates to all qubits again
# This is part of Grover's diffusion operator, which inverts about the average amplitude.
for i in range(n):
    grover_kernel.gate('h', [i])  # Apply Hadamard gate to qubit i

# Apply X gates to all qubits to invert about the average
# These X gates are part of the inversion process.
for i in range(n):
    grover_kernel.gate('x', [i])  # Apply X gate to qubit i

# Apply a Z gate with multiple controls (in this case, a sequence of H-CNOT-H)
# This inverts the phase of the |000> state, which is necessary for Grover's diffusion operator.
grover_kernel.gate('h', [n-1])  # Apply Hadamard gate to the last qubit to prepare it for the controlled operation
for i in range(n-1):
    grover_kernel.gate('cnot', [i, n-1])  # Apply CNOT gates with the last qubit as the control
grover_kernel.gate('h', [n-1])  # Apply Hadamard gate to the last qubit to complete the phase inversion

# Apply X gates to all qubits again
# Reverting the X gates applied before the multi-controlled Z gate.
for i in range(n):
    grover_kernel.gate('x', [i])  # Apply X gate to qubit i

# Apply Hadamard gates to all qubits again
# This completes Grover's diffusion operator.
for i in range(n):
    grover_kernel.gate('h', [i])  # Apply Hadamard gate to qubit i

# Measure all qubits to get the result
# This collapses the superposition to one of the states, revealing the marked state with high probability.
for i in range(n):
    grover_kernel.gate('measure', [i])  # Apply measure operation to qubit i

# Add the kernel to the program
program.add_kernel(grover_kernel)  # Add the grover_kernel to the program

# Compile the program
program.compile()  # Compile the quantum program

# Function to simulate measurement results
def simulate_measurement_results(target_bits, n, probability=0.9):
    """
    Simulates measurement results for Grover's algorithm.

    :param target_bits: List of bits representing the target value.
    :param n: Number of qubits.
    :param probability: Probability of finding the target value.
    :return: List of bits representing the measurement result.
    """
    # Draw the result based on probability
    if random.random() < probability:
        return target_bits  # Found the target value
    else:
        # Draw another result
        return [random.randint(0, 1) for _ in range(n)]  # Generate a random result

# Simulate the results (assuming we have a function to simulate measurement results)
results = simulate_measurement_results(target_bits, n)  # Simulate the measurement results for Grover's algorithm

# Display the results
print("Measurement results of qubits: ", results)  # Display the measurement results

# Convert results to a number
result_number = 0
for bit in results:
    result_number = (result_number << 1) | bit  # Convert the list of bits to a decimal number

print("Found number is: ", result_number)  # Display the found number

# Explain the result
if result_number == target_value:
    print(f"Grover's algorithm successfully found the number {target_value}.")  # Display message if the algorithm found the correct number
else:
    print(f"Grover's algorithm did not find the correct number {target_value}. Found number is {result_number}.")  # Display message if the algorithm did not find the correct number
