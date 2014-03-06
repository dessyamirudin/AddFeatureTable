'''
Created on 24 Feb 2014

@author: TOSHIBA
'''

import csv

def main():
    with open('test1.csv','rU') as csvinput:
        row_tuple={}
        reader=csv.reader(csvinput)
        col_key=[]
        for row in reader:
            col1=row[0]
            col2=row[1:]
            col_key.append(col1)
            row_tuple[col1]=col2
            #print row
        #col1=[x[0] for x in reader]
        #col2=[x[1] for x in reader]
        #print len(row_tuple)
    num_col_1=row_tuple['Data'].index('Column 1')
    num_col_2=row_tuple['Data'].index('Column 2')
    #adding value for Column 3
    for i in range (len(col_key)):
        if row_tuple[col_key[i]][num_col_1]=='1' and row_tuple[col_key[i]][num_col_2]=='2':
            row_tuple[col_key[i]].append('3')
        else:
            row_tuple[col_key[i]].append('Column 3')
        
    #creating the list
    col_range=len(row_tuple[col_key[0]])+1
    row_val_master=[]
    for x in range (len(col_key)):
        row_val=[]
        #for i in range(col_range):
        row_val=[col_key[x]]+row_tuple[col_key[x]]
        print row_val
        row_val_master.append(row_val)
    #for i in range (1):
        #row_val=[col_key[i]]+row_tuple[col_key[i]]
        #print(col_key[i],row_tuple[col_key[i]])  
    
    print row_val_master
    
    #writing
    with open('test_add_col_v3.csv','wb') as csvoutput:
        writer=csv.writer(csvoutput)
        for ind in range (len(col_key)):
            writer.writerow(row_val_master[ind])
                
if __name__=='__main__':
    main()