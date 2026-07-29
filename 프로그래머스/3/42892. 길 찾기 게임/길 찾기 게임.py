

import sys
sys.setrecursionlimit(10**6)



def solution(nodeinfo):
    answer = []
    pre_result = []
    post_result = []
    
    # 일단 맵을 만들어?
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    nodeinfo.sort(key=lambda x : (-x[1],x[0]))
    
    def traverse(node_list,pre):
        if not node_list:
            return

        root = node_list[0] 

        left_nodes = [node for node in node_list[1:] if node[0] < root[0]]
        right_nodes = [node for node in node_list[1:] if node[0] > root[0]]
        
        if pre:
            pre_result.append(root[2]) 
            traverse(left_nodes,pre)
            traverse(right_nodes,pre)
        
        else:
            traverse(left_nodes,pre)
            traverse(right_nodes,pre)
            post_result.append(root[2]) 
    
    traverse(nodeinfo,True)
    traverse(nodeinfo,False)
    
    
    answer.append(pre_result)
    answer.append(post_result)
    
    return answer