"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 1:
Write a program that reads in integer numbers from a text file named indata.txt in the same directory as the executing program.  
Print the sum of the numbers with comma separators and two digits.
For example if the file has the following data:
10
1000
20
Your program should print 1030.00.
"""

try:
    with open("indata.txt", 'r') as file:
        numbers = [float(line.strip()) for line in file]
    formatted_sum = "{:.2f}".format(sum(numbers))
    print(formatted_sum)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Invalid data format in the file.")
