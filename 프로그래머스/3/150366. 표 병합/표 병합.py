def solution(commands):
    answer = []
    
    SaveList = [["" for i in range(51)] for i in range(51)]
    parent = [[(r, c) for c in range(51)] for r in range(51)]
    
    def find_root(r, c):
        if parent[r][c] == (r, c):
            return (r, c)
        parent[r][c] = find_root(parent[r][c][0], parent[r][c][1])
        return parent[r][c]
    
    for i in commands:
        Command = i.split(" ")
        Way = Command[0]
        
        if Way == "UPDATE":
            if len(Command) == 4:
                r = int(Command[1])
                c = int(Command[2])
                Val = Command[3]
                
                R_r, R_c = find_root(r, c)
                SaveList[R_r][R_c] = Val
            else:
                Val_1 = Command[1]
                Val_2 = Command[2]
                
                for r in range(len(SaveList)):
                    for c in range(len(SaveList[0])):
                        if SaveList[r][c] == Val_1:
                            SaveList[r][c] = Val_2
                            
        elif Way == "MERGE":
            r1 = int(Command[1])
            c1 = int(Command[2])
            r2 = int(Command[3])
            c2 = int(Command[4])
            
            Par_r1, Par_c1 = find_root(r1, c1)
            Par_r2, Par_c2 = find_root(r2, c2)
            
            if (Par_r1, Par_c1) != (Par_r2, Par_c2):
                parent[Par_r2][Par_c2] = (Par_r1, Par_c1)
                
                if SaveList[Par_r1][Par_c1] == "" and SaveList[Par_r2][Par_c2] != "":
                    SaveList[Par_r1][Par_c1] = SaveList[Par_r2][Par_c2]
                SaveList[Par_r2][Par_c2] = ""
                
        elif Way == "UNMERGE":
            r = int(Command[1])
            c = int(Command[2])          
            
            Par_r, Par_c = find_root(r, c)
            SaveValue = SaveList[Par_r][Par_c]
            
            unmerge_list = []
            for r_idx in range(len(parent)):
                for c_idx in range(len(parent[0])):
                    if find_root(r_idx, c_idx) == (Par_r, Par_c):
                        unmerge_list.append((r_idx, c_idx))
                        
            for u_r, u_c in unmerge_list:
                parent[u_r][u_c] = (u_r, u_c)
                SaveList[u_r][u_c] = ""
            
            SaveList[r][c] = SaveValue
            
        elif Way == "PRINT":    
            r = int(Command[1])
            c = int(Command[2])          
            
            Par_r, Par_c = find_root(r, c)
            
            if SaveList[Par_r][Par_c] == "":
                answer.append("EMPTY")
            else:
                answer.append(SaveList[Par_r][Par_c])
    
    return answer