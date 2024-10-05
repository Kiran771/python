import random
import datetime
from read  import * 
#Function for the header of invoice
def header(customer_name,datetime_invoice):
  """
  function to generated header of the invoice that generate txt file named with customer_name and datetime_invoice
  takes two parameter customer_name and datetime_invoice.
  customer_name (str): Name of the customer for whome the invoice is being generated
  datetime_invoice(int):Date and time at which the land is rented or returned
  return none
  """
  invoice_filename=customer_name+str(datetime_invoice.date())+".txt"
  #open a file in write mode
  with open(invoice_filename,"w") as bill:
     bill.write("\t\t\t\t\t\t\t\t\t\t\t\tTechnoproperty Nepal\n")
     bill.write("\t\t\t\t\t\t\t\t\t\t\tAddress:Kamalpokhari Kathmandu\n")
     bill.write("\t\t\t\t\t\t\t\t\t\tContact:980000000012||Email:technorental@gmail.com\n")
     bill.write("\n")
     bill.write("Bill No.:"+str(random.randint(2737,4307))+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+str(datetime_invoice)+"\n")
     bill.write("\n")
     bill.write("Name of the customer:"+customer_name+"\n")
     bill.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
     bill.write("\n")

#function to update the availability  of the land in LandInfo.txt file
def write_land_text(kitta_number):
  """
  function to perform the changes on the availability of land with respect to kitta_number(key)
  takes kitta_number as parameter
  kitta_number(int):kitta number of the land that is being rented or returned
  return none
  """
  land_info=read_land_info()
  #check if the land of the provided kitta number is available or not
  if land_info[kitta_number][4].strip()=="Available":
    #if it is available change the status to Not Available
    land_info[kitta_number][4]="Not Available"
  else:
    #change the status to Availabel
    land_info[kitta_number][4]="Available"
  #open LandInfo.txt in write mode
  with open("LandInfo.txt","w") as file:
    #iterate land_info values
    for details in land_info.values():
      file.write(details[0]+","+details[1]+","+details[2]+","+details[3]+","+details[4]+"\n")

#function to create the invoice while renting land         
def create_invoice_rentland(rent_land_details,customer_name,datetime_invoice,grand_total):
   """
      takes 4 parameters:
      rent_land_details(2Dlist):store the details of rented land
      customer_name (str): Name of the customer who rent the land
      datetime_invoice (str): date and time at which the land is rented
      grand_total(int):total amount of the land
       
      return none
   """ 
   invoice_filename=customer_name+str(datetime_invoice.date())+".txt"
   #open a file in append mode
   with open(invoice_filename,"a") as bill:
      bill.write("Kitta No.\t\t\t City\t\t\t Direction\t\t\t Aana\t\t\t Rent Duration\t\t\t Price per month\t\t\t Total amount")
      bill.write("\n")
      bill.write("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
      bill.write("\n")
      #iterate rent_land_details
      for details in rent_land_details:
        bill.write(str(details[0])+"\t\t\t\t"+details[1]+"\t\t"+details[2]+"\t\t\t"+str(details[3])+"\t\t\t" +str(details[4])+"\t\t\t\t"+str(details[5])+"\t\t\t\t\t" +str(details[6])+"\n")
        bill.write("\n")
      bill.write("Grand Total:"+str(grand_total))
      bill.write("\n")
   print_info(invoice_filename)
    
#function to create the invoice while returning land     
def create_invoice_returnland(return_land_details,customer_name,datetime_invoice,fine_none,grand_total):
   """
      takes 5 parameters:
      return_land_details(2Dlist):Store the details of land that is returned
      customer_name (str): Name of the customer returning the land
      datetime_invoice (str): Return date and time of land
      fine_none (int): fine amount according the return duration of land
      grand_total(int):total amount of rent after adding rent
      return none
   """
   invoice_filename=customer_name+str(datetime_invoice.date())+".txt"
   #open a file in append mode
   with open(invoice_filename,"a") as bill:
     
    if fine_none== "fine":
      bill.write("Kitta No.\t\t City\t\t Direction\t\t Aana\t\t Rent Duration\t\t Price per month\t\tFine/Discount\t\t Total amount")
      bill.write("\n")
      bill.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
      for details in return_land_details:
        bill.write(str(details[0])+"\t\t\t" +details[1]+"\t"+details[2]+"\t\t"+str(details[3])+"\t\t\t"+str(details[4])+"\t\t" +str(details[5])+"\t\t\t\t"+str(details[6])+"\t\t\t" +str(details[7])+"\n")
        bill.write("\n")
      bill.write("Grand Total:"+str(grand_total))
      bill.write("\n")
      
    else:
      bill.write("Kitta No.\t\t City\t\t Direction\t\t Aana\t\t Rent Duration\t\t Price per month\t\tFine/Discount\t\t Total amount")
      bill.write("\n")
      bill.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
      bill.write("\n")
      #iterate renturn_land_details
      for details in return_land_details:
        bill.write(str(details[0])+"\t\t\t" +details[1]+"\t"+details[2]+"\t\t"+str(details[3])+"\t\t\t"+str(details[4])+"\t\t" +str(details[5])+"\t\t\t\t"+str(details[6])+"\t\t\t" +str(details[7])+"\n")
        bill.write("\n")
      bill.write("Grand Total:"+str(grand_total)) 
      bill.write("\n")
   print_info(invoice_filename)
   
  
