{-
lg[]=0
lg(x:xs) = 1 + lg xs

concat [] ls = ls
concat (x:xs) ls = x : concat (xs:ls)

renverse[] = []
renverse(x:xs) = concat(renverse xs) [x]


renv ls = loop ls [] where
	loop [] js = js
	loop(x:xs)ys = loop xs (x : ys)
	
	
T(n) = T(n-1) + O(1) -> T(n) est O(n)
T(n) = T(n-1) + O(n) -> T(n) est O(n^2)

tf[] =[]
tf ls = merge (tf gauche) (tf droite) where
	gauche = take (n/2) ls
	droite = drop (n/2) ls
	n = length ls
	
	
take 0 ls = []
take n [] = []
take (n + 1)(x:xs) = x : take n xs

drop 0 ls = ls
drop n [] = []
drop( n+1) (x:xs) = drop n xs


-- recoit 2 listes tries et les fusionne
merge [] ls = ls
merge ls [] = ls
merge (x:xs) (y:ys) = 
	| x < y = x : merge xs ( y:ys)
	| otherwise = y: merge (x:xs) ys

	
	 | (length(equal_list(x:xs))) > nr) = (True, x, length(equal_list(x:xs)))
--| (length(less_list(x:xs))) > (half_size (x:xs)) = 
-}

--tableau majoritaire

test ((xs), pivot) =  less ++ eq ++ more where 
 less = filter (<pivot) xs
 more = filter(>pivot) xs
 eq = filter(==pivot) xs
 
equal_list [] = []
equal_list (x:xs) = [x] ++ f where 
 f = filter (==x) xs  
 
less_list [] = []
less_list (x:xs) = f where 
 f = filter (<x) xs  
 
greater_list [] = []
greater_list (x:xs) = f where 
 f = filter (>x) xs  
 
half_size(xs) = length xs `div` 2 
  


maj_size([],nr )=(False, 0, 0)
maj_size((x:xs), nr)
 | (length(equal_list(x:xs)) > nr) = (True, x, length(equal_list(x:xs)))
 |(length(less_list(x:xs)) > nr) = maj_size(less_list(x:xs), nr)
 |(length(greater_list(x:xs)) > nr) = maj_size(greater_list(x:xs), nr)
 | otherwise = (False, -1, -1)
 
maj[]=(False, 0, 0)
maj(xs) = maj_size(xs, half_size(xs)) 