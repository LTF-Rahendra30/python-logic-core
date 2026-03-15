# 04 — Nested Loop

## Overview


A **nested loop** is a loop inside another loop.

Hello Everyone! Today I will start learn nested loop in python, my goal is to strengthen my programming logic

This means that for every iteration of the outer loop, the inner loop will run completely.
Nested loops are commonly used when working with grids, tables, matrices, or structured data.

### Indonesian Translation


**Nested loop** adalah loop yang berada di dalam loop lainnya.
Artinya setiap kali loop luar berjalan satu kali, loop di dalamnya akan dijalankan sepenuhnya.

Nested loop sering digunakan ketika bekerja dengan grid, tabel, matriks, atau data yang memiliki struktur bertingkat.


---


# Basic Example


Example:


```python
for i in range(3):
    for j in range(2):
        print(i, j)
```


Output:


```
0 0
0 1
1 0
1 1
2 0
2 1
```


Explanation:


The outer loop runs **3 times**, and the inner loop runs **2 times** for each iteration.

Total iterations:


```
3 × 2 = 6
```


### Indonesian Translation


Penjelasan:

Loop luar berjalan **3 kali**, dan loop dalam berjalan **2 kali** pada setiap iterasi.


Total iterasi:


```
3 × 2 = 6
```


---


# Example — Creating a Grid


Nested loops are often used to create a grid or table.


Example:


```python
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()
```


Output:


```
* * *
* * *
* * *
```


### Indonesian Translation


Nested loop sering digunakan untuk membuat grid atau tabel.


Contoh di atas mencetak pola bintang berbentuk kotak.


---


# Example — Multiplication Table


Example:


```python
for i in range(1,4):
    for j in range(1,4):
        print(i * j, end=" ")
    print()
```


Output:


```
1 2 3
2 4 6
3 6 9
```


### Indonesian Translation


Nested loop juga dapat digunakan untuk membuat tabel perkalian.


Loop luar mewakili baris, dan loop dalam mewakili kolom.


---


# Example — Simple Blockchain Structure

Example:

```python
blockchain = [
    ["tx1", "tx2"],
    ["tx3", "tx4"]
]


for block in blockchain:
    for tx in block:
        print(tx)
```


Output:


```
tx1
tx2
tx3
tx4
```


### Indonesian Translation


Dalam sistem blockchain, satu block biasanya berisi beberapa transaksi.


Nested loop dapat digunakan untuk membaca setiap transaksi di dalam setiap block.


---


# Files in This Module


```
01_basic_nested_loop.py
02_matrix_loop.py
03_practice_nested_loop.py
04_exercise_nested_loop.py
```


### Indonesian Translation


Penjelasan file pada modul ini:


- **01_basic_nested_loop.py**  
  Dasar penggunaan nested loop.


- **02_matrix_loop.py**  
  Contoh nested loop untuk membuat grid atau matriks.


- **03_practice_nested_loop.py**  
  Latihan penggunaan nested loop.


- **04_exercise_nested_loop.py**  
  Soal latihan untuk menguji pemahaman nested loop.


---


# Learning Goals

After completing this module, you should understand:


- How nested loops work
- How outer loops and inner loops interact
- How nested loops are used in real-world problems


### Indonesian Translation

Setelah menyelesaikan modul ini, kamu diharapkan memahami:


- Cara kerja nested loop
- Hubungan antara loop luar dan loop dalam
- Cara nested loop digunakan dalam masalah nyata