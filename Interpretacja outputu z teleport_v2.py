# This file describes a double quantum teleportation process in OpenQL's intermediate representation (IR).
# The IR provides a low-level description of quantum operations to be executed on a quantum computer.

pragma @ql.name("double_quantum_teleportation")

.double_teleportation_kernel
    prep_z q[0]         # Initialize qubit q[0] to the |0⟩ state.
    prep_z q[1]         # Initialize qubit q[1] to the |0⟩ state.
    prep_z q[2]         # Initialize qubit q[2] to the |0⟩ state.
    prep_z q[3]         # Initialize qubit q[3] to the |0⟩ state.
    prep_z q[4]         # Initialize qubit q[4] to the |0⟩ state.
    prep_z q[5]         # Initialize qubit q[5] to the |0⟩ state.

    h q[2]              # Apply a Hadamard gate to qubit q[2], putting it into a superposition state.
    cz q[2], q[4]       # Apply a controlled-Z gate between qubits q[2] (control) and q[4] (target), entangling them.
    
    h q[3]              # Apply a Hadamard gate to qubit q[3], putting it into a superposition state.
    cz q[3], q[5]       # Apply a controlled-Z gate between qubits q[3] (control) and q[5] (target), entangling them.
    
    cnot q[0], q[2]     # Apply a CNOT gate with qubit q[0] as control and qubit q[2] as target, entangling qubit q[0] with qubit q[2].
    h q[0]              # Apply a Hadamard gate to qubit q[0], preparing it for measurement.
    measure q[0]        # Measure qubit q[0]. The measurement collapses its state to a classical bit.
    measure q[2]        # Measure qubit q[2]. The measurement collapses its state to a classical bit.
    cnot q[2], q[4]     # Apply a CNOT gate with qubit q[2] as control and qubit q[4] as target. This corrects the state of qubit q[4] based on the measurement of qubit q[2].
    cz q[0], q[4]       # Apply a controlled-Z gate between qubits q[0] (control) and q[4] (target). This corrects the state of qubit q[4] based on the measurement of qubit q[0].

    cnot q[1], q[3]     # Apply a CNOT gate with qubit q[1] as control and qubit q[3] as target, entangling qubit q[1] with qubit q[3].
    h q[1]              # Apply a Hadamard gate to qubit q[1], preparing it for measurement.
    measure q[1]        # Measure qubit q[1]. The measurement collapses its state to a classical bit.
    measure q[3]        # Measure qubit q[3]. The measurement collapses its state to a classical bit.
    cnot q[3], q[5]     # Apply a CNOT gate with qubit q[3] as control and qubit q[5] as target. This corrects the state of qubit q[5] based on the measurement of qubit q[3].
    cz q[1], q[5]       # Apply a controlled-Z gate between qubits q[1] (control) and qubit q[5] (target). This corrects the state of qubit q[5] based on the measurement of qubit q[1].
