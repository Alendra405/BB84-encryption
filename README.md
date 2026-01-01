# BB84 Quantum Key Distribution Simulation with Qiskit

A simple and educational implementation of the **BB84** quantum key distribution (QKD) protocol using **Qiskit**. This project simulates the famous Bennett-Brassard 1984 protocol, demonstrating how Alice and Bob can generate a shared secret key that's secure against eavesdropping—even from quantum computers.

## 🌟 Features
- Full simulation of BB84 protocol on Qiskit's Aer simulator.
- Random bit and basis generation for Alice and Bob.
- Optional eavesdropping (Eve) mode to demonstrate error introduction.
- Automatic eavesdropping detection via error rate checking (threshold ~10%).
- Generates a final shared secret key when the channel is secure.
- Easy to modify: change qubit count, add visualization, or extend with error correction.

## 🔬 How It Works (Quick Overview)
1. Alice prepares qubits based on random bits and bases (Z or X).
2. Bob measures in random bases.
3. They publicly compare bases and keep matching ones.
4. Sample bits are checked for errors → if error rate is high, eavesdropping detected!
5. Remaining bits become the shared secret key.

Security comes from quantum mechanics: any eavesdropping introduces detectable errors (≈25% error rate).

## 🚀 Install libraries
```bash
pip install qiskit qiskit-aer numpy
pip install qiskit
pip install numpy
```
## 🚦 Output 
```bash
=== Without eave :> YES! ===
Errors: 0.00%
Channel is secure!
Final key: [np.int32(0), np.int32(1), np.int32(1), np.int32(0), np.int32(1), np.int32(1), np.int32(1), np.int32(0), np.int32(1), np.int32(1), np.int32(1), np.int32(0), np.int32(0), np.int32(1), np.int32(0)]     

=== With eave (*_*)HA? ===
Errors: 33.33%
Eave was found!!!!!!.
Final key: None
```
## ¯\_(ツ)_/¯ install with debian/ubuntu
