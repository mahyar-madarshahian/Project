import Kruskal_algorithm
import pandas as pd
import operator
from functools import reduce   
leafage=[]
primary_leaf_paths=[]
kruskal_leaf_paths=[]
for i in range(sub_G.number_of_nodes()):
    if sub_G.degree[i]==1:
        leafage.append(i)
print(leafage)
for i in range(len(leafage)):
    for j in range(len(leafage)):
        paths = list(nx.shortest_simple_paths(sub_G, leafage[i], leafage[j]))
        primary_leaf_paths.append(paths)
# چون خروجی کد بالا سه لیست تو در تو است با استفاده از تابع زیر لیست بیرونی حذف می شود.
primary_leaf_paths=reduce(operator.concat,primary_leaf_paths)  
for item in primary_leaf_paths:
    if len(item)>1:
        kruskal_leaf_paths.append(item)  
output_file=open("Kruskal_leaf_paths","w")
for item in kruskal_leaf_paths:
    for item2 in item:
        
        # به دلیل اینکه در الگوریتم ژنتیک نقاط از 1 تا 15 است ولی در اینجا 0 تا 14 است.
        output_file.writelines(f'{item2+1}\t')
    output_file.writelines(f'\n[TYPE 3]\t')