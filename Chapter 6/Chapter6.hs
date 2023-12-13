module Chapter6 where

-- Exercise 4.

data Shape
  = Circle Float
  | Rect Float Float
  | Square Float

area :: Shape -> Float
area (Circle r) = pi * r * r
area (Rect d h) = d * h
area (Square e) = e * e

circ :: Shape -> Float
circ (Circle r) = 2.0 * pi * r
circ (Rect d h) = 2.0 * (d + h)
circ (Square e) = 2.0 * (e + e)