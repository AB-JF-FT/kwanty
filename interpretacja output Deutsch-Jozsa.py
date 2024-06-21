# This file describes the Deutsch-Jozsa Algorithm in OpenQL's intermediate representation (IR).
# The IR provides a low-level description of quantum operations to be executed on a quantum computer.

pragma @ql.name("deutsch_jozsa")

.deutsch_jozsa
    x q[2]         # Initialize the ancilla qubit q[2] to the |1⟩ state. This is crucial for the oracle function.
    h q[0]         # Apply a Hadamard gate to qubit q[0], putting it into a superposition state. This explores all possible inputs simultaneously.
    h q[1]         # Apply a Hadamard gate to qubit q[1], putting it into a superposition state.
    h q[2]         # Apply a Hadamard gate to the ancilla qubit q[2], putting it into a superposition state necessary for the oracle.
    cnot q[0], q[2] # Apply a CNOT gate with qubit q[0] as control and ancilla qubit q[2] as target. This is part of the oracle function for f(x) = x1 ⊕ x2.
    cnot q[1], q[2] # Apply a CNOT gate with qubit q[1] as control and ancilla qubit q[2] as target. This completes the oracle function.
    h q[0]         # Apply a Hadamard gate to qubit q[0] to interfere the states. This will help determine if the function is constant or balanced.
    h q[1]         # Apply a Hadamard gate to qubit q[1] to interfere the states.
    measure q[0]   # Measure qubit q[0] to collapse the state and get the result.
    measure q[1]   # Measure qubit q[1] to collapse the state and get the result.
