# Chapter 6

**1. Show the isomorphism between `Maybe a` and `Either () a`**

We can show this by defining the two mapping functions that are inverses of each other: 

``` Haskell
maybeToEitherUnit :: Maybe a -> Either () a
maybeToEitherUnit Nothing = Left ()
maybeToEitherUnit (Just x) = Right x

eitherUnitToMaybe :: Either () a -> Maybe a
eitherUnitToMaybe (Left ()) = Nothing
eitherUnitToMaybe (Right x) = Just x
```

**2. Here's a sum type defined in Haskell:**
``` Haskell
data Shape = Circle Float | Rect Float Float
```
**Implement Shape in C++ or Java as an interface and create two classes: `Circle` and `Rect`. Implement `area` as a virtual function.**

--> see Chapter6.java

**3. Add `circ` to your C++ or Java implementation. What parts of the original code did you have to touch?**

--> see Chapter6.java for Implementation

Had to touch all of it - the function declaration needs to be added to the interface and its implementation needs to be added to each implementing class.


**4. Add a new shape, `Square`, to `Shape` and make all the necessary updates. What code did you have to touch in Haskell vs. C++ or Java?**

--> see Chapter6.java and Chapter6.hs for Implementation

In Java, neither the interface nor the other implementing classes need to be touched to add a new implementing class. In Haskell everything needs to be touched when we add a new constructor - we need to add it to the type definition and add a case for it to each existing function taking that type as an argument.

**5. Show that `a + a = 2 * a` holds for types (up to isomorphism). Remember that 2 corresponds to `Bool`, according to our translation table.**

The canonical corresponding types for each side of our equation are: 

`a + a` corresponds to `Either a a`

`2 * a` corresponds to `(Bool, a)`

To show that the equation holds up to isomorphism we show that these two types are isomorphic by defining their two mapping functions which are inverses of each other:

``` Haskell
eitherToBoolPair :: Either a a -> (Bool, a)
eitherToBoolPair (Left x) = (False, x)
eitherToBoolPair (Right x) = (True, x)

boolPairToEither :: (Bool, a) -> Either a a
boolPairToEither (False, x) = Left x
boolPairToEither (True, x) = Right x
```