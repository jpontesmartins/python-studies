import os
import shutil
import glob
import sys
import re
from datetime import date


print('==================================')
print('studiyng standatd library in python (part 1)')
print('==================================\n')


# current directory
print(f'get cwd: {os.getcwd()}')

# print(f'dir: {dir(os)}')

# copy README.md file and paste as README2.md at the same dir
# shutil.copyfile('../README.md','../README2.md')

# glob
files_with_py_extension = glob.glob('*.py')
print(f'glob: {files_with_py_extension}')

# sys
print(f'sys argv: {sys.argv}')

# re
text = 'which foot or hand fell fastest'
starting_with_f_letter = re.findall(r'\bf[a-z]*',text)
print(f"starting with 'f' letter: {starting_with_f_letter}")

another_text = 'tea for too'
print(f" replacing..: {another_text.replace('too','two')}")

# datetime
now = date.today()
print(f'now: {now}')

# formatting date
other_now = now.strftime('%d/%m/%Y | %d %b %y | %H:%M:%S')
print(f'now: {other_now}')

print(f"now1: {now.strftime('%c')} ")

# link to formats to date
# link: https://docs.python.org/3/library/datetime.html#module-datetime
