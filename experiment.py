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