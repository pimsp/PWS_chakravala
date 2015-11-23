# PWS_chakravala
Generates the fundamental solution to Pell's equation and creates a class and several functions for performing calculations in $Z[\sqrt{d}]$ or $Z/nZ[\sqrt{d}]$.

# The fundamental solution
Calculates the fundamental solution using the chakravala method.
Example usage:
```python
>>> smallest_solution_Pell(34)
[35,6]
>>> 35**2 - 34*6**2
1
```

# $Z[\sqrt{d}]$
Given a,b,d and f, represents the number $a+b\sqrt{d}$ with coefficients a,b in $Z/fZ$ (a,b in Z if f isn't given).
Can multiply and add two numbers with the same d and f.
Prints a given number.
Calculates the order of a solution mod f: the smallest power such that f divides the b-value.

Example usage:
```python
>>> alpha = ZfZsqrtd(35,6,34,17)
>>> print(alpha)
1+6sqrt{34} (mod 17)
>>> print(alpha*alpha)
1+12sqrt{34} (mod 17)
>>> print(orde(alpha,17))
17
```


## License

PWS_chakravala is released under the [MIT License](http://opensource.org/licenses/MIT).  
Copyright (c) 2015 Pim Spelier
