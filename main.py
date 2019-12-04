from conv_files import jconv,vcfconv
import pprint as pp

data = {}

#taking values from the csv file
with open("decode/contacts.csv","r+") as csv: # change values to suite your file
    csvlist=csv.readlines()

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

if(input("Do you want to see it[Y/N]: ").upper()=='Y'):
    print(data.keys())
print()
choice = int(input("In what form do you want\n1.JSON\n2.VCF\n>> "))

if(choice == 1):
    jconv.conv(data)
elif(choice == 2):
    vcfconv.conv(data)