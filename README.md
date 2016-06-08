#FATROW

A fatrow is a name I use in the office to refer to an hbase row which possesses many values for 1 key. 

Example:

CarReg: A21BC , Seen1: Doctors, Seen2: Hospital, Seen3: Trainstation

1 Key - can have many results.

#Boiling down the CSV

The CSV data needs to be extracted and placed into a dictionary. For that purpose there is the process command.

it is formatted like this.

##process

Process a line of data. Adding the unique values to a dictionary. Please note: Duplicate values are removed.


#Example
from fatrow import fatrow

    fr = fatrow()
    fr.process('1,this')
    fr.process('1,test')
    fr.process('1,record')
    fr.process('2,junk')
    fr.process('1,a')
    fr.process('3,still')
    
    #See the output
    
    for k, v in fr:
        logger.debug('' + k + '--->' + str(v))
        
See the file **test.py** to check the output.