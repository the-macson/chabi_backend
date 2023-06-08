def file_type(ext_type, file_list):
    ext_type = ext_type.split(';')
    ext_type = [i.split(',') for i in ext_type]
    ext_type = dict(ext_type)
    file_type = {}
    for i in file_list:
        if i.split('.')[-1] in ext_type.keys():
            file_type[i] = ext_type[i.split('.')[-1]]
        else:
            file_type[i] = 'unknown'
    return file_type

print(file_type("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg", "xyz.xls", "text.csv", "123"]))
