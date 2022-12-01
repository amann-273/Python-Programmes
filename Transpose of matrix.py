#!/usr/bin/env python
# coding: utf-8

# In[ ]:


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

transposed = []
print("matrix:")
print(matrix)
print("transposition using nested while:")
""" Matrix Transposition using Nested while"""
i = 0
while(i < len(matrix[0])):
	j = 0
	lx = []
	while(j < len(matrix)):
		lx.append(matrix[j][i])
		j = j + 1
	transposed.append(lx)
	i = i + 1
print(transposed)
print("transposition using nested for:")
""" Matrix Transposition using Nested Fors"""
transposed = []         # Transposed Matrix
for i in range(len(matrix[0])):
	transposed_row = []
	for row in matrix:  # Build each row
		transposed_row.append(row[i])
	transposed.append(transposed_row) # Apend the row
print(transposed)
print("transposition single list comprehension:")
""" Matrix Transposition using single list comprehension"""
transposed = []
#list comprehension used to build the row
for i in range(len(matrix[0])):
	transposed.append([row[i]for row in matrix]) 
print(transposed)
print("transposition double list comprehension:")
""" Matrix Transposition using double list comprehension"""
#list comprehension used to build the row and column
trasposed = []
transposed = [[row[i]for row in matrix]for i in range(len(matrix[0]))]
print(transposed)


# In[ ]:




