# simple calculator program
class Calc:
       def __init__(self , perform):
            self.perform = perform
       def add(self,a,b):
           return a + b 
       def sub(self,a,b):
           return a - b 
       def mul(self,a,b):
           return a * b
       def div(self,a,b):
         if b > 0 :
           return a / b
         else:
            print('division error , Try Again!!')     

while True:
   print(f'''1-addition
2-subtraction
3-multiplication
4-division''')
   perform = input('enter (1,2,3,4)=').strip().lower()

   if perform == 'exit':
    print('bye!!')
    break 

   num1 = int(input('enter the number1='))
   num2 = int(input('enter the number2='))
   calculator = Calc(perform)

   if perform == '1':
    result = calculator.add(num1,num2)
    print(f'{perform} = {result}')
   elif perform == '2': 
    result = calculator.sub(num1,num2)
    print(f'{perform} = {result}')
   elif perform == '3':
    result = calculator.mul(num1,num2)
    print(f'{perform} = {result}') 
   elif perform == '4':
    result = calculator.div(num1,num2) 
    print(f'{perform} = {result}')
   else:
      print('invalid input , Try Again!!')     
