


from tabulate import tabulate

Menu = 0 

headers = ["index","Inventory", "Colour", "Locations", "Stock", "New/Second"]


Menu_utama = """
>>>>>Welcome to Sukses Toys <<<<<  
Please select one of the menu below: 
1. Add a product 
2. Show products
3. Update existing products information
4. Erase products
5. Exit program """

Daftar = {1:{"Inventory" : "Ferari", "Colour":"Red", "Locations":"Jakarta", "Stock" : 50, "New/Second" :"New"},
          2: { "Inventory" : "BMW", "Colour":"Black", "Locations":"Jakarta", "Stock" : 10, "New/Second" :"Second"},
          3: { "Inventory" : "Toyota", "Colour":"Blue", "Locations":"Jakarta", "Stock" : 20, "New/Second" :"New"},
          4: { "Inventory" : "Honda", "Colour":"Yellow", "Locations":"Jakarta", "Stock" : 10, "New/Second" :"Second"},
          5: { "Inventory" : "Lambo", "Colour":"Purple", "Locations":"Jakarta", "Stock" : 40, "New/Second" :"New"}}
while Menu != 5: # jelasin
    print(Menu_utama)  

    try:
        Menu = int(input('Please input menu: ')) # jelasin


       
        if Menu == 1 : # jelasin
            Judul_1 = """ 
            
>>>>>Welcome to Sukses Toys <<<<<  
Please select one of the option
1. Add New Inventory
2. Back to first page"""

            Pilihan_1 = True
            while Pilihan_1  :
                print(Judul_1)  
                Menu_1 = int(input("Please select one of the option: " ))
                print("\n")
                if Menu_1 == 1:
                    Insert_Key = int(input("Please insert new index: "))
                    print("\n")
                    if Insert_Key in Daftar :
                        print("===== Product already included =====")
                    else :
                        Inventory = input("Please input Inventory :")
                        Colour = input("Please input the colour :")
                        Location= input("Please input the location :")
                        Stock = int(input("Please input the Stock :"))
                        New_or_second = input("New/Second :")

                        confirm = input("Do you want to save the data (Y/N): ").lower()

                        if confirm == "y":

                            Daftar[Insert_Key] = ({"Inventory" : Inventory, "Colour" : Colour, "Locations" : Location, "Stock" : Stock, "New/Second" : New_or_second})
                            print("\n")
                            print(">>>>> Data succesfully saved <<<<<")
                            
                        else :
                            print("\n")
                            print (">>>>> Data was not saved <<<<<")
                elif Menu_1 == 2 :
                    Pilihan_1 = False # jelasin
                else :
                    print("Please insert valid option")
        elif Menu == 2 :

            Pilihan_2 = True
            while Pilihan_2 :
            
                print("""
>>>>>Welcome to Sukses Toys <<<<<  
Please select one of the menu below: 
1. Show all of the datas
2. Show one of datas
3. Back to first page  """ ) # belum karena pakai while 
                
                Pilih_2 = int(input("Please select one of the menus: "))

                if Pilih_2 == 1 :
                    print("\n")
                    Table = []
                    for key, value in Daftar.items() :
                        Table.append([key,value["Inventory"], value["Colour"], value["Locations"], value["Stock"], value["New/Second"]])
                    print(tabulate(Table,headers=headers, tablefmt="fancy_grid"))
            
                    print("\n")       
                
                elif Pilih_2 == 2 :
                    
                    Selected_datas = int(input("Please select one of the datas: ")) ## masih error kalau masukkan huruf 

                    if Selected_datas in Daftar:

                        value = Daftar[Selected_datas]
                        
                        print("\n")
                        
                        Table_2 = [[Selected_datas,value["Inventory"], value["Colour"], value["Locations"], value["Stock"], value["New/Second"]]]
                        print(tabulate(Table_2,headers=headers, tablefmt="fancy_grid"))
                        print("\n")
                    else :
                        print("\n")
                        print(">>>>> Data not found <<<<<")

                elif Pilih_2 == 3 :
                    Pilihan_2 = False # jelasin

                else :
                    print("Please insert valid option")

        elif Menu == 3 :
            Pilihan_3 = True
            while Pilihan_3 :
                print("\n")
                print(
                    """
>>>>>Welcome to Sukses Toys <<<<<  
Please select one of the menu below: 
1. Update datas
2. Back to first page""" ) 
                
                Pilih_3 = int(input("Please select one of the menus:"))

                if Pilih_3 ==1 :
                    print('\n')
                    Pilih_3_1 = int(input("Insert the index numbers: "))  
                    
                    if Pilih_3_1 in Daftar :
                        print(">>>>> Selected Data <<<<<")
                        value = Daftar[Pilih_3_1]
                        Table_3 = [[Pilih_3_1,value["Inventory"], value["Colour"], value["Locations"], value["Stock"], value["New/Second"]]]
                        print(tabulate(Table_3,headers=headers, tablefmt="fancy_grid"))

                        print ("""
Please select data you want to update" 
    1. Inventory
    2. Colour
    3. Locations
    4. Stocks
    5. New/Second """)
                        Pilih_3_2 = int(input('Please select the colomns want to be updated (1-5): ')) # jelasin
                        
                        if Pilih_3_2 == 1:
                            Updated_inventory = input("Please insert updated toy's name: ")
                            confirm = input("Do you want to save the data (Y/N): ").lower() # jelasin

                            if confirm == "y":

                                Daftar[Pilih_3_1]["Inventory"] = Updated_inventory
                                print("\n")
                                print(">>>>> Data succesfully saved <<<<<")
                            else :
                                print("\n")
                                print (">>>>> Data was not saved <<<<<")
                                
                        elif Pilih_3_2 == 2:

                            Updated_Colour = input("Please insert toy's colour: ")
                            confirm = input("Do you want to save the data (Y/N): ").lower()
                            if confirm == "y" :

                                Daftar[Pilih_3_1]["Colour"] = Updated_Colour
                                print("\n")
                                print(">>>>> Data succesfully saved <<<<<")
                            else :
                                print("\n")
                                print (">>>>> Data was not saved <<<<<")

                        elif Pilih_3_2 == 3 :

                            Updated_Locations = input("Please insert toy's locations: ")
                            confirm = input("Do you want to save the data (Y/N): ").lower()

                            if confirm == "y" :
                    
                                Daftar[Pilih_3_1]["Locations"] = Updated_Locations
                                print("\n")
                                print(">>>>> Data succesfully saved <<<<<")
                            else :
                                print("\n")
                                print (">>>>> Data was not saved <<<<<")
                            
                        elif Pilih_3_2 == 4 :
                        
                            Updated_Stock = input("Please insert toy's stock: ")
                            confirm = input("Do you want to save the data (Y/N): ").lower()
                            if confirm == "y" :

                                Daftar[Pilih_3_1]["Stock"] = Updated_Stock
                                print("\n")
                                print(">>>>> Data succesfully saved <<<<<")
                            else :
                                print("\n")
                                print (">>>>> Data was not saved <<<<<")

                        elif Pilih_3_2 == 5 :
                            Updated_New_or_second = input("Please insert New or Second: ")
                            confirm = input("Do you want to save the data (Y/N): ").lower()
                            if confirm == "y" :
                                Daftar[Pilih_3_1-1]["New/Second"] = Updated_New_or_second
                            else :
                                print("\n")
                                print (">>>>> Data was not saved <<<<<")
                            
                    else : 
                        print(f">>>>> There is no product with index of {Pilih_3_1} <<<<<")
                
                elif Pilih_3 ==2 :
                    Pilihan_3 = False
               

        elif Menu == 4 :
            Pilihan_4 = True
            while Pilihan_4:

                print("""
>>>>>Welcome to Sukses Toys <<<<<  
Please select one of the menu below: 
    1. Erase data
    2. Back to first page""")
                
                Pilih_4 = int(input(" Please select of the menu (1/2): "))

                if Pilih_4 == 1 :

                    Data_Hapus = int(input("Please insert index of data you want to erase: "))
                    

                    if Data_Hapus in Daftar :

                        confirm = input("Do you want to delete the data (Y/N): ").lower()

                        if confirm == "y" :

                            Daftar.pop(Data_Hapus)
                            print("\n")
                            print(">>>>> Data has been deleted <<<<<")
                        else :
                            print("\n")
                            print (">>>>> Cancel <<<<<")   
                    
                    else : 
                        print(f">>>>> There is no product with index of {Data_Hapus} <<<<<")
                
                else:
                    Pilihan_4 = False

    except ValueError :
        
        print(">>>> Please input the right option <<<<<")
        continue
   

        
        