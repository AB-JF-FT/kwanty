# This file describes a quantum lotto number selection process in OpenQL's intermediate representation (IR).
# The IR provides a low-level description of quantum operations to be executed on a quantum computer.

pragma @ql.name("quantum_lotto")

.lotto
    { # start at cycle 0
        prep_z q[0]       # Initialize qubit q[0] to the |0⟩ state.
        prep_z q[1]       # Initialize qubit q[1] to the |0⟩ state.
        prep_z q[2]       # Initialize qubit q[2] to the |0⟩ state.
        prep_z q[3]       # Initialize qubit q[3] to the |0⟩ state.
        prep_z q[4]       # Initialize qubit q[4] to the |0⟩ state.
        prep_z q[5]       # Initialize qubit q[5] to the |0⟩ state.
    }
    skip 1               # Skip 1 cycle to ensure qubits are properly initialized.
    { # start at cycle 2
        h q[0]            # Apply a Hadamard gate to qubit q[0], putting it into a superposition state.
        h q[1]            # Apply a Hadamard gate to qubit q[1], putting it into a superposition state.
        h q[2]            # Apply a Hadamard gate to qubit q[2], putting it into a superposition state.
        h q[3]            # Apply a Hadamard gate to qubit q[3], putting it into a superposition state.
        h q[4]            # Apply a Hadamard gate to qubit q[4], putting it into a superposition state.
        h q[5]            # Apply a Hadamard gate to qubit q[5], putting it into a superposition state.
    }
    skip 1               # Skip 1 cycle to allow the superposition state to stabilize.
    { # start at cycle 4
        measure q[0]      # Measure qubit q[0]. The measurement collapses its state to a classical bit.
        measure q[1]      # Measure qubit q[1]. The measurement collapses its state to a classical bit.
        measure q[2]      # Measure qubit q[2]. The measurement collapses its state to a classical bit.
        measure q[3]      # Measure qubit q[3]. The measurement collapses its state to a classical bit.
        measure q[4]      # Measure qubit q[4]. The measurement collapses its state to a classical bit.
        measure q[5]      # Measure qubit q[5]. The measurement collapses its state to a classical bit.
    }
    skip 14              # Skip 14 cycles to account for measurement operations and readout times.
