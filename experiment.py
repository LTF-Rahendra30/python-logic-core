import hashlib
import json

data_dict = {
    "nama": "Budi",
    "usia": 25,
    "aktif": True
}
# 1. Ubah dictionary menjadi string JSON dan encode menjadi bytes
dict_string = json.dumps(data_dict, sort_keys=True)

# 2. Buat objek hash SHA-256
hash_obj = hashlib.sha256(dict_string.encode('utf-8'))

# 3. Dapatkan hasil hash (format heksadesimal)
hasil_hash = hash_obj.hexdigest()

print("Hash SHA-256:", hasil_hash)




transaction =[  # ← LEVEL 3: Transaction list
        {
            "tx_id": 1,
            "type": "in",      # "in" atau "out"
            "amount": 0.3,
            "date": "2026-05-20",
            "description": "Received from exchange"
        },
        {
            "tx_id": 2,
            "type": "out",
            "amount": 0.1,
            "date": "2026-05-21",
            "description": "Sent to cold storage"
        }
    ]
total = 0.0
for trx in transaction:
    total += trx["amount"]
print(total)
