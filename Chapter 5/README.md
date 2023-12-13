 # Chapter 5

**1. Show that the terminal object is unique up to unique isomorphism.**

Given any two terminal objects `A` and `B`, by definition of a terminal object, both of them have one and only one morphism coming in to them from each object in the category.
Therefore, there is exactly one morphism from `A` to `B`, which we'll call `f`, and exactly one morphism from `B` to `A`, which we'll call `g`.
Since we are in a category the composition of those two  `g . f` must also be in the category. That composition must be a morphism from `A` to `A`. However due to the definition of the terminal object (only one morphism coming in from each object in the category) and the fact that as we are in a category, `A` must have an identity morphism `id_A`, it follows that that identity morphism `id_A` is the only morphism from `A` to `A` and thus the composition `g . f` must be equal to `id_A`. 
Since `g . f == id_A` it follows that `A` and `B` must be isomorphic.

Assuming there is a second isomorphism with `f' :: A -> B`, `g' :: B -> A` then it follows immediately from the definition of a terminal object that `f' == f` and `g' == g` because by definition a terminal object only has one morphism coming into it from each object, so there can only be one morphism from `A` to `B` and one morphism from `B` to `A`.

**2. What is a product of two objects in a poset? Hint: Use the universal construction.**

The universal construction for a product `C` of `A` and `B` tells us that there must be two morphisms `p :: C -> A` and `q :: C -> B` and that for any other candidate `C'` with morphisms `p' :: C'-> A` and `q' :: C' -> B` there must be a unique morphism `m :: C'-> C` that factorizes them. 
From the definition of a partial order we have `forall A B. A <= B and B <= A implies A == B`.

So assuming two objects `A` and `B` whose product we are looking for.
Any candidate `C` would have to have morphisms `p :: C -> A` and `q :: C -> B`, but since the only relation in the poset is the ordering both those morphisms represent `C <= A` and `C <= B`. For any other candidate `C'` there must be a unique morphism `m :: C'-> C` that factorizes them, but again since that morphism must represent the ordering it follows that `C' <= C` for any "worse" candidate `C'`.

Thus a product of two objects in a poset (if there is one) must fulfill: `C <= A`, `C <= B` and for all `C'` where `C' <= A` and `C' <= B` we have `C' <= C`. 

We can be even more specific if `A` and `B` are in relation to each other: In this case the product is the smaller of the two since it fulfills the pattern for the product: If `A <= B` then there are two morphisms `p :: A -> A == id_A` and `q :: A -> B` (the assumption of this case) and for each other object `C'` with `p' :: C' -> A` and `q' :: C' -> B` the morphism `p'` is the `m` we need to factorize since `p' == p . m == id_A . p'` and `q' == q . p'`.

If `A` and `B` are not in relation to each other then the product is the next smaller element that is in relation to both (if there is one).


**3. What is a coproduct of two objects in a poset?**

The universal construction for a coproduct `C` of `A` and `B` tells us that there must be two morphisms `p :: A -> C` and `q :: B -> C` and that for any other candidate `C'` with morphisms `p' :: A -> C'` and `q' :: B -> C'` there must be a unique morphism `m :: C-> C'` that factorizes them. 
From the definition of a partial order we have `forall A B. A <= B and B <= A implies A == B`.

Same as above, combining the universal construction with the fact that all morphisms represent the ordering relation we have `A <= C` and `B <= C` and for every other candidate `C'` we have `C <= C'`.

With a parallel argument to the one used above, if `A` and `B` are in relation to each other then the coproduct `C` is the larger of the two. If they are not in relation then the coproduct is the next larger object both are in relation to (if there is one)

**4. Implement the equivalent of Haskell `Either` as a generic type in your favorite language (other than Haskell).**
Tried this in Clojure, and this map is the best candidate I managed to come up with without reaching down to the Java level.
``` Clojure
(defn i [n] {:isLeft true :value n} )
(defn j [m] {:isLeft false :value m} )
```
To add type information to this i imagine we would have to define a generic wrapper class in Java and invoke its constructor with the respective type when writing the `:value` field of `i` and `j`. 

If we instead implemented the whole thing in Java we might build sth like this:
``` Java
public enum LeftOrRight { LEFT, RIGHT }

public class Either<A, B> {
  private LeftOrRight leftOrRight;
  private A left;
  private B right;
  
  public Either<A, B> injectLeft(A x){
    Either<A, B> either = new Either<A, B>();
    either.leftOrRight = LeftOrRight.LEFT;
  	either.left = x;
    return either;
  }
  public Either<A, B> injectRight(B x){
    Either<A, B> either = new Either<A, B>();
    either.leftOrRight = LeftOrRight.RIGHT;
  	either.right = x;
    return either;
  }
}
```


**5. Show that `Either` is a "better" coproduct than `int` equipped with two injections:**
``` C++
int i(int n) { return n; }

int j(bool b) { return b ? 0: 1; }
```

To show this we need a unique morphism `m :: Either Bool Int -> int` for which `i =  m . Left` and `j = m . Right`.
``` Haskell
m (Left x) = x
m (Right y) = if y then 1 else 0
```

We cannot prove the absence of other morphisms `m' Either Bool Int  -> int` that fulfill the same criteria here, so instead we prove that `int` cannot be the better coproduct of the two, in which case the better one must be `Either`.

**6. Continuing the previous problem: How would you argue that `int` with the two injections `i` and `j` cannot be "better" than `Either`.**

If `int` with the two injections given were the better coproduct then we would need a unique morphism `m :: int -> Either Bool Int` for which `Left = m . i` and `Right = m . j`. 
However, it is not clear how that function `m` should handle inputs `0` and `1` - an `m` where `m(0) = Right False` fulfills `Right = m . j` but not `Left = m . i` since `(m . i) (0) = Right False != Left 0`. An `m` where `m(0) = Left 0` fulfills `Left = m . i` but not `Right = m . j` since `(m . j) (0) = Left 0 != Right False`.

**7. Still continuing: What about these injections:**
``` C++
int i(int n) {
  if (n < 0) return n;
  return n + 2;
}

int j(bool b) { return b ? 0: 1; }
```

If `int` with the two injections given were the better coproduct then we would need a unique morphism `m :: int -> Either Bool Int` for which `Left = m . i` and `Right = m . j`. 

`m` would be 
``` Haskell
m 0 = Left False
m 1 = Left True
m x = Right (if x > 0 then x - 2 else x)
```

This representation is isomorphic to Either (?)

**8. Come up with an inferior candidate for a coproduct of `int` and `bool` that cannot be better than `Either` because it allows multiple acceptable morphisms from it to `Either`.**

For this we just need to duplicate some information like so: 

``` C++
pair<int, int> i(int n) {
  if (n < 0) return (n, n);
  int m = n + 2;
  return (m, m);
}

int j(bool b) { return b ? (0, 0): (1, 1); }
```

There are at least two possible morphisms from this to the candidate from 7.: one that always takes the first element of the Pair and one that always takes the second.
Since the representation from 7. is isomorphic to `Either` there is a morphism from it to either and due to the composition laws of a category this means there must be at least two morphisms from the candidate above to `Either` as well.