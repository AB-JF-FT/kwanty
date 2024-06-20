import openql as ql
import os

# Initialize OpenQL framework
ql.initialize()

# Set the directory for output files
ql.set_option('output_dir', 'output')
# Set the logging level to display informational messages
ql.set_option('log_level', 'LOG_INFO')

# Define a quantum computing platform with a name and specify no configuration file
platform = ql.Platform('my_platform', 'none')

# Define the number of qubits required (6 qubits for teleporting 2 qubits)
nqubits = 6  

# Create a quantum program named 'double_quantum_teleportation' for the defined platform with the specified number of qubits
program = ql.Program('double_quantum_teleportation', platform, nqubits)

# Create a quantum kernel named 'double_teleportation_kernel' for the defined platform with the specified number of qubits
kernel = ql.Kernel('double_teleportation_kernel', platform, nqubits)

# Initialize all qubits to the |0⟩ state
for i in range(nqubits):
    kernel.prepz(i)

# Steps for teleporting the state of qubit 0 to qubit 4 and qubit 1 to qubit 5

# Step 1: Create entangled pairs
# Apply Hadamard gate on qubit 2 to create superposition
kernel.hadamard(2)
# Apply controlled-Z gate between qubit 2 and qubit 4 to entangle them
kernel.cz(2, 4)
# Apply Hadamard gate on qubit 3 to create superposition
kernel.hadamard(3)
# Apply controlled-Z gate between qubit 3 and qubit 5 to entangle them
kernel.cz(3, 5)

# Step 2: Teleport the state of qubit 0 to qubit 4
# Apply CNOT gate with qubit 0 as control and qubit 2 as target
kernel.cnot(0, 2)
# Apply Hadamard gate on qubit 0
kernel.hadamard(0)
# Measure qubit 0
kernel.measure(0)
# Measure qubit 2
kernel.measure(2)
# Apply CNOT gate with qubit 2 as control and qubit 4 as target
kernel.cnot(2, 4)
# Apply controlled-Z gate between qubit 0 and qubit 4
kernel.cz(0, 4)

# Step 3: Teleport the state of qubit 1 to qubit 5
# Apply CNOT gate with qubit 1 as control and qubit 3 as target
kernel.cnot(1, 3)
# Apply Hadamard gate on qubit 1
kernel.hadamard(1)
# Measure qubit 1
kernel.measure(1)
# Measure qubit 3
kernel.measure(3)
# Apply CNOT gate with qubit 3 as control and qubit 5 as target
kernel.cnot(3, 5)
# Apply controlled-Z gate between qubit 1 and qubit 5
kernel.cz(1, 5)

# Add the defined kernel to the program
program.add_kernel(kernel)

# Compile the quantum program
program.compile()

# Print a message indicating that the program has been compiled
print("Compiled double quantum teleportation program.")
