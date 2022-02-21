# Pokemon

python-oop:  command-line program 

`75` lines of code.

This simple command-line program in python shows how you can build a simple a command-line program in python using OOP concepts
such as attributes, classes and methods. 

## How to execute this program  

On the terminal, type the following command to run the program:  

`python3 -i pokemon.py`

## We can
```python
>>> print(ravi)
Ravi (grass)
	100/100 HP.

>>> print(vira)
Vira (water)
	200/200 HP.
```

### batle point

```python
>>> ravi.battle(vira)
---#_<
Ravi (grass)
	100/100 HP. 
---
 Vira (water)
	200/200 HP.

---#_<
Battle:  Ravi vs Vira
	Ravi fought Vira,
		and the result is a win
Vira lost and now has 180 HP.

---#_<
Ravi (grass)
	100/100 HP. 
---
 Vira (water)
	180/200 HP
```

or

```python
>>> vira.battle(ravi)
---#_<
Vira (water)
	200/200 HP. 
---
 Ravi (grass)
	100/100 HP.

---#_<
Battle:  Vira vs Ravi
	Vira fought Ravi,
		and the result is a lose
Vira lost and now has 180 HP.

---#_<
Vira (water)
	180/200 HP. 
---
 Ravi (grass)
	100/100 HP
```

## CONCEPTS
- Object-Oriented Programming in Python
- game logic
- instance methods
- `@staticmethod`
- self, other
- __init__, __str__
- if __name__ == '__main__'
- importing your own code
- scissor paper rock concept

## License

This code is open source. So feel free to use, modify, share, download as per your need. I do not take risk or responsibility for your errors or any commercial damage.
