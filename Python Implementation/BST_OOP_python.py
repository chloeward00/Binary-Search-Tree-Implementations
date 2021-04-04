class Node: # will be used in both BST

    def __init__(self, name , number, address):
        self.name = name
        self.number = number
        self.address = address
        self.left_child = None
        self.right_child = None

class Binary_search_tree_Names:

    
    def insert(self, current,name,number,address):

        if current ==  None:
            return Node(name,number,address)
        
        # if data is smaller than parent , insert it into left side
        if name < current.name:

            current.left_child = self.insert(current.left_child, name,number,address)

        elif name > current.name:

            current.right_child = self.insert(current.right_child, name,number,address)

        return current


    def print_tree(self, current): # FUNCTION WILL PRINT TREE

        if current !=None:

            self.print_tree(current.left_child)

            print("Name: " + current.name + "\nNumber: " + str(current.number) + "\nAddress: " + current.address +"\n")

        if current != None:

            self.print_tree(current.right_child)

    def find_name(self, current,name): # FUNCTION WILL FIND NAME USER INPUTS

        if current == None:
            print (name + " does not exist in phonebook.\n")
        elif current.name == name:
            print ("****CONTACT FOUND *****\nName: " + current.name + "\nNumber: " + str(current.number)+"\n---------------------------\n")
        elif current.name < name:
            return self.find_name(current.right_child, name) #recursion
        else:
            return self.find_name(current.left_child, name) # recursion



    def val_delete(self,node): 
        current = node 
  
    # loop down to find the leftmost leaf 
        while(current.left_child != None): 
            current = current.left_child  
  
        return current  

    def remove(self,current,name):

        if current == None:
            return None

        # searching key into BST.
        if name < current.name:
            current.left_child = self.remove(current.left_child, name)
        elif name > current.name:
            current.right_child = self.remove(current.right_child, name)
        else: # reach to the node that need to delete from BST.
            if current.left_child == None and current.right_child == None:
                return None
            if current.left_child == None:
                temp = current.right_child
                del current
                return  temp
            elif current.right_child == None:
                temp = current.left_child
                del current
                return temp
            else:
                temp = self.val_delete(current.right_child) 
      
            # Copy the inorder successor's content to this node 
                current.name = temp.name 
      
            # Delete the inorder successor 
                current.right_child = self.remove(current.right_child , temp.name) 


        return current


class Binary_search_tree_numbers:
    
    def insert(self, current,name,number,address):

        if current ==  None:
            return Node(name,number,address)
        # if data is smaller than parent , insert it into left side
        if number < current.number:
            current.left_child = self.insert(current.left_child, name,number,address)
        elif number > current.number:
            current.right_child = self.insert(current.right_child, name,number,address)

        return current


    def print_tree(self, current): # FUNCTION WILL PRINT TREE

        if current !=None:

            self.print_tree(current.left_child)
            print("Name: " + current.name + "\nNumber: " + str(current.number) + "\nAddress: " + current.address +"\n")

        if current != None:

            self.print_tree(current.right_child)

    def find_number(self, current,number): # FUNCTION WILL FIND NAME USER INPUTS

        if number == int(number):
                #print("Number must be int and not string")

            if current == None:

                print(str(number) + " does not exist in phonebook.")


            elif int(current.number) == int(number):
                print ("****CONTACT FOUND *****\nName: " + current.name + "\nAddress: " + str(current.address)+"\n--------------------------\n")

            elif int(current.number) < int(number):
                return self.find_number(current.right_child, number) #recursion
            else:
                return self.find_number(current.left_child, number) # recursion
        else:
            print("number must be int and not string")


    def val_delete(self,node): 
        current = node 
  
    # loop down to find the leftmost leaf 
        while(current.left_child != None): 
            current = current.left_child  
  
        return current  

    def remove2(self,current,number):

        if current == None:
            return None

        # searching key into BST.
        if number < current.number:
            current.left_child = self.remove2(current.left_child, number)
        elif number > current.number:
            current.right_child = self.remove2(current.right_child, number)
        else: # reach to the node that need to delete from BST.
            if current.left_child == None and current.right_child == None:
                return None
            if current.left_child == None:
                temp = current.right_child
                del current
                return  temp
            elif current.right_child == None:
                temp = current.left_child
                del current
                return temp
            else:
                temp = self.val_delete(current.right_child) 
      
            # Copy the inorder successor's content to this nodes 
                current.number = temp.number
      
            # Delete the inorder successor 
                current.right_child = self.remove2(current.right_child , temp.number) 


        return current


def main():


    print("--------------------------------\nPhonebook in alphabethical order\n--------------------------------")
    phonebook_names = Binary_search_tree_Names()
    root = None
    root = phonebook_names.insert(root,"Ethan",1238765890,"DUBLIN")
    phonebook_names.insert(root,"Chloe",1110987654, "GALWAY")
    phonebook_names.insert(root,"Dwayne",8486547654,"BOSTON")
    phonebook_names.insert(root,"Harry",9880967654,"DCU")
    phonebook_names.insert(root,"Connor",9923564312, "UK")
    phonebook_names.insert(root,"Niall Horan",4445677897,"Ireland")
    phonebook_names.insert(root,"Ariana Grande",8756732111,"Ireland")
    phonebook_names.insert(root,"Khloe",2222222243, "GALWAY")
    phonebook_names.insert(root,"Darren",9875645678,"BOSTON")
    phonebook_names.insert(root,"Zeke",9999999999, "UK")
    phonebook_names.insert(root,"Kian",1118795786,"Ireland")
    phonebook_names.insert(root,"Lola",1113454325,"Ireland")
    phonebook_names.print_tree(root)
 
    phonebook_names.find_name(root,"Kian") # names of people in phonebook so should return true
    phonebook_names.find_name(root,"Chloe") # names of people in phone book so should return true
    phonebook_names.find_name(root,"Justin Bieber") # so it prints that Justin Bieber does not exist in phonebook
    phonebook_names.remove(root,"Ethan") # removing Ethan
    phonebook_names.find_name(root,"Ethan") # verifying that Ethan no longer exists in phone book


    print("-----------------------------\nPhonebook in numerical order\n-----------------------------")
    phonebook_numbers = Binary_search_tree_numbers()
    root2 = None
    root2 = phonebook_numbers.insert(root2,"Ethan",1238765890,"DUBLIN")
    phonebook_numbers.insert(root2,"Chloe",1110987654, "GALWAY")
    phonebook_numbers.insert(root2,"Dwayne",8486547654,"BOSTON")
    phonebook_numbers.insert(root2,"Harry",9880967654,"DCU")
    phonebook_numbers.insert(root2,"Connor",9923564312, "UK")
    phonebook_numbers.insert(root2,"Niall Horan",4445677897,"Ireland")
    phonebook_numbers.insert(root2,"Ariana Grande",8756732111,"Ireland")
    phonebook_numbers.insert(root2,"Khloe",2222222243, "GALWAY")
    phonebook_numbers.insert(root2,"Darren",9875645678,"BOSTON")
    phonebook_numbers.insert(root2,"Zeke",9999999999, "UK")
    phonebook_numbers.insert(root2,"Kian",1118795786,"Ireland")
    phonebook_numbers.insert(root2,"Lola",8888888888,"Ireland")
    phonebook_numbers.print_tree(root2)

    phonebook_numbers.find_number(root2,4445677897) # finding contact
    phonebook_numbers.find_number(root2,1110987654) # finding contact
    phonebook_numbers.remove2(root2,8888888888) # removing contact
    phonebook_numbers.find_number(root2,"8888888888") # put in as a string so an error message will come up in terminal as it has to be an int
    phonebook_numbers.find_number(root2,8888888888) # verifying that it no longer exists in phonebook




if __name__ == "__main__":
    main()
