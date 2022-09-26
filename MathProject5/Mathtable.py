def printOperationTable(operation, numRows=9, numColumns=9):
    nwidth = len(str(eval('{}{}{}'.format(numRows, operation, numColumns))))
    rwidth = len(str(numRows))
 
    print('{}'.format(' '*rwidth), ('{:{nwidth}}'*numColumns).format(*range(1, numColumns+1), nwidth=nwidth+1))
    for r in range(1, numRows+1):
        print('{:{rwidth}} '.format(r, rwidth=rwidth), end='')
        for c in range(1, numColumns+1):
            print('{:{nwidth}}'.format(eval('{}{}{}'.format(r, operation, c)), nwidth=nwidth+1), end='')
        print()
    print()
 
printOperationTable('+',  5, 5)
printOperationTable('*',  5, 5)
printOperationTable('**', 5, 5)