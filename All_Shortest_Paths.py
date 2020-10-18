import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set()
# گراف پایه و شبکه اصلی با استفاده از گراف G ایجاد می شود
G=nx.Graph()
final_path=[]

def network(reader_cost,reader_points):
    matrix_points=np.array(reader_points)
    matrix_cost=np.array(reader_cost)
    for i in range(matrix_points.shape[0]):
        G.add_node(i,pos=(matrix_points[i,1],matrix_points[i,2]))
    for i in range (matrix_cost.shape[0]):
        G.add_edge(matrix_cost[i,0],matrix_cost[i,1], weight=matrix_cost[i,2])   
    weight=nx.get_edge_attributes(G,'weight') 
    pos=nx.get_node_attributes(G,'pos')  
    nx.draw_networkx(G,pos)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=weight,font_color='brown')
    plt.savefig("kashan_network",dpi=300,bbox_inches='tight')
                

reader_points =pd.read_excel(r'E:\learning_pymc3\Thesis_Code\All_shortest_paths_BaseGraph\Kashan\kashan_points.xlsx')
reader_cost =pd.read_excel(r'E:\learning_pymc3\Thesis_Code\All_shortest_paths_BaseGraph\Kashan\kashan_cost.xlsx')
reader_od =pd.read_excel(r'E:\learning_pymc3\Thesis_Code\All_shortest_paths_BaseGraph\Kashan\kashan_od.xlsx')   
network(reader_cost,reader_points)      

# با استفاده از دستور islice می توان k کوتاهترین مسیر را به تعداد مشخص شده در تابع ایجاد کرد
all_shortest_path=dict(nx.all_pairs_shortest_path(G))

primary_shortest_paths=[]
Final_all_shortest_path = []

for i in range(G.number_of_nodes()):
    for j in range(G.number_of_nodes()):
        
        # در اینجا با استفاده از دو حلقه تمام مسیرهای بین دو نقطه در گراف از حالت دیکشنری به لیست تبدیل می شود
        primary_shortest_paths.append(all_shortest_path[i][j])
        
     # در اینجا چنانچه طول مسیر برابر با یک یا همان نقطه شد از مسیرهای ممکن حذف می شود 
     # در Final_all_shortest_path مسیرها به صورت رفت و برگشت ایجاد می شود
for item in primary_shortest_paths:
    if len(item)>1:
        Final_all_shortest_path.append(item)
        
output_file=open("All_shortest_Paths1","w")
for item in Final_all_shortest_path:
    for item2 in item:
        
        # به دلیل اینکه در الگوریتم ژنتیک نقاط از 1 تا 15 است ولی در اینجا 0 تا 14 است.
        output_file.writelines(f'{item2+1}\t')
    output_file.writelines(f'\n[TYPE 3]\t')




