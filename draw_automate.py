from graphviz import Digraph
    

dot = Digraph(comment='YOUR AUTOMATE')  #creating the directed graph
nbr_nodes = int(input("Enter the number of nodes you want to add : "))
elements = []   #declare a list
       

def Make_nodes():
    
    i = 0
    while i < nbr_nodes:
            elt = input(f"Enter the element {i} of your automate : ")   #gathering the elements the user wants to make
            elements.insert(i,elt)
            a = str(i)   #type cast
            
            print("Is it initial or final : ")    
            final_initial = "z"
            while (final_initial != "y" and final_initial != "n"):
                  final_initial = input("(y/n) : ").lower()

            if final_initial == "y":
                dot.node(a, elt ,shape = "doublecircle")    #creating a node in doublecircle shape if yes

            else :
                dot.node(a, elt ,shape = "circle")  #creating a node in circle shape if no
 
	
            i=i+1
    
   
    print(f"The list of the elements you listed is {elements}")

    print(dot.source)
    


# A function that matches nodes

def Match_nodes():
    
    
    print("Enter the nodes to match : \nRespond by giving the elements you listed in your list!")

    i = 0 
    while i < nbr_nodes : 

        node_1 = input("The first node is :  ")
        node_2 = input("The second node is :  ")
        

        #Exemple :
        #dot.node('A', '1')
        #dot.node('B', '2')
        #dot.edges(['AB', 'AL'])
        #dot.edges(['AB', 'AL'])

        #dot.edge('B', 'L', constraint='false')
        transition = input("Enter the transition: ")  
        
        dot.edge(node_1 , node_2 , constraint = 'false' , label = transition )
        
        print(dot.source)   
        i=i+1
 

def Add_node():
    response = input("Do you want to add other nodes (y/n) : ").lower()
    while(response != "y" and response != "n"):
        response = input("The only answers accepted (y/n) :").lower()

    if response == "n":
        print("Thank you for using this program !")
    else :
        nbr_nodes_ = int(input("How many nodes you want to add : "))
        i = 0
        while i < nbr_nodes_:
                elt = input(f"Enter the element {i + nbr_nodes} of your automate :  ")
                elements.insert(i + nbr_nodes,elt)
                a = str(i + nbr_nodes_) #type casting
                
                print("Is it initial or final : ")
                final_initial = "z"
                while (final_initial != "y" and final_initial != "n"):
                    final_initial = input("(y/n) : ")

                if final_initial == "y":
                    dot.node(a, elt ,shape = "doublecircle")

                else :
                    dot.node(a, elt ,shape = "circle")
    
        

                i=i+1
        
    
        print(f"The list of the elements you listed is {elements}")

        print(dot.source)
        Match_nodes()

def main():
    Make_nodes()
    Match_nodes()
    Add_node()

if __name__ == "__main__":
    main()

