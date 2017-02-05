def replace98and96(column):
    new = []
    newval = column.max()
    for i in column:
        if (i == 96 | i == 98):
            new.append(newval)
        else:
            new.append(i)
    return new

def cleanHeaders(data):
    cleanCol = []
    for i in range(len(data.columns)):
        cleanCol.append(data.columns[i].replace('-', ''))
    data.columns = cleanCol