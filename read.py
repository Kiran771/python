#function to read the landinfo txt 
def read_land_info():
    with open("Landinfo.txt","r") as file:
        kittaNumber=101
        land_info={}
        for line in file:
            line=line.replace("\n","")
            land_info[kittaNumber]=(line.split(","))
            kittaNumber+=1
    return land_info
#fucntion to read the invoice 
def print_info(invoice_filename):
    """
    takes one parameter invoice_filename
        invoice_filename (str):text file for generating invoic for renting and returning land
    """
    #open invoice-filename in read mode
    with open(invoice_filename,"r") as file:
        for line in file:
            print(line)

           
            
