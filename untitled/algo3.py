'''
T[0)=a
T(n) = T(n-1) + b
T(n) = b*n +a

haskell
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

haskel home : C:\Users\petitChat\AppData\Roaming\local\bin

cd D:\haskell
load test.hs
'''