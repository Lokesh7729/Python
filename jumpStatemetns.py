# Jump / Transfer Statements
#Used to alter loop flow.

#break → Exits the loop immediately.

for i in range(10):
    if i == 5:
        break
    print(i)

#continue → Skips current iteration and goes to next.

for i in range(5):
    if i == 2:
        continue
    print(i)


#pass → Does nothing (placeholder).

for i in range(3):
    pass  # future code here