def array_product(arr):
	l=[]
	for i in range(len(arr)):
		prod=1
		for j in range(len(arr)):
			if i!=j:
				prod*=arr[j]
		l.append(prod)
	return l 

def main():
	n=int(input())
	arr=list(map(int,input().split()))
	print(array_product(arr))

main()