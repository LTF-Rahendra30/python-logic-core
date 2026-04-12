# 05 Algorithmic Pattern

## Overview

Algorithmic patterns are common ways to solve problems using loops.

Instead of only repeating code, we use loops to process data, calculate values, and make decisions.

This module introduces fundamental patterns used in real-world programming.

### Indonesian Translation

Algorithmic pattern adalah cara umum untuk menyelesaikan masalah menggunakan loop.

Bukan hanya mengulang kode, tetapi menggunakan loop untuk memproses data, menghitung nilai, dan mengambil keputusan.

---

# Core Concepts

## 1. Accumulator

Used to collect values during iteration.

### Indonesian Translation

Digunakan untuk mengumpulkan nilai selama iterasi.

Example:

```python
numbers = [10, 20, 30]


total = 0


for n in numbers:
    total += n


print(total)
```

---

## 2. Counter

Used to count how many times something happens.

### Indonesian Translation

Digunakan untuk menghitung jumlah data atau kejadian.

```python
count = 0


for n in numbers:
    count += 1
```

---

## 3. Filtering

Select specific data based on condition.

### Indonesian Translation

Memilih data dengan kondisi tertentu

```python
for n in numbers:
    if n > 10:
        print(n)
```

---

## 4. Conditional Logic

Making decisions inside a loop.

### Indonesian Translation

Digunakan untuk membuat keputusan di dalam loop.

---

## 5. Max / Min Logic

Finding highest or lowest value manually.

### Indonesian Translation

Digunakan untuk mencari nilai terbesar atau terkecil tanpa fungsi bawaan.

```python
max_value = numbers[0]


for n in numbers:
    if n > max_value:
        max_value = n
```

---

# Files in This Module

```
01_accumulator.py
02_counter.py
03_filtering.py
04_max_min.py
05_practice.py
06_exercise.py
```

---

# Learning Goals

- Understand how to process data using loops
- Build logic using accumulator and counter
- Apply conditions inside loops
- Solve simple algorithmic problems

### Indonesian Translation

- Memahami cara memproses data dengan loop
- Menggunakan accumulator dan counter
- Menggunakan kondisi dalam loop
- Menyelesaikan masalah sederhana dengan algoritma
