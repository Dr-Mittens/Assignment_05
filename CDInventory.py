                                                            #------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (James Miller (JM), 2/27/22, Updating inventory lists to a dictionary format)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
DRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
fromfile = [] #JM for use in loading data

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        objFile = open(strFileName, 'r')
        filestring = objFile.read()
        objFile.close()
        filestring = filestring.replace('\n',',')
        lfile = filestring.split(',')
        lfile = lfile[:-1]
        moving = 0
        reps = len(lfile)//3
        if reps > 0:
            for n in range(reps):
                dfile = {'id':int(lfile[moving+0]), 'Song':lfile[moving+1], 'Artist':lfile[moving+2]}
                fromfile.append(dfile)
                moving +=3
        for row in lstTbl:
            fromfile.append(row)
        lstTbl = fromfile
        fromfile = []
        # TODO Add the functionality of loading existing data
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        DRow = {'ID': intID, 'Song': strTitle, 'Artist': strArtist} #JM converted inner list to a dictionary
        lstTbl.append(DRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ') #JM edited to return the values of the dictionary
    elif strChoice == 'd':
        Elim = input('Please enter the ID value of the song to remove, or ALL to delete the current log. \nTo leave press enter')
        if Elim == 'ALL':
            LstTbl = []
        elif not Elim.isdigit():
            continue
        else:
            for item in lstTbl:
                if item['ID'] == int(Elim):
                    lstTbl.remove(item) 
                    #JM: I'm a bit confused, as the assignment asks us to add inventory removal but also not to use functions
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values(): #JM pretty sure this is functional formating for pulling from dictionary
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

