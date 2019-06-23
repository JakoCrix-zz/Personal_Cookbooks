###############################################################################
"""Worksheet 3- Conditions
- Using Conditionals
- If statement
"""
###############################################################################
# %% Conditionals
# Python first casts the object to a bool. As every non-empty string evaluates to True
bool(True);
bool(1); bool(2.0); bool("True"); bool("False")

bool(False)
bool(0); bool(0.0); bool(""); bool("False")
("Monday" and not "holiday" and not "birthday")    # the expression is equivalent to True and not True and not True


# %% Logical Operators
# Precedence over logical operators is as follows: relational operators (including in) > not > and > or.
(True and True)
(True and 1 != 1)
(1 > 2 or True)

(not True)                                              # The not operator negates the logical expression it is applied to
(not 1 > 2 and 1 > 0 or "din" in "coding")
((not(1 > 2) and 1 > 0) or ("din" in "coding"))



# %% Condition Testing- Integer
1 > 2
1 + 1 >= 1
2.0 == 4/2.0

1.==1                                              # 2 numbers equate if true value is the same no matter float or int
1 > 2.0
1 + 1 == 2.0
3.141592653 != 22/7

5 in [1,2,3,4,5]
(ord('A'), ord('a'))
((5>4), not(5>4))
(0<4<6<7, 0>5<6)


# %% Condition Testing- Strings
('he' < 'hi')                                      # In general, strings are compared and sorted by their alphabetical order; From smallest to largest, A-Z then a-z
('Hell' >= 'Hello')
('h' > 'H')
('Z' < 'a')

('Hell' in 'Hello')     # Using in as a operator
('hell' in 'Hello')     # it is case sensitive!

('le' in 'Hello')       # Should be false
('' in 'Hello')         # The empty string is in everything


print(5 in 10) ## note, can't do this as 10 is not iterable



# %%  Complex Ranges
n = 4
((0 < n) and (n < 6))

(0 < n < 6)                            # These are handled as 1 operation
('A' < 'Z' < 'a' < 'z')



# %% Example 1
name="Bob"
if name== "":
  print("A luddite! GO AWAY AT ONCE!")
elif (name.isdigit())>=1:
  print("HAHA! You may not pass!!" )
else:
  print("Welcome to the camp, " + name + ", if that really is your name.")

# %% Example 2
month= int(input("Enter the month (1-12): "))

if month==1 or month==2 or month==12:\
  print("It's summer. Have fun in the sun!")
elif 3<= month <=5:
  print("It's autumn. Enjoy the beautiful sunsets!")
elif 6<= month <=8:
  print("It's winter. Go skiing!")
elif 9<= month <=11:
  print("It's spring. Check out the spring racing carnival!")
else:
  print("Invalid input. Please enter any number between 1 and 12.")
