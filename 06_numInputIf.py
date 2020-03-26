# 由使用寫輸入數字, Python 會以文字處理, 所以要轉成數字才能運算 
# 使用int("99") 可轉成數字 99
# 此程式會測試用戶輸入是否答案，傳回"太大" 或 "太小"
# 任務: 如果輸入的數字是88 (ans), 會傳回「正確」

ans = 88
num = int(input("輸入數字"))

# 条件：輸入的數字大過ans, 會出太大，否則出太小
if num > ans:
  print('太大')
elseif num < ans :
  print ('太小')
else:
  print('正確')
    

