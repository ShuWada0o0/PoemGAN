# coding: utf-8
import csv

flag = 0
with open('outputHAIKU.csv','r') as f:
    with open('outputHAIKU_Main.csv', 'w') as a:
        with open('outputHAIKU_Main-Kigo.csv', 'w') as c:
            writer1 = csv.writer(a)
            writer2 = csv.writer(c)
            reader = csv.reader(f)
            for row in reader:
                if(flag == 0 ):
                    flag = 1
                else:
                    print(row)
                    writer1.writerow([row[0]]) 
                    writer2.writerow([row[0],row[2]])