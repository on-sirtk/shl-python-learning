#Num2 必須大於 Num1才能計算LCM
def lcm(num1, num2):  
  greater = num2 
  while(True):  
       if((greater % num1 == 0) and (greater % num2 == 0)):  
           lcm = greater  
           break  
       greater += 1  
  print(lcm)  

#檢查正整數
def check(number):
  try:
    val = int(number)
    if val < 0:  # if not a positive int print message and ask for input again
      print("必須正數")
      return False
  except ValueError:
      print("必須整數")
      return False
  return True   



num1 = input("第一個數?")
num2 = input("第二個數?")

#測試正整數
if (check(num1) and check(num2)):
  num1 = int(num1)
  num2 = int(num2)
  #** 加入你的代碼 **
  
  
  
  lcm(num1,num2)
