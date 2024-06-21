# This file describes Grover's Algorithm in OpenQL's intermediate representation (IR).
# The IR provides a low-level description of quantum operations to be executed on a quantum computer.

pragma @ql.name("grover")

.grover
    h q[0]         # Apply a Hadamard gate to qubit q[0], putting it into a superposition state. This ensures that all possible states are explored.
    h q[1]         # Apply a Hadamard gate to qubit q[1], putting it into a superposition state.
    h q[2]         # Apply a Hadamard gate to qubit q[2], putting it into a superposition state.
    x q[0]         # Apply an X gate to qubit q[0], flipping its state from |0⟩ to |1⟩ or vice versa. This sets up the oracle.
    x q[1]         # Apply an X gate to qubit q[1], flipping its state. This sets up the oracle.
    x q[2]         # Apply an X gate to qubit q[2], flipping its state. This sets up the oracle.
    h q[2]         # Apply a Hadamard gate to qubit q[2], preparing it for the controlled operation in the oracle.
    cnot q[1], q[2] # Apply a CNOT gate with qubit q[1] as control and qubit q[2] as target. This is part of the oracle function.
    h q[2]         # Apply a Hadamard gate to qubit q[2] to complete the oracle operation.
    x q[0]         # Apply an X gate to qubit q[0] to revert the state back to its original form.
    x q[1]         # Apply an X gate to qubit q[1] to revert the state back to its original form.
    x q[2]         # Apply an X gate to qubit q[2] to revert the state back to its original form.
    h q[0]         # Apply a Hadamard gate to qubit q[0], part of the diffusion operator to invert about the mean.
    h q[1]         # Apply a Hadamard gate to qubit q[1], part of the diffusion operator to invert about the mean.
    h q[2]         # Apply a Hadamard gate to qubit q[2], part of the diffusion operator to invert about the mean.
    x q[0]         # Apply an X gate to qubit q[0], part of the inversion about the mean.
    x q[1]         # Apply an X gate to qubit q[1], part of the inversion about the mean.
    x q[2]         # Apply an X gate to qubit q[2], part of the inversion about the mean.
    h q[2]         # Apply a Hadamard gate to qubit q[2], preparing for the multi-controlled-Z operation.
    cnot q[1], q[2] # Apply a CNOT gate with qubit q[1] as control and qubit q[2] as target. This is part of the multi-controlled-Z operation.
    h q[2]         # Apply a Hadamard gate to qubit q[2] to complete the multi-controlled-Z operation.
    x q[0]         # Apply an X gate to qubit q[0] to revert the state back.
    x q[1]         # Apply an X gate to qubit q[1] to revert the state back.
    x q[2]         # Apply an X gate to qubit q[2] to revert the state back.
    h q[0]         # Apply a Hadamard gate to qubit q[0], final step of the diffusion operator.
    h q[1]         # Apply a Hadamard gate to qubit q[1], final step of the diffusion operator.
    h q[2]         # Apply a Hadamard gate to qubit q[2], final step of the diffusion operator.
    measure q[0]   # Measure qubit q[0] to collapse the state and get the result.
    measure q[1]   # Measure qubit q[1] to collapse the state and get the result.
    measure q[2]   # Measure qubit q[2] to collapse the state and get the result.
