package main // does not have remove functionality

import "fmt"

// phonebook1 which is binary search tree 1
type phonebook1 struct {

	Value string
	number int 
	address string
	left_child  * phonebook1
	right_child * phonebook1
}



// inserts node into tree
func (val *phonebook1) Insert(name string,number int , address string) { // reciever pointer thing i want to modify(like self in python)
	if val == nil {
		val = &phonebook1{Value: name, 
		number: number, 
		address : address}
		
	}
	if name == val.Value {
		fmt.Println("Contact already in phonebook")
		
		
	}
	if name < val.Value {
		if val.left_child == nil {
			val.left_child = &phonebook1{Value: name, // puts variables into memory location
										number:number, 
									    address: address}
		return
			
		}
		val.left_child.Insert(
			name,
			number,
			address)
	
	}
	if name > val.Value {
		if val.right_child == nil {
			val.right_child = &phonebook1{Value: name, 
										number:number,
										address:address}
			return
		}
		val.right_child.Insert(name,
							  number,
							  address)
	}
}



// finds name in tree
func (val * phonebook1) findname(name string) * phonebook1 {
	if val == nil {
		fmt.Println("Phone book is empty")
		return nil
	}
	if name == val.Value {
		fmt.Println("\n****** CONTACT FOUND ******\n","Name:",val.Value,"Number:", val.number,"\n-------------------------------")
		return val

	}
	if name < val.Value {
		if val.left_child == nil {
			fmt.Println("\n-------------------------\nContact not in phonebook\n-------------------------")
			return nil
		}
		return val.left_child.findname(name)
	}
	if val.right_child == nil {
		fmt.Println("\n-------------------------\nContact not in phonebook\n-------------------------")
		return nil
	}
	return val.right_child.findname(name)
}


//  prints tree in order traversal
func (t *phonebook1) printTree() {
	if t != nil {
		t.left_child.printTree()
		fmt.Println("Name:",t.Value,"\nNumber:",t.number,"\nAddress:",t.address,"\n")
		
	}
	if t != nil{
	t.right_child.printTree()
	}
}

// phonebook 2 which is basically binary search tree 2
type phonebook2 struct {

	Value string
	number int
	address string
	left_child  * phonebook2
	right_child * phonebook2
}



// inserts a node into the tree
func (val *phonebook2) Insert(name string,number int , address string) {
	if val == nil {
		val = &phonebook2{Value: name, 
		number: number, 
		address : address}
		
	}
	if number == val.number {
		fmt.Println("Contact already in phonebook")
		
		
	}
	if number < val.number {
		if val.left_child == nil {
			val.left_child = &phonebook2{Value: name, 
										number:number, 
									    address: address}
			return
			
		}
		val.left_child.Insert(
			name,
			number,
			address)
	
	}
	if number > val.number {
		if val.right_child == nil {
			val.right_child = &phonebook2{Value: name, 
										number:number,
										address:address}
			return
		}
		val.right_child.Insert(name,
							  number,
							  address)
	}
}




// ***************** delete function when not commented out returns stack overflow in the terminal and I tried my best to fix it but I could
// not resolve the issue, so I have left it below to show that I've attempted it.

//func (val2 *phonebook2) remove_num(num int) * phonebook2{
	//if val2 == nil{
		//fmt.Println("Phonebook is Empty")
	
	//}
	//if num < val2.number{
		//val2.left_child = val2.remove_num(num)
		
	//}else if num > val2.number{
            //val2.right_child = val2.remove_num(num)
    //}else{// # reach to the node that need to delete from BST.
      //      if val2.left_child == nil && val2.right_child == nil{
                //return nil
        //    }

          //  if val2.left_child == nil {
                //temp = val2.right_child
            //    val2 = val2.right_child
            //}else if val2.right_child == nil {
                //temp = val2.left_child
                //del current
                //return temp
              //  val2 = val2.left_child
            // }else{temp := val2.val_delete(val2.right_child) 
      
           
              //  val2.number = temp.number
      
        
                //val2.right_child = val2.remove_num(num)
           // }
           //}
	//return val2
	//}

//func (val2 * phonebook2) val_delete(node*phonebook2) * phonebook2{
	//for {
      //  if val2.left_child != nil {
            //node = val2.right_child
    //    } else {
           // break
  //      }
    //}
    //return node

//}


// finds number in tree
func (val2 * phonebook2) findnumber(num int) * phonebook2 {
	if val2 == nil {
		fmt.Println("Phone book is empty")
		return nil
	}
	if num == val2.number {
		fmt.Println("\n****** CONTACT FOUND ******\n","Name:",val2.Value,"Number:", val2.number,"\n-------------------------------")
		return val2

	}
	if num < val2.number {
		if val2.left_child == nil {
			fmt.Println("\n---------------------\nContact not in phonebook\n---------------------")
			return nil
		}
		return val2.left_child.findnumber(num)
	}
	if val2.right_child == nil {
		fmt.Println("\n-------------------------\nContact not in phonebook\n-------------------------")
		return nil
	}
	return val2.right_child.findnumber(num)
}



//  prints tree in traversal order
func (t *phonebook2) printTree() {
	if t != nil {
		t.left_child.printTree()
		fmt.Println("Name:",t.Value,"\nNumber:",t.number,"\nAddress:",t.address,"\n")
		
	}
	if t != nil{
	t.right_child.printTree()
	}
}



func main() {

	// main function has all my data

	phonebook_name := &phonebook1{Value: "Chloe",number: 3438789076, address: "Laois"} // inserting first node
	phonebook_name.Insert("Ethan",1111111111,"Donegal")
	phonebook_name.Insert("James",6667654789,"DCU")
	phonebook_name.Insert("Ariana",5876875675,"London")
	phonebook_name.Insert("Shane",33387433654,"Kildare")
	phonebook_name.Insert("Dawson",6565765345,"Scotland")
	phonebook_name.Insert("Joey",4957654376,"Kerry")
	phonebook_name.Insert("Harry Styles",1212786598,"Waterford")
	phonebook_name.Insert("Cillian",4876807529,"Wexford")
	
	fmt.Println("\nPhonebook ordered in alphabethical order.\n")
	phonebook_name.printTree()
	phonebook_name.findname("Ariana") // print found message
	phonebook_name.findname("Cillian") // print found message
	phonebook_name.findname("JLO") // not in phonebook prints error message



	phonebook_number := &phonebook2{Value: "Chloe",number: 3438789076, address: "Laois"} // inserting first node


	phonebook_number.Insert("Ethan",1111111111,"Donegal")
	phonebook_number.Insert("James",6667654789,"DCU")
	phonebook_number.Insert("Ariana",5876875675,"London")
	phonebook_number.Insert("Shane",33387433654,"Kildare")
	phonebook_number.Insert("Dawson",6568576534,"Scotland")
	phonebook_number.Insert("Joey",4957654376,"Kerry")
	phonebook_number.Insert("Harry Styles",1212786598,"Waterford")
	phonebook_number.Insert("Cillian",4876807529,"Wexford")


	fmt.Println("\nPhonebook ordered in numerical order.\n") //smallest number first
	phonebook_number.printTree()

	phonebook_number.findnumber(1111111111) // print contact found which will be Ethan
	phonebook_number.findnumber(1212786598) // print contact found which will be Harry Styles
	phonebook_number.findnumber(999999999999999) // prints that contact cant be found because not in phonebook
	//phonebook_number.remove_num(33387433654) // remove function kept coming up stack overflow so I have commented out.

}
