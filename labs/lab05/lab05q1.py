
# t = ()
# t = t + (5,)      
# t = t + (10,)
# t = (1, 5, 3, 7, 2)

# print(t[0])  # 1
# print(t[1])  # 5
# print(t[2])  # 3
# print(t[3])  # 7
# print(t[4])  # 2

# print(t[-1])  
# print(t[-2])  

# # immutable

# print("tuple'ımız:", t)
# print("length is:", len(t))
# #print("length is: " + str(len(t)))


t = (1, 5, 3, 7, 2)
print("\nold tuple:", t, "\n")
new_tuple = ()
temp = t[0]
for i in range(1, len(t)-1):
      current = t[i]
      print(f"index {i}: {t[i]}")
      if(current > t[i-1] and current > t[i+1]):
            print(f"{current} is peak!")
            new_tuple += (current, )
            
      else:
            print("not peak!")
            
            
print("\nnew tuple:", new_tuple)