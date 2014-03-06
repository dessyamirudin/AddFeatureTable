'''
Created on 24 Feb 2014

@author: TOSHIBA
'''

import csv

def main():
    with open('test.csv','rU') as csvinput:
        col1=[]
        col2=[]
        col3=[]
        reader=csv.reader(csvinput)
        for row in reader:
            col1.append(row[0])
            col2.append(row[1])
            #print row
        #col1=[x[0] for x in reader]
        #col2=[x[1] for x in reader]
        
        for i in range (len(col1)):
            if col1[i]=='1' and col2[i]=='2':
                col3.append('3')
            else:
                col3.append('Column 3')
    csvinput.close()
    
    
    with open('test_add_col.csv','wb') as csvoutput:
        writer=csv.writer(csvoutput)
        for ind in range (len(col1)):
            writer.writerow([col1[ind]]+[col2[ind]]+[col3[ind]])
            
                
    #print [x for x in reader]
    num=col1.index('Column 1')
    print num
    print col1
    print col2
    print col3
            
if __name__=='__main__':
    main()