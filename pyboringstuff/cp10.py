import shutil, os
from pathlib import Path

print('start')


# file_dir = Path(os.path.dirname(__file__)).parents[0] / Path('sample')
file_dir = Path(os.path.dirname(__file__)) / Path(r'..\sample')
print("dir=" + str(file_dir))
if not file_dir.is_dir():
    file_dir.mkdir()
file_path = file_dir / 'cp_test_1.txt'
# create/write
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('test writing')

copy_file_path = file_dir / 'cp_test_2.txt'
# copy
shutil.copy(file_path, copy_file_path)

# move
move_file_path = file_dir / 'cp_test_move.txt'
shutil.move(file_path, move_file_path)


print('---------')

for dname,subdnames,fnames in os.walk(r'C:\workspace\study\python\python_study'):
    print('dir=' + dname)
    for sname in subdnames:
        print('sub_dir=' + sname)
    for fn in fnames:
        print('file=' + fn)
    print('*****')


print('end')