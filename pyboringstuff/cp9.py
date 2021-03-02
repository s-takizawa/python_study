from pathlib import Path
import os

print("start")

# my_files = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in my_files:
#     print(Path(r'C:\Users\AI', filename))

# print('--------------')

# home_foldere = Path('C:\workspace\study\python\python_study')
# sub_folder = Path('sample')

# data_folder = home_foldere / sub_folder

# print(data_folder)

# print('--------------')

file_dir = Path(os.path.dirname(__file__)).parents[0] / Path('sample')
print("dir=" + str(file_dir))

if not file_dir.is_dir():
    file_dir.mkdir()

file_path = file_dir / 'hello.txt'

# create/write
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('abc\n')
    f.write('あいうえお')

# read
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)


print("end")