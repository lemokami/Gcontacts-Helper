import base64 as b64

def conv(param_dict):
    with open("decoded-vcf.vcf","w+") as f:
        for i in param_dict.keys():
            ln=''
            f.write("BEGIN:VCARD\nVERSION:2.1\n")
            if (i.split()[-1]) != (i.split()[0]):
                ln = i.split()[-1]
            f.write(f"N:{ln};{i.split()[0]};;;\n")
            f.write(f"FN:{i}\n")
            f.write(f"TEL;CELL: {param_dict[i]['Phone 1 - Value']}\n")
            f.write("PHOTO;ENCODING=BASE64;JPEG:{}\n")

            try:
                f.write(f"NOTE:Birthday : {param_dict[i]['Birthday']}\n")
                f.write("END:VCARD\n")
            except:
                f.write("END:VCARD\n")
                
