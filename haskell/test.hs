{-
:cd D:\haskell
:load test.hs
:reload
lg ([2,6,1])
qs([2, -1, 7, 5])

lg ls = f ls 0 where
    f[] n = n
    f(x:xs) = f xs (n+1)
qs[] = []
qs(x:xs)=qs petits ++ [x] ++ qs grands where
    petits  = filter (<x) xs
    grands = filter ( >=x) xs

filter p[] = []
filter p(a:as)
    | p a = a : filter p as
    |otherwise = filter p as

-}

lg[] = 0
lg (x:xs) = 1 + lg xs

qs [] = []
qs (x:xs) = qs petits ++ [x] ++ qs grands where
 petits = filter (<x) xs
 grands = filter(>=x) xs
 
equal_list [] = []
equal_list (x:xs) = f where 
 f = filter (==x) xs 
 
 
--frequence [] n  = 0
frequence(x:xs,n)  = lg(filter (==n) xs)


