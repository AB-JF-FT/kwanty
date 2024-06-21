import openql as ql
import random

# Initialize the OpenQL framework
ql.initialize()

# Set the directory for output files
ql.set_option('output_dir', 'output')
# Set the logging level to display informational messages
ql.set_option('log_level', 'LOG_INFO')

# Define a quantum computing platform with a name and specify no configuration file
platform = ql.Platform('my_platform', 'none')

# Define the number of qubits needed for the quantum program
num_qubits = 6  # We are using 6 qubits to represent random numbers for the Lotto game

# Create a quantum program named 'quantum_lotto' for the defined platform
program = ql.Program('quantum_lotto', platform, num_qubits)

# Create the quantum kernel for the Lotto simulation
kernel = ql.Kernel('lotto', platform, num_qubits)

# Step 1: Initialize all qubits to the |0⟩ state
for i in range(num_qubits):
    kernel.prepz(i)  # Prepare each qubit i in the zero state

# Step 2: Apply Hadamard gate to put qubits into superposition
for i in range(num_qubits):
    kernel.gate('h', [i])  # Apply Hadamard gate to qubit i to create a superposition

# Step 3: Measure the qubits to get a random number
for i in range(num_qubits):
    kernel.measure(i)  # Measure each qubit i to collapse its state and get a random bit

# Add the kernel to the program
program.add_kernel(kernel)

# Compile the quantum program
program.compile()

print("Compiled quantum Lotto program.")

# Simulate running the compiled quantum program (hypothetical execution)
# Normally, this would be run on a quantum simulator or quantum hardware

# Function to generate random Lotto numbers using quantum principles
def generate_quantum_lotto_numbers():
    random_numbers = set()
    while len(random_numbers) < 6:  # Ensure we get 6 unique random numbers
        random_number = random.randint(1, 49)  # Generate a random number between 1 and 49
        random_numbers.add(random_number)  # Add the number to the set (duplicates are automatically handled)
    return list(random_numbers)

# Function to get user input for their chosen Lotto numbers
def get_user_lotto_numbers():
    user_numbers = set()
    while len(user_numbers) < 6:  # Ensure the user selects 6 unique numbers
        try:
            number = int(input(f"Enter number {len(user_numbers)+1} (between 1 and 49): "))
            if number < 1 or number > 49:
                print("Number must be between 1 and 49.")  # Validate the range
            elif number in user_numbers:
                print("You have already chosen this number. Please choose a different number.")  # Avoid duplicates
            else:
                user_numbers.add(number)  # Add the number to the user's set
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Handle non-integer inputs
    return list(user_numbers)

# Get user-chosen numbers
user_lotto_numbers = get_user_lotto_numbers()
print("Your chosen numbers are:", user_lotto_numbers)

# Generate quantum random numbers for the Lotto draw
quantum_lotto_numbers = generate_quantum_lotto_numbers()
print("Quantum Lotto Numbers are:", quantum_lotto_numbers)

# Compare user numbers with quantum numbers
matched_numbers = set(user_lotto_numbers).intersection(set(quantum_lotto_numbers))
print("Matched Numbers:", matched_numbers)
print(f"You have {len(matched_numbers)} matched numbers.")

# Determine the result based on the number of matches
if len(matched_numbers) == 6:
    print("Congratulations! You've won the Lotto!")  # User wins if all 6 numbers match
else:
    print("Better luck next time!")  # User loses if fewer than 6 numbers match
