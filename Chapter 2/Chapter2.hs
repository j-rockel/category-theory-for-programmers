module Chapter2 where

import System.CPUTime

slowFib :: Int -> Integer
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n - 2) + slowFib (n - 1)

-- This is very fast

memoizedFib :: Int -> Integer
memoizedFib = (map fib [0 ..] !!)
  where
    fib 0 = 0
    fib 1 = 1
    fib n = memoizedFib (n - 2) + memoizedFib (n - 1)

-- Careful, this does not work the same way !!

memoize :: (Int -> a) -> Int -> a
memoize = \f i -> map f [0 ..] !! i
{-# INLINE memoize #-}

memoizedFib' :: Int -> Integer
memoizedFib' = memoize fib
  where
    fib 0 = 0
    fib 1 = 1
    fib n = memoizedFib' (n - 2) + memoizedFib' (n - 1)

main :: IO ()
main = do
  putStrLn "Slow"
  getCPUTime >>= print
  print (slowFib 30)
  getCPUTime >>= print
  print (slowFib 30)
  getCPUTime >>= print
  print (slowFib 30)
  getCPUTime >>= print
  putStrLn "Memoized"
  getCPUTime >>= print
  print (memoizedFib 30)
  getCPUTime >>= print
  print (memoizedFib 30)
  getCPUTime >>= print
  print (memoizedFib 30)
  getCPUTime >>= print
  return ()