# =============================================================================
# Files 1- Grok 12 File IO
# Created textfile: somebody.txt
# =============================================================================
file_object = open("zzsomebody.txt", 'r')
file_object.close()


file_object=open("zzsomebody.txt", 'r')
content=file_object.read()
file_object.close()
print(content)



fo=open("zzsomebody.txt", 'r')
linenumber=1
for line in fo:
    print(strline)
    linenumber+=1
fo.close()


" Appending and altering files "
fo=open('zzsomebody.txt', 'a')
fo.write('Random text to display at the end of the line')
fo.close()

fo=open('text2.txt', 'w')
fo.write('This is a new string that will replace our prev text')
fo.close()

"Creating a new file"
fp = open("zzNewTextFile.txt", "w")
fp.write('Random line in new textfile')
fp.close()


# =============================================================================
# Files 2- Grok 12 CSV files
# Created zzmax_temp.csv
# Created textfile: somebody.txt# =============================================================================
import csv

with open("zmax_temp.csv") as fo:
    for line in fo:
        print(line)
    
with open("zmax_temp.csv") as fo:
    content=csv.reader(fo)
    for line in content:
        print(line)


# For csv files, us csv reader to make it a list of values
fo=open("zmax_temp.csv")
content=csv.reader(fo)
print(next(content))
for line in content:
    print(line)
fo.close()




# Handling CSV files
fo=open("zmax_temp.csv")
content=csv.reader(fo)
header=next(content)
for line in content:
    Cityname=line[0]
    ## to calculate the average of the 12 months
    sum1=float()
    for elem in line[1:]:
        sum1+=float(elem)
    AvgOfMonths=sum1/12
    print(Cityname, round(AvgOfMonths,2))


'''Handling csv files as dictionaries'''
fo=open('zmax_temp.csv')
content=csv.DictReader(fo)
for row in content:
    print(row)
fo.close()


fo=open('zmax_temp.csv')
content=csv.DictReader(fo)
for row in content:
    print(row)
fo.close()



'''Handling csv files as 2d data '''
fo = open("zzmax_temp.csv")
content=csv.reader(fo); content
content2=list(content); content2
print(content2[0][2])  #note, [column][row]
fo.close()






""" writing csv files """
import csv
data_2d = [['H1', 'H2', 'H3', 'H4'],[1, 2, 3], [4, 5, 6, 7]]; data_2d
csv_file = open("zNewData.csv", "w")
writer = csv.writer(csv_file)
writer.writerows(data_2d)
csv_file.close()

fh=open('zNewdata.csv','r')
data=csv.reader(fh)
header=next(data); header
for line in data:
    print(line)
