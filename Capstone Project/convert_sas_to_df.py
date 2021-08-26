import pandas as pd

def convert(ifile, label, columns, name):
    """Converts SAS Program file to pandas dataframe
    Parameters:
        ifile (str): SAS source code file.
        lable (str): sas value to extract.
        columns (list): list of 2 containing column names.
    Return:
        dataframe
    """

    readFile = ''
    with open(ifile) as f:
        readFile = f.read()

    readFile = readFile[readFile.index(label):]
    readFile = readFile[:readFile.index(';')]

    fileList = readFile.split('\n')[1:]
    codes = []
    values = []

    for line in fileList:

        if '=' in line:
            code, value = line.split('=')
            code = code.strip()
            value = value.strip()

            if code[0] == "'":
                code = code[1:-1]

            if value[0] == "'":
                value = value[1:-1]

            codes.append(code)
            values.append(value)


    pd.DataFrame(list(zip(codes,values)), columns=columns).to_csv(name + '.csv')

