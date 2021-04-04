is_bst(nil). % verifies if the bst is empty

is_bst(bst(_, L, R)) :- % verifies if bst because of left and right nodes 
    is_bst(L),
    is_bst(R).



bstinsert(nil, V, bst(V, nil, nil)). % if right and left is empty then put as bst 

bstinsert(Tree, V, Tree) :- Tree = bst(V, _, _). % inserting 3 and a value into the bst and returning the new tree

bstinsert(bst(K, L, R), V, bst(K, Lnew, R)) :- % if inserted bst is less than the current bst then lower bst becomes root bst in tree . 
 V < K, bstinsert(L, V, Lnew). % Also caters for duplicates if there are any as bst have to have distinct values

bstinsert(bst(K, L, R), V, bst(K, L, Rnew)) :- % if its less than then value V goes into the left tree
 V > K, bstinsert(R, V, Rnew).



%searches to see if value is in tree returns true if it is false if it isnt 

search(bst(V,_,_),V). % if tree is empty then value is not in tree
search(bst(N,L,_),V):- V < N,!,search(L,V). % if value is less than root bst then it checks the right tree to see if values there
search(bst(_,_,R),V):- search(R,V). % if value still not found it checks left tree

inorder(bst(V,nil,nil),[V]).
inorder(bst(V,L,R), RES) :- inorder(L,LS), inorder(R,RS), append(LS,[V|RS], RES).
inorder(nil,[]).

preorder(nil, []). % base case if tree is empty
preorder(bst(V, L, R), [V|T]) :- preorder(L, LT), append(LT, RT, T), preorder(R, RT).


postorder(nil,[]).
postorder(bst(V,nil,nil),[V]).
postorder(bst(V,L,R),RES) :- postorder(L,LS), postorder(R,RS), append(RS,[V],RSS), append(LS,RSS,RES).         