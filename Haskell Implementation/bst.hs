data Tree a = Empty | Node a (Tree a) (Tree a) -- defining data type
    deriving(Read, Show)

--data Tree a = Empty | Leaf a | Node (Tree a) a (Tree a)  deriving Show
 


makeTree :: Ord a => [a] -> Tree a -- returns a tree

makeTree [] = Empty -- returns empty tree which is the base

makeTree (n : ns) = insert n (makeTree ns)


 
insert :: Ord a => a -> Tree a -> Tree a

insert a Empty = Node a Empty Empty -- base case inserted a becomes the root node and right and left trees are empty

insert a  (Node node tree1 tree2) -- recursive case for right and left trees

    | a < node = Node node (insert a tree1) tree2

    | otherwise = Node node tree1 (insert a tree2)


 


 

inorder :: Tree a -> [a]

inorder Empty = [] -- base case if empty

inorder (Node node tree1 tree2) = (inorder tree1) ++ [node] ++ (inorder tree2)


-- preorder traversal (root, left, right)

preorder :: Tree a -> [a]

preorder Empty = []

preorder (Node node tree1 tree2) = [node] ++ (preorder tree1) ++ (preorder tree2)

postOrder :: Tree a -> [a]

postOrder Empty = []

postOrder (Node node tree1 tree2) =  (postOrder tree1) ++ (postOrder tree2) ++ [node]


search :: (Ord a) => (Tree a) -> a -> Bool -- returns true or false if in bst

search Empty _ = False -- DOESNT WORK FOR NEGATIVE NUMBERS THO GOT TO ASK STACK OVERFLOW

search (Node node tree1 tree2) x

      | x == node = True

      | x < node = search tree1 x

      | x > node = search tree2 x