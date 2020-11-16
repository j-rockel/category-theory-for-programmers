# Chapter 1

**1. Implement, as best as you can, the identity function in your favorite language (or the second favorite, if your favorite happens to be Haskell).**
* see `chapter1.py`


**2. Implement the composition function in your favorite language. It takes two functions as arguments and returns a function that is their composition.**
* see `chapter1.py`


**3. Write a program that tries to test that your composition function respects identity.**
* see `chapter1.py`


**4. Is the world-wide web a category in any sense? Are links morphisms?**
* not every page links to itself
* page A linking to page B and B linking to C doesn't mean A links to C 
* so no, not with links as morphisms


**5. Is Facebook a category, with people as objects and friendships as morphisms?**
* again no
* there is no identity morphism (what would that look like? being facebook friends with yourself?)
* even if there was, a friend of a friend is not necessarily a friend of mine


**6. When is a directed graph a category?**
* when its edge relation is reflexive and transitive