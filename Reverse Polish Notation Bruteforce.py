import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #GCF
         
        input = ""
        for a in tokens:
            input = input + a + " "
        x=input.split()
        print(x)
        i = 0
        numb1 = 0
        numb2 = 0
        sum = 0
        product = 1
        while len(x) > 1:
            if x[i]=="+" or x[i]== "-" or x[i]== "*" or  x[i]=="/":
                numb1 = x[i-2]
                numb2 = x[i-1]

                if x[i] == "+":
                    sum = int(numb1) + int(numb2)
                    x[i] = str(sum)
                    x.pop(i-1)
                    x.pop(i-2)
                    i = 0
                elif x[i] == "-":
                    sum = int(numb1) - int(numb2)
                    x[i] = str(sum)
                    x.pop(i-1)
                    x.pop(i-2)
                    i = 0
                elif x[i] == "*":
                    product = int(numb1) * int(numb2)
                    x[i] = str(product)
                    x.pop(i-1)
                    x.pop(i-2)
                    i=0
                elif x[i] == "/":
                    quotient = float(numb1)/float(numb2)
                    x[i] = str(int(quotient))
                    x.pop(i-1)
                    x.pop(i-2)
                    i=0

            else:
                i = i + 1
                
        return(int(x[0]))
