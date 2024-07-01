def add(n1,n2):
    return n1+n2
def subract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
calculator_dict={
    "+":add,
    "-":subract,
    "*":multiply,
    "/":divide
}
n1=int(input("Enter first number "))
n2=int(input("Enter second number "))
for symbol in calculator_dict:
    print(symbol)
symbol=input("Enter the operation you want to perform ")
task=calculator_dict[symbol]
print(task(n1,n2))