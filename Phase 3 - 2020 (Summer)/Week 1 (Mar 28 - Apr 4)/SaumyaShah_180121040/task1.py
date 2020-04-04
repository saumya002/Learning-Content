
import csv

import numpy as np
with open("data.csv",'r')as f :
    data_list = list(csv.reader(f, delimiter=" "))
da=np.array(data_list[1:])
print(da)