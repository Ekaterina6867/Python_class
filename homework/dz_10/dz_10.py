import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
unique_vals = data['whoAmI'].unique()
one_hot = pd.DataFrame(columns=unique_vals)
for val in unique_vals:
    one_hot[val] = (data['whoAmI'] == val).astype(int)
print(one_hot.head())