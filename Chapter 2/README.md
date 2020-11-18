# Chapter 2
**1. Define a higher-order function (or a function object) memoize in your favorite language. This function takes a pure function `f` as an argument and returns a function that behaves almost exactly like `f`, except that it only calls the original function once for every argument, stores the result internally, and subsequently returns this stored result every time it's called with the same argument. You can tell the memoized function from the original by watching its performance. For instance, try to memoize a function that takes a long time to evaluate. You'll have to wait for the result the first time you call it, but on subsequent calls, with the same argument, you should get the result immediately.**
* see `chapter2.py`

**2. Try to memoize a function from your standard library that you usually use to produce random numbers. Does it work?**
* see `chapter2.py`
* no, for two reasons:
  * the function i implemented expects exactly one argument and python `random()` gets no arguments
  * i changed the memoizer to accept functions without arguments, but it still does not work because i memoize the random number that is generated the first time `random()` is called and subsequently always return that number, but calling `random()` repeatedly yields different random numbers
  
**3. Most random number generators can be initialized with a seed. Implement a function that takes a seed, calls the random number generator with that seed, and returns the result. Memoize that function. Does it work?**
* see `chapter2.py`
* yes

**4. Which of these C++ functions are pure? Try to memoize them and observe what happens when you call them multiple times: memoized and not.**
    **(a) The factorial function from the example in the text.**
    * pure, see `chapter2.py`
    **(b) `std::getchar()`**
    * not pure (since it reads from stdin) (no example in python since this is a c++ specific function)
    **(c) `bool f() {
            std::cout << "Hello!" <<std::endl;
            return true;
          }`**
    * not pure since it has a side effect: writing to stdout (no example in python since this is a c++ specific function)
    **(d) `int f(int x) {
            static int y = 0;
            y += x;
            return y;
          }`**
    * not pure because it has state (in the form of the static variable y whose value is retained between calls & modified by each function call), see `chapter2.py`


**5. How many different functions are there from `Bool` to `Bool`? Can you implement them all?**
    * four: id, flip (negation), always true and always false,  for implementation see `chapter2.py`

**6. Draw a picture of a category whose only objects are the types `Void`, `()` (unit), and `Bool`; with arrows corresponding to all possible functions between these types. Label the arrows with the names of the functions.**
![](C.png)

