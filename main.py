from conv_files import jconv,vcfconv,icomb
import pprint as pp
import os
data = {}

while(1):
    fpath = input("Drag and Drop the csv file here:>")
    if(os.path.exists(fpath)):
        with open(fpath,"r+") as csv:
            csvlist=csv.readlines()
            break
    else:
        print("Wrong Path..Try Again?")

basevalues=csvlist[0].rstrip().split(',')

for datline in csvlist[1:]:
    data_dict = {}
    tmp_data = datline.rstrip().split(',')
    for i in range(0,len(basevalues)):
        if(tmp_data[i]==''):
            continue
        data_dict[basevalues[i]] = tmp_data[i]
    data[data_dict['Name']] = data_dict

print(f"{len(data.keys())} contacts retrieved..")

while(1):
    ch = input("Do you want to see it[Y/N]: ")
    if ch.upper()=='Y':
        print(data.keys())
        break
    elif(ch.upper()!='N'):
        print("Wrong Choice")
    else:break



print()

print("In what form do you want\n1.JSON\t2.VCF\n")
while(1):
    try:
        choice = int(input(":> "))
        if(choice == 1 or choice ==2):break
        else:error
    except:
        print("Invalid Input\n")
        continue

if(choice == 1):
    jconv.conv(data)
elif(choice == 2):
    vcfconv.conv(data)