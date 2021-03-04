import csv
import json
import os

print('start')

#########################
# csv
#########################

# read
with open(r'input_data\data1.csv') as file:
    reader = csv.reader(file)
    dat = [row for row in reader]
    print(dat)

print('------------')

# dict read
with open(r'input_data\data2.csv') as file:
    reader = csv.DictReader(file)
    dat = [row for row in reader]
    print(dat)
    
print('------------')

# write
with open(r'input_data\output_data1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['spam', 'egg', 'bacon', 'ham'])
    writer.writerow(['hello,worlds', 'good morning'])
    writer.writerow([1, 2, 3, 10])

# dict write
with open(r'input_data\output_data2.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, ['Name', 'Pet', 'Phone'])
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '111-2222'})
    writer.writerow({'Name': 'Bob', 'Pet': '', 'Phone': '333-5678'})

# remove header
os.makedirs(r'input_data\cp16', exist_ok=True)

for csv_fname in os.listdir(r'.\input_data'):
    if not csv_fname.endswith('.csv'):
        continue
    print('Removing header from ' + csv_fname + '...')

    row_data = []
    # read
    with open(os.path.join(r'.\input_data', csv_fname), 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            # １行目を取り除く
            if reader.line_num == 1:
                continue
            row_data.append(r)

    if len(row_data) == 0:
        continue

    # write
    with open(os.path.join(r'.\input_data\cp16', csv_fname), 'w', newline='') as f:
        writer = csv.writer(f)
        for r in row_data:
            writer.writerow(r)

print('------------')


#########################
# json
#########################
# json文字列
json_str_data = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
py_dic_val = {'isCat': True, 'miceCaught': 0,
              'name': 'Zophie', 'felineIQ': None}

# json文字列 => dict
jval = json.loads(json_str_data)
print(type(jval))
print(jval)
# dict => json文字列
jdump = json.dumps(py_dic_val)
print(type(jdump))
print(jdump)
# json文字列 => dict
temp_val = json.loads(jdump)
print(type(temp_val))
print(temp_val)


print('------------')

print('end')
