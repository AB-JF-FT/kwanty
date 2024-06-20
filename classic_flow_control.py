import openql as ql

# Initialize the OpenQL framework
ql.initialize()

# Set the directory for output files where compiled results will be stored
ql.set_option('output_dir', 'output')

# Set the logging level to display informational messages during the execution
ql.set_option('log_level', 'LOG_INFO')

# Define a quantum computing platform with a name ('my_platform') and specify no configuration file
# The configuration file typically includes details about the quantum hardware, but 'none' is used here
platform = ql.Platform('my_platform', 'none')

# Define the number of qubits and classical registers needed
# num_qubits: The total number of quantum bits used in the program
# num_cregs: The total number of classical registers for storing measurement results and performing classical operations
num_qubits = 5
num_cregs = 10

# Create a quantum program named 'test_classical' for the defined platform
# The program will consist of multiple kernels (quantum operations) executed on the platform
program = ql.Program('test_classical', platform, num_qubits, num_cregs)

# Create the first quantum kernel named 'First'
# A kernel represents a sequence of quantum operations executed together
kfirst = ql.Kernel('First', platform, num_qubits, num_cregs)

# Create classical registers with identifiers
# Classical registers are used to store measurement outcomes and to perform classical operations
rs1 = ql.CReg(0)
rs2 = ql.CReg(1)

# Add the first kernel to the program
# This kernel currently doesn't perform any operations
program.add_kernel(kfirst)

# Create kernels for the then-part and else-part of the if-else construct
# The 'then' part will execute if the condition is true, and the 'else' part will execute if the condition is false
kthen = ql.Kernel('Thenpart', platform, num_qubits, num_cregs)
kthen.gate('x', [0])  # Apply an X gate (NOT gate) to qubit 0 in the then-part

kelse = ql.Kernel('Elsepart', platform, num_qubits, num_cregs)
kelse.gate('y', [0])  # Apply a Y gate to qubit 0 in the else-part

# Add the if-else construct to the program
# This construct compares the values in classical registers rs1 and rs2
# If rs1 equals rs2, the 'then' kernel (kthen) is executed, otherwise the 'else' kernel (kelse) is executed
program.add_if_else(kthen, kelse, ql.Operation(rs1, '==', rs2))

# Create a kernel for the body of the for loop
# The loop body contains the operations that will be repeated
kloopbody = ql.Kernel('Loopbody', platform, num_qubits, num_cregs)
kloopbody.gate('x', [0])  # Apply an X gate to qubit 0 in the loop body

# Add a for loop to the program that repeats 10 times over the loop body kernel
# This means the operations in kloopbody will be executed 10 times in a row
program.add_for(kloopbody, 10)

# Create a kernel for the operations that occur after the for loop
# These operations will be executed once the loop has completed all its iterations
kafterloop = ql.Kernel('Afterloop', platform, num_qubits, num_cregs)
kafterloop.gate('y', [0])  # Apply a Y gate to qubit 0 after the loop
program.add_kernel(kafterloop)

# Create a kernel for the body of the do-while loop
# The loop body contains operations that will be repeated as long as the loop condition is met
kdowhileloopbody = ql.Kernel('Dowhileloopbody', platform, num_qubits, num_cregs)
kdowhileloopbody.gate('x', [0])  # Apply an X gate to qubit 0 in the loop body

# Add the do-while loop to the program
# This construct executes the loop body (kdowhileloopbody) at least once and then continues to execute it
# as long as the value in classical register rs1 is less than the value in classical register rs2
program.add_do_while(kdowhileloopbody, ql.Operation(rs1, '<', rs2))

# Create a kernel for the operations that occur after the do-while loop
# These operations will be executed once the do-while loop has completed
kafterdowhile = ql.Kernel('Afterdowhile', platform, num_qubits, num_cregs)
kafterdowhile.gate('y', [0])  # Apply a Y gate to qubit 0 after the do-while loop
program.add_kernel(kafterdowhile)

# Compile the quantum program
# Compilation translates the high-level program description into instructions that can be executed on the quantum hardware
program.compile()

# Print a message indicating that the quantum program has been successfully compiled
print("Compiled quantum program with classical control flow.")
