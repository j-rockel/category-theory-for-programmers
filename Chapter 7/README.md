# Chapter 7

**1. Can we turn the `Maybe` type constructor into a functor by defining `fmap _ _ = Nothing` which ignores both of its arguments?**

The functor laws are: Identity is Identity, Composition is composition. 
So let's check them for this implementation of `fmap`:

``` Haskell
fmap (f . g) == fmap f . fmap g

fmap (f . g) x 
 = -- {definition of fmap}
Nothing
 = -- {definition of fmap}
fmap f Nothing
 = -- {definition of fmap}
fmap f . fmap g $ x
```
This one was easy 

``` Haskell
fmap id = id

-- annotated the ids to make them easier to differentiate
-- case for Nothing
fmap (id :: a -> a) x  
 = -- {definition of fmap}
Nothing
 = -- {definition of id}
(id :: Maybe a -> Maybe a) Nothing

-- case for Just
fmap (id :: a -> a) x  
 = {definition of fmap}
Nothing
 != -- here we have a problem, that means this implementation does not preserve identity!
(id :: Maybe a -> Maybe a) (Just x)
```
Because the identity function for `Maybe` maps `Just` to `Just` and `fmap id` maps it to `Nothing`, this implementation of `fmap` is not a functor

**2. Prove functor laws for the reader functor.**
Reader functor: 
``` Haskell
instance Functor ((->) r) where 
  fmap :: (a -> b) -> (r -> a) -> (r -> b)
  fmap f g = f . g
```
Preserves Identity:
``` Haskell
fmap id = id
-- annotated the ids to make them easier to differentiate
(fmap (id :: a -> a) :: (r -> a) -> (r -> a)) = (id :: (r -> a) -> (r -> a)) 


fmap (id :: a -> a) (f :: (r -> a))
 = -- {definition of fmap}
(id :: a -> a) . f
 = -- {left identity law}
f 
 = -- {definition of id}
(id :: (r -> a) -> (r -> a)) f
```

Preserves Composition:
``` Haskell
fmap (f . g) == fmap f . fmap g

fmap (f . g) h
 = -- {definition of fmap}
(f . g) . h
 = -- {commutativity of composition}
f . (g . h)
 = -- {definition of fmap}
f . (fmap g h)
 = -- {definition of fmap}
fmap f (fmap g h) = fmap f . fmap g $ h
```

**3. Implement the reader functor in your second favorite language.**
``` Clojure
(defn fmap [f, g, x] (f (g x)))

; for example
(my-fmap (partial + 2) (partial + 3) 1)
;=> 6
```

**4. Prove the functor laws for the list functor. Assume the laws are true for the tail part of the list you're applying it to (use induction).**

List functor: 
``` Haskell
instance Functor [a] where 
  fmap :: (a -> b) -> [a] -> [b]
  fmap _ Nil = Nil
  fmap f (Cons x t) = Cons (f x) (fmap f t)
 ```
Preserves Identity:
``` Haskell
fmap id = id
-- annotated the ids to make them easier to differentiate
(fmap (id :: a -> a) :: [a] -> [a]) = (id :: [a] -> [a]) 

-- Case for Nil
fmap (id :: a -> a) Nil
 = -- {definition of fmap}
Nil
 = -- {definition of id}
(id :: [a] -> [a]) Nil

-- Case for Cons
-- Assumption A: fmap id tail = id tail
fmap (id :: a -> a) (Cons x t)
 = -- {definition of fmap}
Cons ((id :: a -> a) x) (fmap (id :: a -> a) tail)
 = -- {Assumption A}
Cons ((id :: a -> a) x) ((id :: [a] -> [a]) tail)
 = -- {definition of id (x2)}
Cons x tail
 = -- {definition of id }
(id :: [a] -> [a]) (Cons x tail)
```

Preserves Composition:
``` Haskell
fmap (f . g) == fmap f . fmap g

-- Case for Nil
fmap (f . g) Nil
 = -- {definition of fmap}
Nil
 = -- {definition of fmap}
fmap g Nil
 = -- {definition of fmap}
fmap f (fmap g Nil) = fmap f . fmap g $ Nil

-- Case for Cons
-- Assumption A: fmap (f . g) tail = fmap f (fmap g tail) ( = fmap f . fmap g $ tail)
fmap (f . g) (Cons x tail)
 = -- {definition of fmap}
Cons ((f . g) x) (fmap (f . g) tail)
 = -- {Assumption A}
Cons ((f . g) x) (fmap f (fmap g tail))
 = -- {composition syntax}
Cons (f (g x)) (fmap f (fmap g tail))
 = -- {definition of fmap}
fmap f (Cons (g x) (fmap g tail))
 = -- {definition of fmap}
fmap f (fmap g (Cons x tail)) = fmap f . fmap g $ Cons x tail
```
