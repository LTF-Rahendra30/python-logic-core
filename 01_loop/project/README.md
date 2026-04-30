# A Project Loop-Based System Simulation

## 📌 Overview

This folder contains simulation-based projects built using fundamental loop concepts (`while` and `for`).
Instead of focusing only on syntax, these projects simulate real-world system behavior such as financial transactions and mining processes.
The goal is to transform basic loop understanding into structured problem-solving and system thinking.

## 🎯 Purpose

- Strengthen programming logic using real-world inspired cases
- Build a developer mindset (control flow, validation, and state management)
- Practice handling unpredictable user input
- Prepare a strong foundation before learning advanced topics like Web3 & Blockchain

## 🧠 Concepts Applied

- `while loop` (infinite loop & condition-based loop)
- `for loop` (iteration & counting)
- control flow (`break`, `continue`)
- input validation (`try-except`)
- state management (balance, attempts, system state)
- decision making (`if-elif-else`)
- basic simulation logic

## 📂 File Structure

```text
project/
    ├── simple_crypto_wallet_simulation.py
    ├── mining_simulation.py
    └── README.md
```

## 📖 Description The Project File

## 🎮 Project 1 — Crypto Wallet Simulation

```text
    simple_crypto_wallet_simulation.py
```

A simple command-line wallet system that simulates basic web3 wallet behavior
The user can check wallet information, send transactions, and receive funds.
This project focuses on how wallet-based systems manage balance and transaction flow.

## 🔑 Rules

User can:

- Check wallet info
- Send transaction
- Receive funds
- Exit

Sending transaction must pass validations:

- amount must be a number
- amount must be greather than 0
- amount must not exeed balance

## 💡 Concepts Practiced

- `while True` for persistent system loop
- layered validation (`try-except + logical checks`)
- state management (`balance, wallet state`)
- control flow (`break, continue`)
- decision branching (`if-elif-else`)
- basic transaction flow simulation

## 🎮 Project 2 — Mining Simulation

```text
    mining_simulation.py
```

A simple simulation of the mining process inspired by Proof-of-Work in blockchain systems.
The program continuously searches for a valid number (nonce) that satisfies a given condition.

## 🔑 Rules

- The system starts from an initial number (e.g., 0)
- The number increases continuously in a loop
- The loop stops when a condition is met
  (e.g., number divisible by 7 or matches a specific pattern)
- The final number is considered a valid "mined" result

## 💡 Concepts Practiced

- `while` loop for brute-force computation
- condition-based loop termination
- incremental state (`nonce`)
- understanding computational effort (trial and error)
- simulation of Proof-of-Work concept

## 🚀 How to Run

1. Make sure Python is installed
2. Open terminal in this folder
3. Run one of the project files:

```bash
python simple_crypto_wallet_simulation.py

```
