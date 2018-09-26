num=(int(input("ENter number of series : ")))
a=0
b=1
print('0')
print('1')
for i in range(num-2):
  t=a
  a=b
  b=t+a

  print(b)
