from conv_files import icomb
def conv(param_dict):
    with open("decoded-vcf.vcf","w+") as f:
        for i in param_dict.keys():
            ln=''
            f.write("BEGIN:VCARD\nVERSION:2.1\n")
            if (i.split()[-1]) != (i.split()[0]):
                ln =" ".join(i.split()[1:])
            f.write(f"N:{ln};{i.split()[0]};;;\n")
            f.write(f"FN:{i}\n")
            f.write(f"TEL;CELL: {param_dict[i]['Phone 1 - Value']}\n")

            try:
                f.write(f"PHOTO;ENCODING=BASE64;JPEG:{icomb.imgmaker(param_dict[i]['Photo'])}\n")
                print(f"downloading {i}'s image")
            except:pass
            try:
                f.write(f"NOTE:Birthday : {param_dict[i]['Birthday']}\n")
                f.write("END:VCARD\n")
            except:
                f.write("END:VCARD\n")
                
