# در این ماژول، میان برگ های حاصل از درخت اشتاینر مسیرهای اولیه ایجاد می شود و در ادامه این مسیرها داخل الگوریتم ژنتیک گذاشته می شود.
import steiner_algorithm
import pandas as pd
import operator
from functools import reduce
reader_points =pd.read_excel(r'E:\learning_pymc3\Thesis_Code\Steiner_Algorithm\kashan\kashan_points.xlsx')
reader_cost =pd.read_excel(r'E:\learning_pymc3\Thesis_Code\Steiner_Algorithm\kashan\kashan_cost.xlsx')
reader_od =pd.read_excel(r'E:\learning_pymc3\Thesis_Code\Steiner_Algorithm\kashan\kashan_od.xlsx')   
steiner_tree(reader_cost,reader_od,reader_points) 
leafage=[]
primary_leaf_paths=[]
steiner_leaf_paths=[]
for i in range(sub_G.number_of_nodes()):
    if sub_G.degree[i]==1:
        leafage.append(i)
for i in range(len(leafage)):
    for j in range(len(leafage)):
        paths = list(nx.shortest_simple_paths(sub_G, leafage[i], leafage[j]))
        primary_leaf_paths.append(paths)

# چون خروجی کد بالا سه لیست تو در تو است با استفاده از تابع زیر لیست بیرونی حذف می شود.
primary_leaf_paths=reduce(operator.concat,primary_leaf_paths)  
for item in primary_leaf_paths:
    if len(item)>1:
        steiner_leaf_paths.append(item)
  
output_file=open("Steiner_leaf_Paths4","w")
for item in steiner_leaf_paths:
    for item2 in item:
        
        # به دلیل اینکه در الگوریتم ژنتیک نقاط از 1 تا 15 است ولی در اینجا 0 تا 14 است.
        output_file.writelines(f'{item2+1}\t')
    output_file.writelines(f'\n[TYPE 3]\t')