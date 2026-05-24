# A Simple Crypto Wallet Tracker

My first project that I dedicated myself to was learn the fundalemtals logic of programming in the AI Era and Building a long-term mindset of a developer.


## 📋 Project Description

Simple cryptocurrency wallet tracker for manage multiple wallets users with transaction history tracking.

**Why this project?**
- 🧠 Mastering nested data structures (user → wallet → transaction)
- 🔗 Learn complex data relationships
- 💾 Practice real-world data modeling
- 🎯 Foundation for backend & Web3 development


## 🎯 Features
### User Management
- ✅ Register user dengan email & password validation
- ✅ Get user by username
- ✅ View all registered users
- ✅ User data persistence (in-memory)

### Wallet Management
- ✅ Add wallet to specific user
- ✅ Get all wallets owned by user
- ✅ Get specific wallet by ID
- ✅ View wallet details (address, balance, coin type)
- ✅ Calculate total balance across all wallets

### Transaction Management
- ✅ Add transaction (in/out) to specific wallet
- ✅ View transaction history per wallet
- ✅ Calculate wallet balance from transaction history
- ✅ Filter transactions by type (in/out)
- ✅ Filter transactions by date range




## 🧠 Core Concepts

## 📂 Folder structure
```text
wallet-crypto-tracker/
├── README.md                    # Documentation (this is file)
├── main.py                      # Entry point / playground
│
├── validators/                  # Pure validation functions
│   ├── init.py
│   ├── user_validators.py       # User validation (email, password, username)
│   └── wallet_validators.py     # Wallet validation (address, coin type)
│
├── managers/                    # Business logic & data management
│   ├── init.py
│   ├── user_manager.py          # User CRUD operations
│   └── wallet_manager.py        # Wallet & transaction operations
│
└── display/                     # Display & formatting functions
├── init.py
├── user_display.py          # Format & display user data
└── wallet_display.py        # Format & display wallet & transaction data
```

## 🚀 How to Run
```bash
cd 02_wallet_crypto_system
python main.py
```
