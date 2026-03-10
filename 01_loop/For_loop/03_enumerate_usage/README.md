# 03 — Enumerate Usage

## Overview
`enumerate()` is a built-in Python function that allows us to loop through an iterable while also keeping track of the index of each element.

Normally, when we iterate over a list using a `for` loop, we only get the value. However, in many situations we also need the position (index) of that value. `enumerate()` solves this problem by returning both the index and the value at the same time.

### Indonesian Translation
`enumerate()` adalah fungsi bawaan Python yang memungkinkan kita melakukan iterasi pada sebuah iterable sambil tetap mengetahui indeks dari setiap elemennya.

Biasanya ketika kita melakukan loop pada sebuah list menggunakan `for`, kita hanya mendapatkan nilainya saja. Namun dalam banyak kasus kita juga membutuhkan posisi (index) dari nilai tersebut. `enumerate()` menyelesaikan masalah ini dengan mengembalikan index dan value sekaligus.

---

# Why Use enumerate()

Using `enumerate()` makes code cleaner and more readable compared to manually managing indexes with `range(len(...))`.

Example without `enumerate()`:

```python
fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])
```
```output
0 apple
1 banana
3 manggo
```

Example with `enumerate()`:

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```
```output
0 apple
1 banana
3 manggo
```

### Indonesian Translation

Menggunakan `enumerate()` membuat kode lebih bersih dan lebih mudah dibaca dibandingkan mengelola indeks secara manual menggunakan `range(len(...))`.

Contoh tanpa `enumerate()`:

```python
fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])
```
```output
0 apple
1 banana
3 manggo
```

Contoh dengan `enumerate()`:

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```
```output
0 apple
1 banana
3 manggo
```
---

# Starting Index

By default, `enumerate()` starts counting from `0`.  
However, we can change the starting number using the `start` parameter.

Example:

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

Output:

```
1 apple
2 banana
3 mango
```

### Indonesian Translation

Secara default, `enumerate()` memulai perhitungan dari `0`.  
Namun kita dapat mengubah angka awal menggunakan parameter `start`.

Contoh:

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

---

# Real-World Example (Blockchain Concept)

In blockchain systems, blocks often contain a list of transactions.  
We may want to display transactions with their order number.

Example:

```python
transactions = [
    "0xa1f4",
    "0xb9c2",
    "0xf331"
]

for index, tx in enumerate(transactions, start=1):
    print("Transaction", index, ":", tx)
```

Output:

```
Transaction 1 : 0xa1f4
Transaction 2 : 0xb9c2
Transaction 3 : 0xf331
```

### Indonesian Translation

Dalam sistem blockchain, sebuah block biasanya berisi daftar transaksi.  
Kita sering ingin menampilkan transaksi beserta nomor urutnya.

Contoh:

```python
transactions = [
    "0xa1f4",
    "0xb9c2",
    "0xf331"
]

for index, tx in enumerate(transactions, start=1):
    print("Transaction", index, ":", tx)
```

---

# Files in This Module

```
01_basic_enumerate.py
02_enumerate_start.py
03_practice_enumerate.py
04_exercise_enumerate.py
```

### Indonesian Translation

Penjelasan file pada modul ini:

- **01_basic_enumerate.py**  
  Dasar penggunaan `enumerate()`.

- **02_enumerate_start.py**  
  Menggunakan parameter `start` untuk mengubah index awal.

- **03_practice_enumerate.py**  
  Latihan penggunaan `enumerate()` pada contoh sederhana.

- **04_exercise_enumerate.py**  
  Soal latihan untuk menguji pemahaman konsep `enumerate()`.

---

# Learning Goal

After completing this module, you should understand:

- How `enumerate()` works
- The difference between iterating values and iterating with index
- When `enumerate()` is more readable than `range(len())`

### Indonesian Translation

Setelah menyelesaikan modul ini, kamu diharapkan memahami:

- Cara kerja `enumerate()`
- Perbedaan iterasi nilai saja vs iterasi dengan indeks
- Kapan `enumerate()` lebih baik digunakan dibanding `range(len())`
