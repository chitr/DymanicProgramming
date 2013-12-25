import os
import sys
import copy



max_wt_seq=[]
max_val=[]
max_list={}
count=0

def get_max_wt_val(i,vi,wi,max_w):
    print "============"+str(i)+"======================"
    
    tmp_wt={}
    t_list={}
    if i==0:
        
        
        print max_w
    
            
        for r in range(int(max_w)+1):
            if int(r) < int(wi):                
                t_list={0:{0:[int('-1')]}}
                print r
                tmp_wt[r]=t_list
            else:
                t_list={wi:{vi:[i]}}
                print r
                tmp_wt[r]=t_list
        print tmp_wt        
        max_val.append(tmp_wt)
        print str(max_val)
        return 
    
    
        
    for r in range(int(max_w)+1):
        print "---------------"+str(r)+"-----------------------"
        print str(max_val[int(i)-1].values()[int(r)])
        i_1_wt_data=copy.deepcopy(max_val[int(i)-1].values()[int(r)])
        print str(i_1_wt_data)
        i_1_wt=i_1_wt_data.keys()[0]
        i_1_val_data=copy.deepcopy(i_1_wt_data.values()[0])
        
        print "INDEX:"+str(int(i)-1)
        print "RANGE:"+str(r)+"#WEIGHT: "+str(i_1_wt)+"#VAL: "+str(i_1_val_data.keys()[0])
        
        val1=i_1_val_data.keys()[0]
        print "VAL1:"+str(val1)
        print "VAL1 wt:"+str(i_1_wt)+" VAL1 list:"+str(i_1_val_data.values()[0])
        val1_wt=copy.deepcopy(i_1_wt)
        val1_list=copy.deepcopy(i_1_val_data.values()[0])
        
        val2=0
        val2_wt=0
        val2_list=[]
        if int(wi) <= int(r):
            r_wi=int(r)-int(wi)
            print "r-wi:"+str(r_wi)
            if int(r_wi) >int(0):
                    r_wi_wt_data=copy.deepcopy(max_val[int(i)-1].values()[int(r_wi)])
                    r_wi_val_data=copy.deepcopy(r_wi_wt_data.values()[0])
                    val2=int(r_wi_val_data.keys()[0])+int(vi)
                    print "VAL2:"+str(val2)
                    val2_wt=int(r_wi_wt_data.keys()[0]) + int(wi)                    
                    val2_list=copy.deepcopy(r_wi_val_data.values()[0])
                    val2_list.append(i)
                    print "VAL2 wt:"+str(val2_wt)+" VAL2 LIST:"+str(val2_list)
            else :
                val2_wt=copy.deepcopy((wi))
                val2_list=[i]
                val2=copy.deepcopy(vi)
          
        
        print "RANGE :"+str(r)+" w1:"+str(val1_wt)+" w2 :"+str(val2_wt)
        
        opt_wt=0
        if int(val1) > int(val2):
            t_list={val1_wt:{val1:val1_list}}
            opt_wt=val1_wt
        else:
            t_list={val2_wt:{val2:val2_list}}
            opt_wt=val2_wt
        print "R: "+str(r)+"OPT wt:"+str(opt_wt)
        
        tmp_wt[r]=t_list
        print tmp_wt
          
        
    max_val.append(tmp_wt)    
        
        
    
    
 






if __name__=="__main__":
    print "SYSARG"+str(sys.argv)
    if 4 != len(sys.argv) :
        print "Usage: "+str(sys.argv[0])+" <',' separated value of items> <',' separated wt of items > <Max allowed weight>"
    
    
    #Enter values of items , weight of each item and Max weight
    value=list(sys.argv[1].split(','))
    weight=list(sys.argv[2].split(','))
    count=len(weight)
    max_w=int(sys.argv[3])
    
    for i in range(0,len(value)):
        get_max_wt_val(i,value[i],weight[i],max_w)
    
    
    
