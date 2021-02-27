import hello
import module1
import os
import csv

hello.print_hello()

file_path = os.path.join("Users", "bob", "st.txt")
print(file_path)

my_list = []

with open("st.txt", "w", encoding="utf-8") as f:
    f.write("Hi From python（パイソン）")

with open("st.txt", "r", encoding="utf-8") as f:
    my_list.append(f.read())

print(my_list)

with open("st.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["1", "ni", "three"])
    w.writerow(["4", "go", "six"])

with open("st.csv", "r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print("=".join(row))
