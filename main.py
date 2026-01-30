array=[1,2,3,4,5,6,7,8,9,10]
ele=4
pos=Binary_search(array,ele)
print("Element found at ",pos)
def Binary_search(array,ele):
	left=0
	right=len(array)-1
	
	while(left<right):
		mid=(left+right)//2
		if(mid[array]==ele):
			pos=mid
		elif(ele<mid[array]):
			right=mid-1
		elif(ele>mid[array]
			left=mid+1
	return pos

