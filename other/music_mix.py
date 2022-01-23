import os
from random import randint

dir = r'E:\music'
files = os.listdir(dir)
nums = list()

while len(nums) < len(files):
    a = randint(0, len(files))
    if a not in nums:
        nums.append(a)

for n, i in enumerate(files):
    old_name = os.path.join(dir, i)
    i = ''.join(i.split()[1:])
    new_name = os.path.join(dir, f'{nums[n]}. {i}')
    os.rename(old_name, new_name)
