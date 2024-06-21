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

# Number of qubits for the Grover's Algorithm (3 qubits for simplicity)
n = 3

# Create a quantum program named 'grover' for the defined platform
program = ql.Program('grover', platform, n)

# Create a quantum kernel named 'grover'
grover_kernel = ql.Kernel('grover', platform, n)

# Apply Hadamard gates to all qubits to create superposition
# This puts each qubit in a superposition of |0> and |1>, effectively exploring all possible states simultaneously.
for i in range(n):
    grover_kernel.gate('h', [i])

# Apply the Oracle (assuming the marked item is |111>)
# The Oracle flips the amplitude of the target state. In this case, the target state is |111>.
grover_kernel.gate('x', [0])  # Apply X gate to qubit 0 to prepare it for the Oracle
grover_kernel.gate('x', [1])  # Apply X gate to qubit 1 to prepare it for the Oracle
grover_kernel.gate('x', [2])  # Apply X gate to qubit 2 to prepare it for the Oracle
grover_kernel.gate('h', [2])  # Apply Hadamard gate to qubit 2 to enable the controlled operation
grover_kernel.gate('cnot', [1, 2])  # Apply CNOT gate to flip the state of qubit 2 if qubit 1 is |1>
grover_kernel.gate('h', [2])  # Apply Hadamard gate to qubit 2 to complete the Oracle operation
grover_kernel.gate('x', [0])  # Apply X gate to qubit 0 to revert the state back
grover_kernel.gate('x', [1])  # Apply X gate to qubit 1 to revert the state back
grover_kernel.gate('x', [2])  # Apply X gate to qubit 2 to revert the state back

# Apply Hadamard gates to all qubits again
# This is part of the Grover diffusion operator which inverts about the mean amplitude.
for i in range(n):
    grover_kernel.gate('h', [i])

# Apply X gates to all qubits to invert about the mean
# These X gates are part of the inversion process.
for i in range(n):
    grover_kernel.gate('x', [i])

# Apply a multi-controlled-Z gate (in this case, H-CNOT-H sequence)
# This flips the phase of the |000> state, which is necessary for the Grover diffusion operator.
grover_kernel.gate('h', [n-1])  # Apply Hadamard gate to the last qubit to prepare it for controlled operation
grover_kernel.gate('cnot', [n-2, n-1])  # Apply CNOT gate with the second-to-last qubit as control
grover_kernel.gate('h', [n-1])  # Apply Hadamard gate to the last qubit to complete the phase flip

# Apply X gates to all qubits again
# Reverting the X gates applied before the multi-controlled-Z gate.
for i in range(n):
    grover_kernel.gate('x', [i])

# Apply Hadamard gates to all qubits again
# This completes the Grover diffusion operator.
for i in range(n):
    grover_kernel.gate('h', [i])

# Measure all qubits to get the result
# This collapses the superposition to one of the states, revealing the target state with high probability.
for i in range(n):
    grover_kernel.gate('measure', [i])

# Add the kernel to the program
program.add_kernel(grover_kernel)

# Compile the program
program.compile()

print("Grover's Algorithm program compiled successfully.")
