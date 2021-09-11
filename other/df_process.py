import pandas as pd
from time import time

start = time()

df = pd.read_excel(open('data\DF_properties.xlsx', 'rb'))

skin = []
face = []
eyes = []
clothing = []
hair = []
haircolour = []
for num in range(len(df)):
    # Layer 1 process
    l1 = df['Layer_1'][num].split('_')
    skin.append(l1[0])
    face.append(l1[1])
    eyes.append(' '.join(l1[2:]))
    # Layer 2 process
    l2 = df['Layer_2'][num].split('_')
    clothing.append(' '.join(l2))
    # Layer 5 process
    l5 = df['Layer_5'][num].split('_')
    hair.append(l5[0])
    haircolour.append(' '.join(l5[1:]))


df.insert(2, 'Skin', skin)
df.insert(3, 'Face', face)
df.insert(4, 'Eyes', eyes)
df.insert(6, 'Clothing', clothing)
df.insert(10, 'Hair/Hat', hair)
df.insert(11, 'Haircolour', haircolour)

df.to_excel(r'data\new_df.xlsx')

print(f'Execution time: {time()-start:.2f}')