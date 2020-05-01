#take input format
input_format = list(map(int,input().split(" ")))

K = input_format[0]
M = input_format[1]

list_container = []
S = 0

#now take all input based on input format K
while K >0:
	#convert the space separated input into a list
	take_element = list(map(int,input().split(" ")))
	
	#append the take_element list into a container list
	#container list will containe each of the input list
	list_container.append(take_element)
	K-=1

each_max = []
power = 0

#access all separated list from container list
#then find the maximum value and append
#into the each_max list
for element in list_container:
	each_max.append(max(element))
	
#grab each max value then add into power
#with multiplied by power 2
for i in each_max:
	power+=i**2
	
#at the last calculate the modulus by M
#and print the final requirement value of S
S = power%M
print(S)