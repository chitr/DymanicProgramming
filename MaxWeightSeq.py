import sys
import os
import copy

max_weight_list={}
#53 3 5 67 10 8 105
def get_max_weight(data_graph,index):
    print "INDEX  :: "+str(index)
    if index == -1:
        tmp_dict={0:[int('-1')]}
        print tmp_dict
        max_weight_list[int(-1)]=tmp_dict
        print max_weight_list
        return 0
    if index == 0:
        print data_graph
        tmp_dict={copy.deepcopy(int(data_graph[index])):[0]}
        max_weight_list[index]=tmp_dict
        print max_weight_list[index]
        return data_graph[index]
    
    print "INDEX : "+str(index)
    print max_weight_list
    wt1=copy.deepcopy(max_weight_list[index-1].keys()[0])
    print "wt1   :"+str(wt1)
    print max_weight_list[0]
    wt2=copy.deepcopy(int(max_weight_list[index-2].keys()[0] )) + copy.deepcopy(int(data_graph[index]))
    print "wt2  :"+str(wt2)
    
    if wt1 > wt2 :
        max_weight_list[index]=copy.deepcopy(max_weight_list[index-1])
        tmp_list=copy.deepcopy(max_weight_list[index-1].values()[0])
    else:
        print max_weight_list
        tmp_list = copy.deepcopy(max_weight_list[index-2].values()[0])
        tmp_list.append(index)
        print max_weight_list
        print tmp_list
        max_weight_list[index]={wt2:tmp_list}
        
    print max_weight_list[index]
    print max_weight_list
    print "WEIGHT LIST IS :"+str(tmp_list)
    
    for i in tmp_list:
        if i != -1:
            print data_graph[i]
    
    return max(wt1,wt2)
    
if __name__ == "__main__":
    len=len(sys.argv)
    array=sys.argv[1:]
 
    print "======================================="
 
    for i in range(-1,int(len-1)):
        print "INDEX :"+str(i)
        get_max_weight(array,i)
        print "======================================="
