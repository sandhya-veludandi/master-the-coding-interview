## Regular Recursion
```JavaScript
function recFactorial(x) {
  if(x <= 1) {
    return 1; 
  }
  return x * recFactorial(x - 1); 
}
```

## Call Stack Space: O(n)
```JavaScript 
recFactorial(4); 
4 * recFactorial(3); 
4 * (3 * recFactorial(2)); 
4 * (3 * (2 * recFactorial(1))); 
4 * (3 * (2 * 1)); 
``` 

* Time: O(n)
* Space: O(n) because all the calls to the function must wait on an answer (have to calculate x*blah blah): `return x * recFactorial(x -1)`, for factorial 4 there were in total 4 calls to the function (4 recursive stacks)

## Tail Recursion
```JavaScript 
function tailFactorial(x, totalSoFar = 1) {
  if (x === 0) {
    return totalSoFar; 
  }
  return tailFactorial(x - 1, totalSoFar * x); 
}
```

## Call Stack Space: O(1)
```JavaScript
tailFactorial(4); 
tailFactorial(4, 1); 
tailFactorial(3, 4); 
tailFactorial(2, 12); 
tailFactorial(1, 24); 
tailFactorial(0, 24); 
```

* Time: O(n)
* Space: O(1) because we are no longer waiting on an answer (no waiting on x * blah blah calculation): `return tailFactorial(x - 1, totalSoFar * x)` 
* Engine compiler dependent: tail recursion O(1) space won’t occur
