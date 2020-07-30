def array_product(arr):
	l=[]

	prod=1
	for i in range(len(arr)):
		prod*=arr[i]

	for j in range(len(arr)):
		l.append(prod//arr[j])

	return l 

def main():
	n=int(input())
	arr=list(map(int,input().split()))
	print(*array_product(arr),sep=" ")

main()