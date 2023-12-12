# Chapter 3
**1. Generate a free category from:**

**(a) A graph with one node and no edges**
The free category for a graph with one node and no edges is the category with only one object and its identity morphism.

**(b) A graph with one node and one (directed) edge (hint: this edge can be composed with itself)**
For the graph with one node `X` and one edge `f` the edge `f` must start and end at the only node `X`. The free category for a graph with one node and one edge is the category with only one object `X`, its identity morphism `id_X`, and the morphism `f` representing the single edge `f` from the graph. This morphism can then be concatenated with itself infinitely many times, resulting in one morphism for each natural number `n` representing the morphism `f` concatenated with itself `n` times.

**(c) A graph with two nodes and a single arrow between them**
For a graph with nodes X and Y and a single arrow f between them the free category contains: Two Objects X and Y, their identity morphisms `id_X` and `id_Y`, the morphism f. 

Question: do we include any concatenations here or are concatenations involving identity functions only implicitly part of the category?

**(d) A graph with a single node and 26 arrows with the letters of the alphabet: a, b, c ... z.**
For a graph with a single node `X` and 26 arrows with the letters of the alphabet, all arrows must start and end at `X`. Therefore they can be arbitrarily concatenated. The resulting free category has one object `X`, its identity morphism `id_X` (which also corresponds to the empty string) and morphisms for each letter and all possible concatenations of letters (one morphism for every possible string consisting of only the lowercase letters of the alphabet)

**2. What kind of order is this?**

**(a) A set of sets with the inclusion relation: *A* is included in *B* if every element of *A* is also an element of *B*.**
This is very similar to the example in the chapter of the smaller or equal relation. We have identity (`A` is included in `A`) and composition (if every element of `A` is an element of `B` and every element of `B` is an element of `C` then every element of `A` is an element of `C`) so it is a preorder. It is also the case that if every element of `A` is an element of `B` and every element of `B` is an element of `A` then `A` and `B` are the same, so it is also a partial order. Although we can inspect every pair of sets, not all pairs are connected by the inclusion relation - for example, the sets {X} and {Y} have no inclusion relation between them since neither contains all the elements of the other. Therefore this is not a total order.

**(b) C++ types with the following subtyping relation: `T1` is a subtype of `T2` if a pointer to `T1` can be passed to a function that expects a pointer to `T2` without triggering a compilation error.**
Caveat: I know nothing about C++ so I may be missing some nuance here. 
Identity: Yes. If a function expects a pointer to `T1` and gets a pointer to `T1` it is being used as intended.
Composition: Yes. If I can use `T1` wherever I can use `T2` and `T2` wherever I can use `T3` then I should be able to use `T1` wherever I can use `T3`.
-> It's a preorder.
After this it gets tricky. I don't think being able to use `T1` where a `T2` is expected and being able to use a `T2` where a `T1` is expected means they must be the same type - I imagine some numerical types in C++ can be used interchangeably - meaning it would not be a partial order, but I don't know enough about C++ to know this for sure. 
I can say for sure though that not all types have this kind of relation in either direction - you can neither use a class where a string is expected nor a string where a class is expected, so even if it were a partial order it would not be a total order.

**3. Considering that `Bool` is a set of two values `True` and `False`, show that it forms two (set-theoretical) monoids with respect to, respectively, operator `&&` (AND) and `||` (OR).**
First Monoid: Bool + `&&`: 
Associativity: `A && (B && C) == (A && B) && C` holds: both sides evaluate to `True` iff `A, B, C` are all `True`, else both sides evaluate to `False`.
Neutral element: `True` is the neutral element wrt. `&&` since `A && True == True && A == A`.
Second Monoid: Bool + `||`: 
Associativity: `A || (B || C) == (A || B) || C` holds: both sides evaluate to `False` iff `A, B, C` are all `False`, else both sides evaluate to `True`.
Neutral element: `False` is the neutral element wrt. `||` since `A || False == False || A == A`. 

**4. Represent the `Bool` monoid with the AND operator as a category: List the morphisms and their rules of composition.**
Objects: `Bool`
Morphisms: `id_Bool` == `(&&True)`, `(&& False)`
Rules of composition: 
`(&& True) . f == f . (&& True) == f` (this is just identity)
and
`(&& False) . f == f . (&& False) == (&& False)` (this is an additional rule)

**5. Represent addition modulo 3 as a monoid category.**
Objects: `{0,1,2}`
Morphisms: 
Representing all natural numbers `n` where `n mod 3 = 1` we have `(+n mod 3 = 1)`
Representing all natural numbers `n` where `n mod 3 = 2` we have `(+n mod 3 = 2)`
Representing all natural numbers `n` where `n mod 3 = 0` we have `(+n mod 3 = 0)` == `id_{0,1,2}`
Composition: 
`forall x,y in {0,1,2}. ((x + y) mod 3 = z) -> (+n mod 3 = x) . (+n mod 3 = y) == (+n mod 3 = z)`