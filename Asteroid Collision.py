asteriods =  [10,2,-5]
stack = []
for asteriod in asteriods:
    if asteriod>0:
        stack.append(asteriod)
        continue
    previousnumb = stack.pop()
    if previousnumb < abs(asteriod):
        stack.append(asteriod)
        asteriods.pop(previousnumb)
    elif previousnumb > abs(asteriod):
        stack.append(previousnumb)
        asteriods.pop(asteriod)
print(stack)

    


