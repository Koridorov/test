count=int(input("Enter the number of the candles: "))
list=[]

for i in range(count):
    candle=int(input("Enter the length of each candle: "))
    list.append(candle)

print(list.count(max(list)))
