import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def bb84_protocol(n_qubits=32, eavesdrop=False):
    alice_bits = np.random.randint(2, size=n_qubits)
    alice_bases = np.random.randint(2, size=n_qubits)
    bob_bases = np.random.randint(2, size=n_qubits)
    qc = QuantumCircuit(n_qubits, n_qubits)
    for i in range(n_qubits):
        if alice_bits[i] == 1:
            qc.x(i)  # بیت ۱
        if alice_bases[i] == 1:
            qc.h(i)  # پایه X

    if eavesdrop:
        qc.barrier()
        eve_bases = np.random.randint(2, size=n_qubits)
        for i in range(n_qubits):
            if eve_bases[i] == 1:
                qc.h(i)
        qc.measure(range(n_qubits), range(n_qubits)) 
        qc.barrier()

    for i in range(n_qubits):
        if bob_bases[i] == 1:
            qc.h(i)
    qc.measure(range(n_qubits), range(n_qubits))

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()
    bob_bits_str = list(counts.keys())[0][::-1]
    bob_bits = [int(b) for b in bob_bits_str]

    shared_key_alice = []
    shared_key_bob = []
    for i in range(n_qubits):
        if alice_bases[i] == bob_bases[i]:
            shared_key_alice.append(alice_bits[i])
            shared_key_bob.append(bob_bits[i])

    if len(shared_key_alice) < 4:
        print("Not enough bits.")
        return shared_key_alice

    test_size = len(shared_key_alice) // 4
    test_indices = np.random.choice(len(shared_key_alice), size=test_size, replace=False)
    error_rate = sum(shared_key_alice[j] != shared_key_bob[j] for j in test_indices) / test_size

    print(f"Errors: {error_rate:.2%}")

    if error_rate > 0.10:  
        print("Eave was found!!!!!!.")
        return None
    else:
        print("Channel is secure!")

        final_key = [shared_key_alice[j] for j in range(len(shared_key_alice)) if j not in test_indices]
        return final_key

print("=== Without eave :> YES! ===")
key_safe = bb84_protocol(32, eavesdrop=False) #Run protocol without eave
print("Final key:", key_safe)

print("\n=== With eave (*_*)HA? ===")
key_eve = bb84_protocol(32, eavesdrop=True) #Run protocol with eave

print("Final key:", key_eve)
