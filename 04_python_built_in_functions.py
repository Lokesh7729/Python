"""
📌 PYTHON BUILT-IN FUNCTIONS NOTES
---------------------------------
These are predefined functions in Python that can be used directly 
without importing any library. 
"""

# ===============================
# 1. INPUT / OUTPUT FUNCTIONS
# ===============================
print("Hello, World!")        # Output something
name = input("Enter your name: ")   # Take user input
print("Welcome,", name)

# ===============================
# 2. TYPE CONVERSION FUNCTIONS
# ===============================
x = "100"
print(int(x) + 50)            # Convert to int -> 150
print(float("3.14"))          # Convert to float
print(str(123) + " is string") # Convert to string
print(list("abc"))            # Convert to list
print(tuple([1,2,3]))         # Convert to tuple
print(set([1,2,2,3]))         # Convert to set {1,2,3}
print(dict([(1,'a'), (2,'b')])) # Convert to dictionary

# ===============================
# 3. MATHEMATICAL FUNCTIONS
# ===============================
print(abs(-10))       # Absolute value -> 10
print(pow(2, 3))      # 2^3 = 8
print(round(3.14159, 2))  # 3.14
print(min(5, 2, 7))   # Minimum = 2
print(max(5, 2, 7))   # Maximum = 7
print(sum([1,2,3]))   # Sum = 6

# ===============================
# 4. SEQUENCE RELATED FUNCTIONS
# ===============================
nums = [4, 1, 3]
print(len(nums))        # Length = 3
print(sorted(nums))     # [1, 3, 4]
print(list(reversed(nums)))  # [3, 1, 4]

for i, v in enumerate(nums):   # Enumerate -> index with value
    print(i, v)

# ===============================
# 5. TYPE & OBJECT RELATED FUNCTIONS
# ===============================
x = [1, 2, 3]
print(type(x))          # <class 'list'>
print(id(x))            # Unique ID in memory
print(isinstance(x, list))  # True
print(dir(x))           # All attributes/methods of list

# ===============================
# 6. UTILITY FUNCTIONS
# ===============================
print(help(len))        # Documentation of len()
print(eval("10+20"))    # Evaluate string as Python code -> 30
print(any([0, False, 2]))   # True (since 2 is True)
print(all([1, 2, 3]))       # True (all True)

print(list(zip([1,2], ["a","b"]))) # [(1,'a'),(2,'b')]

nums = [1,2,3,4]
print(list(map(lambda x: x*2, nums)))   # [2,4,6,8]
print(list(filter(lambda x: x%2==0, nums))) # [2,4]

"""
✅ QUICK REVISION - TOP 20 BUILT-IN FUNCTIONS
--------------------------------------------
1. print()   → Display output
2. input()   → Take user input
3. int()     → Convert to int
4. float()   → Convert to float
5. str()     → Convert to string
6. list()    → Convert to list
7. tuple()   → Convert to tuple
8. set()     → Convert to set
9. dict()    → Convert to dictionary
10. abs()    → Absolute value
11. pow()    → Exponentiation
12. round()  → Round number
13. min()    → Minimum value
14. max()    → Maximum value
15. sum()    → Sum of elements
16. len()    → Length of sequence
17. sorted() → Sorted sequence
18. type()   → Type of object
19. any()    → True if any element True
20. all()    → True if all elements True
"""
