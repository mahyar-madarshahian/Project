import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from itertools import islice
sns.set()
# گراف پایه و شبکه اصلی با استفاده از گراف G ایجاد می شود
# گراف درخت اشتاینر با استفاده از گراف sub_G ایجاد می شود
# گراف Virtual_G به منظور ذخیره کوتاه مدت عضوهای غیر مشترک برای توسعه درخت اشتاینر استفاده می شود.
G=nx.Graph()
sub_G=nx.Graph()
virtual_G=nx.Graph()
final_path=[]
sub_trees=[]
sub_trees_nodes=[]
sub_trees_degree=[]
maxdegree_nodes_trees=[]
forest_nodes=[]

def steiner_tree(reader_cost,reader_od,reader_points):
    matrix_points=np.array(reader_points)
    matrix_cost=np.array(reader_cost)
    matrix_od=np.array(reader_od)
    for i in range(matrix_points.shape[0]):
        sub_G.add_node(i,pos=(matrix_points[i,1],matrix_points[i,2]))
    for i in range(matrix_points.shape[0]):
        G.add_node(i,pos=(matrix_points[i,1],matrix_points[i,2]))
    for i in range (matrix_cost.shape[0]):
        G.add_edge(matrix_cost[i,0],matrix_cost[i,1], weight=matrix_cost[i,2])   
    weight=nx.get_edge_attributes(G,'weight') 
    pos=nx.get_node_attributes(G,'pos')
    list_max=[]
    for item in matrix_od[:,-1]:
        list_max.append(item)
    # ماکزیمم اول و دوم را در لیست ایجاد شده شناسایی کن
    first_max=max(list_max[0],list_max[1])
    second_max=0
    for item in range(2,len(list_max)):
        if list_max[item]>first_max:
            second_max=first_max
            first_max=list_max[item]
        elif list_max[item]>second_max:
            second_max=list_max[item]
    print(list_max.index(first_max),list_max.index(second_max))
# با استفاده از دستور islice می توان k کوتاهترین مسیر را به تعداد مشخص شده در تابع ایجاد کرد
    paths = list(islice(nx.shortest_simple_paths(G, list_max.index(first_max), list_max.index(second_max)), 10))

    for i in range(len(paths)):
# با استفاده از zip یال های بین دو گره متوالی در کوتاهترین مسیر ایجاد شده، ساخته می شود
        path_edges = list(zip(paths[i],paths[i][1:]))
        virtual_G.add_edges_from(path_edges)
        diff_path = (virtual_G.edges-sub_G.edges)
        sub_G.add_edges_from(diff_path)
        virtual_G.remove_edges_from(path_edges)
        if nx.cycle_basis(sub_G):
            sub_G.remove_edges_from(diff_path)
        else: 
            pass
    matrix_od[list_max.index(first_max),-1]=0
    matrix_od[list_max.index(second_max),-1]=0
    if np.count_nonzero(matrix_od[:,-1])>1:
        final_path.append(path_edges)
        steiner_tree(reader_cost,matrix_od,reader_points)
    else:
# در اینجا اگر درخت یکتا تشکیل نشده و جنگلی از درختان تشکیل شده باشد میبایست جنگلها را به هم از گره هایی که بیشترین درجه را در هر درخت دارند و از کوتاهترین مسیر به همدیگر متصل کنیم
        if nx.number_connected_components(sub_G)!=0:
            
# در اینجا درختان با توجه به تعداد گره های هر درخت اولویت بندی می شوند
            sub_trees=sorted(nx.connected_components(sub_G), key = len, reverse=True)
            for i in sub_trees:
                sub_trees_nodes=list(i)
                for item in sub_trees_nodes:
                    
                    # در اینجا درجه هر گره در هر درخت مشخص می شود
                   sub_trees_degree.append(sub_G.degree[item])
                   
                   # در اینجا شماره گره و درجه آن گره در یک تاپل و داخل یک لیست کلی قرار می گیرد.
                tree_node_degree=list(zip(sub_trees_nodes,sub_trees_degree))
                
                # در اینجا ماکزیمم درجه گره ها در هر درخت مشخص می شود
                max_degree=(max(tree_node_degree, key=(lambda x:x[1])))
                
                # در اینجا گره هایی هر درخت با بیشترین درجه انتخاب و داخل لیست قرار می گیرد
                forest_nodes.append(max_degree)
                
                # در اینجا کا کوتاهترین مسیر بین گره های دو درخت با بیشترین درجه ایجاد می شود.
            new_path = list(islice(nx.shortest_simple_paths(G, forest_nodes[0][0], forest_nodes[1][0]), 3))
            for i in range(len(new_path)):
# با استفاده از zip یال های بین دو گره متوالی در کوتاهترین مسیر ایجاد شده، ساخته می شود
                path_edges = list(zip(new_path[i],new_path[i][1:]))
                virtual_G.add_edges_from(path_edges)
                diff_path = (virtual_G.edges-sub_G.edges)
                sub_G.add_edges_from(diff_path)
                virtual_G.remove_edges_from(path_edges)
                if nx.cycle_basis(sub_G):
                    sub_G.remove_edges_from(diff_path)
                else: 
                    pass
    plt.figure()
    nx.draw_networkx(G,pos)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=weight,font_color='brown')
    nx.draw_networkx_edges(G,pos,edgelist=sub_G.edges,edge_color='r',width=5)
    #plt.savefig("steiner_network.jpg",dpi=300,bbox_inches='tight')
    return(sub_G.edges)









