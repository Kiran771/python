import datetime
import write
import read

#function to rent the land
def rent_land(grand_total=0):
    """
    takes one parameter grand_total which is initialized and its default value is set as zero
    return none
    """
    # Call a function to read land information from a file
    land_info=read.read_land_info() 
     # List to store rental details
    rent_land_details=[] 
    #ask for customer_name
    customer_name=input("Please enter your name:")
    #check if customer_name is alphabetic character or not
    if not customer_name.isalpha():
        print("Please provide a valid name(Only alphabetic characters)")
        customer_name=input("Please enter your name:")
    #initialize found as False
    found=False
    #initialize loop as True
    loop=True
    while loop==True:
        try:
            #ask to provide kitta_number
            kitta_number=int(input("Please provide the kitta number of the land you want to rent:"))
            if kitta_number<0:
                print("Please enter a non negative kitta number.")
            else:
                # Set found to False
                found=False 
            #iterate land_info
            for key,details in land_info.items():
                #check if key and kitta_number matches or not
                if key==kitta_number: 
                    found=True
                    #check if the land with provided kitta number is available or not
                    if land_info[kitta_number][4].strip()=="Available":
                        print("The land is available")
                        datetime_invoice=datetime.datetime.now()
                        while True:
                            try:
                                #ask for user to enter rent duration month
                                rent_duration=int(input("Please provide number of months you want to rent a land: "))
                                if rent_duration<=0:
                                    print("Plese provide a valid month.")
                                else:
                                    break
                            except ValueError:
                                print("Please enter a valid integer.")
                        print("Thank you for renting the land.")
                        #calcualtion rent price
                        rent_price=rent_duration*int(details[3])
                        grand_total+=rent_price
                        #call function header in write file
                        write.header(customer_name,datetime_invoice)
                        #call function write_land_text in write file
                        write.write_land_text(kitta_number)
                        #append rent_land_details list to list cointaining details of rented land
                        rent_land_details.append([key,details[0],details[1],details[2],rent_duration,details[3],rent_price,grand_total])
                        print(rent_land_details)
                        #call function create_invoice_rentland in write file
                        write.create_invoice_rentland(rent_land_details,customer_name,datetime_invoice,grand_total)
                        # Update the land availability status
                        land_info[key][4] = "Not Available"
                            
                    else:
                        print("Sorry the land is not available") 
             
            if not found:
                print("Kitta number does not exist.") 
            #ask to choose option   
            rent_more = input("Do you want to rent more ? (y/n)")
            if rent_more !="y":
                break                        
        except ValueError:
            print("Please provide valid kitta number.")
        
#function to return land
def return_land(grand_total=0):
    """
    takes one parameter grand_total which is initialized and its default value is set as zero
    return none
    """
    fine_none = None 
    land_info=read.read_land_info()
     # List to store return land details
    return_land_details=[]
    #ask for customer_name
    customer_name=input("Please provide your name:")
    #check if customer_name is alphabetic character or not
    if not customer_name.isalpha():
        print("Please provide a valid name(Only alphabetic characters)")
        customer_name=input("Please enter your name:")
    #initialize found as False
    found=False
    loop=True
    while loop==True:
        try:
            #ask user to enter the kitta number of the land they want to rent
            kitta_number=int(input("Please provide the kitta number of the land that you have rented:"))
            if kitta_number<0:
                print("Please enter a non negative kitta number.")
            else:
                # Set found to False
                found=False
            #iterate land_info
            for key,details in land_info.items():
                #check if key and kitta_number matches or not
                if key==kitta_number: 
                    found=True
                    #checks if land with provided kitta number is not available or not
                    if land_info[kitta_number][4].strip()=="Not Available":
                        while True:
                            try:
                                #ask for user to enter the month for which they have rented the land
                                rent_duration=int(input("How many months have you rented the land for?"))
                                if rent_duration<=0:
                                    print("Plese provide a valid month.")
                                else:
                                    break
                            except ValueError:
                                print("Please provide valid integer.")
                        while True:
                            try:
                                #ask for return duration of land
                                return_duration=int(input("After how many month did you return the land?"))
                                if return_duration<=0:
                                    print("Please provide a valid month.")
                                else:
                                    break
                            except ValueError:
                                print("Please enter a valid integer.")
                        print("Thank you for returning the land")
                        datetime_invoice=datetime.datetime.now()
                        rent_amount=int(land_info[kitta_number][3])
                        #check if return duration is greater than rent duration if true then add fine
                        if return_duration>rent_duration:
                            payment_change=(return_duration-rent_duration)*rent_amount
                            amount=rent_duration*(rent_amount)+payment_change
                            fine_none = "fine"   
                        else:
                            payment_change=0
                            amount=rent_duration*rent_amount
                            
                        grand_total+=amount
                        #call function header in write file
                        write.header(customer_name,datetime_invoice)
                        #append rent_land_details list to list cointaining details of rented land
                        return_land_details.append([key,details[0],details[1],details[2],rent_duration,details[3],payment_change,amount])
                        print(return_land_details)
                        #call create_invoice_returnland in write file
                        write.create_invoice_returnland(return_land_details,customer_name,datetime_invoice,fine_none,grand_total) 
                        #call function write_land_text in write file
                        write.write_land_text(kitta_number)
                        # Update the land availability status
                        land_info[key][4] ="Available"
                    else:
                        print("The land is not rented")  
                        
            #if land is not found print the provided statement
            if not found:
                print("Kitta number does not exist.")  
            #ask to choose a option 
            return_more = input("Do you want to return more ? (y/n)")
            if return_more != "y":
                break         
        except ValueError:
            print("Plese provide a valid kitta number")
   
#function to display the details of the land   
def details_display():
    print("Press 1 to rent")
    print("Press 2 to return")
    print("Press 3 to exit")
    print("-"*198)
    print("Kitta"+"\t  City"+"\t\tDirection"+"\tAnna"+"\t Price"+"\t\tAvaiability")
    print("-"*198)
    print("\n")
    land_info=read.read_land_info()
    #iterate land_info
    for key,value in land_info.items():
        print(str(key)+"\t"+str(value[0])+"\t"+str(value[1])+"\t"+str(value[2])+"\t"+str(value[3])+"\t\t"+str(value[4]))
        print("\n")
    print("-"*198)                    
#function for rental system
def rental_system():  
    #set loop as True
    loop=True
    while loop==True:
        details_display()
        #ask for user input
        user_input=input("Please choose a option to continue:")#ask for user input 
        
        if user_input=="1":
            print("Provide your name for invoice generation.")
            #call rent_land function
            rent_land()    
        elif user_input=="2":
            print("Provide your name for invoice generation.")
            #call return_land function
            return_land()                      
        elif user_input=="3":
             print("Thanks for using our service.")
             #exit the loop
             break
        else:
             print("Please choose a valid option")

             





