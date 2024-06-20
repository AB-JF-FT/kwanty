# This file describes a quantum teleportation process in OpenQL's intermediate representation (IR).
# The IR provides a low-level description of quantum operations to be executed on a quantum computer.

pragma @ql.name("quantum_teleportation")

.teleportation_kernel
    prep_z q[0]         # Initialize qubit q[0] to the |0⟩ state.
    prep_z q[1]         # Initialize qubit q[1] to the |0⟩ state.
    prep_z q[2]         # Initialize qubit q[2] to the |0⟩ state.
    
    h q[1]              # Apply a Hadamard gate to qubit q[1]. This puts qubit q[1] into a superposition state.
    
    cz q[1], q[2]       # Apply a controlled-Z gate between qubits q[1] (control) and q[2] (target), entangling them.
    
    cnot q[0], q[1]     # Apply a CNOT gate with qubit q[0] as control and qubit q[1] as target. This entangles qubit q[0] with q[1].
    
    h q[0]              # Apply a Hadamard gate to qubit q[0], preparing it for measurement.
    
    measure q[0]        # Measure qubit q[0]. The measurement collapses its state to a classical bit.
    measure q[1]        # Measure qubit q[1]. The measurement collapses its state to a classical bit.
    
    cnot q[1], q[2]     # Apply a CNOT gate with qubit q[1] as control and qubit q[2] as target. This corrects the state of qubit q[2] based on the measurement of qubit q[1].
    
    cz q[0], q[2]       # Apply a controlled-Z gate between qubits q[0] (control) and q[2] (target). This corrects the state of qubit q[2] based on the measurement of qubit q[0].
