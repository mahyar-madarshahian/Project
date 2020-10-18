import boruvka_algorithm
import pandas as pd  
# در اینجا تمام مسیرها با استفاده از الگوریتم کوتاهترین مسیر بر روی گراف درخت اشتاینر در دیکشنری ایجاد می شود
all_shortest_path=dict(nx.all_pairs_shortest_path(sub_G))

primary_shortest_paths=[]
Final_all_shortest_path = []

for i in range(sub_G.number_of_nodes()):
    for j in range(sub_G.number_of_nodes()):
        
        # در اینجا با استفاده از دو حلقه تمام مسیرهای بین دو نقطه در گراف از حالت دیکشنری به لیست تبدیل می شود
        primary_shortest_paths.append(all_shortest_path[i][j])
        
     # در اینجا چنانچه طول مسیر برابر با یک یا همان نقطه شد از مسیرهای ممکن حذف می شود 
     # در Final_all_shortest_path مسیرها به صورت رفت و برگشت ایجاد می شود
for item in primary_shortest_paths:
    if len(item)>1:
        Final_all_shortest_path.append(item)
        
output_file=open("Boruvka_All_Paths","w")
for item in Final_all_shortest_path:
    for item2 in item:
        
        # به دلیل اینکه در الگوریتم ژنتیک نقاط از 1 تا 15 است ولی در اینجا 0 تا 14 است.
        output_file.writelines(f'{item2+1}\t')
    output_file.writelines(f'\n[TYPE 3]\t')