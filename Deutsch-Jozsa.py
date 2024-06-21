import openql as ql
import os

# Initialize the OpenQL framework
ql.initialize()

# Set the directory for output files
output_dir = 'output'
ql.set_option('output_dir', output_dir)
# Set the logging level to display warnings
ql.set_option('log_level', 'LOG_WARNING')

# Define the quantum platform with a name and specify no configuration file
platform = ql.Platform('my_platform', 'none')

# Number of qubits for the Deutsch-Jozsa Algorithm (2 input qubits + 1 ancilla qubit)
n = 3

# Create a quantum program named 'deutsch_jozsa' for the defined platform
program = ql.Program('deutsch_jozsa', platform, n)

# Create a quantum kernel named 'deutsch_jozsa'
dj_kernel = ql.Kernel('deutsch_jozsa', platform, n)

# Initialize the ancilla qubit to |1>
dj_kernel.gate('x', [n-1])  # Apply X gate to the ancilla qubit to set it to |1>

# Apply Hadamard gates to all qubits to create superposition
# This puts the input qubits in a superposition of all possible inputs and prepares the ancilla for the Oracle.
for i in range(n):
    dj_kernel.gate('h', [i])

# Apply the Oracle function
# For the Deutsch-Jozsa algorithm, the Oracle distinguishes between constant and balanced functions.
# This example assumes a balanced function f(x) = x1 ⊕ x2.
dj_kernel.gate('cnot', [0, 2])  # Apply CNOT gate with qubit 0 as control and ancilla as target
dj_kernel.gate('cnot', [1, 2])  # Apply CNOT gate with qubit 1 as control and ancilla as target

# Apply Hadamard gates to all input qubits again
# This completes the interference process that reveals whether the function is constant or balanced.
for i in range(n-1):
    dj_kernel.gate('h', [i])

# Measure all input qubits to get the result
# The measurement will reveal whether the function is constant (all 0s) or balanced (at least one 1).
for i in range(n-1):
    dj_kernel.gate('measure', [i])

# Add the kernel to the program
program.add_kernel(dj_kernel)

# Compile the program
program.compile()

print("Deutsch-Jozsa Algorithm program compiled successfully.")
