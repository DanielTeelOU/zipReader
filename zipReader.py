from zipfile import ZipFile #to manage the zip file
import datetime #for date modified
import sys #to read output

def main():
        # specifying the zip file name, getting input from user
        file_name = input("Enter the Path to the parent directory: \n")
        zipRead(file_name)

def zipRead(file):
    # opening the zip file in READ mode to gather data
        original = sys.stdout
        sys.stdout = open('zipProperties.txt', 'w')
        with ZipFile(file, 'r') as zip: 
                for info in zip.infolist(): 
                        print(info.filename + "\t" + str(datetime.datetime(*info.date_time)) + "\t" + str(float(info.compress_size) / 1024) + ' kb')
                        #print('\tModified:\t' + str(datetime.datetime(*info.date_time))) 
                        #print('\tCompressed:\t' + str(info.compress_size) + ' bytes') 
                        #print('\tUncompressed:\t' + str(info.file_size) + ' bytes') 
        sys.stdout = original

main()