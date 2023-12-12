# Chapter 4

Caveat for this chapter: I don't know C++ so interpret this as C++-style pseudocode.

**1. Construct the Kleisli category for partial functions (define composition and identity).**
Composition: 
``` C++
auto const compose = [](auto m1, auto m2) {
  return [m1, m2] (auto x) {
    auto opt1 = m1(x);
    if opt1.isValid() return m2(opt1.value());
      else return opt1;
  }
}
```
Identity:
``` C++
template <class A> optional<A> identity(A x) {
  return optional<A> {x};
}
```

**2. Implement the embellished function `safe_reciprocal` that returns a valid reciprocal of its argument, if it's different from zero.**
``` C++
optional<double> safe_reciprocal(double x) {
  if (x != 0) return optional<double>{ 1 / x }; 
  else return optional<double>{};
}
```

**3. Compose the functions `safe_root` and `safe_reciprocal` to implement `safe_root_reciprocal` that calculates `sqrt(1/x)` whenever possible.**
``` C++
optional<double> safe_root_reciprocal(double x) {
  return compose (safe_reciprocal, safe_root) (x);
}
```
