class Solution:
    def PrintMinNumber(self , numbers: List[int]) -> str:
        # write code
        if not numbers:
            return ""
        l=len(numbers)
        for i in range(l-1):
            for j in range(i+1,l):
                if str(numbers[i])+str(numbers[j])>str(numbers[j])+str(numbers[i]):
                    numbers[i],numbers[j]=numbers[j],numbers[i]
        print(numbers)
        numbers=list(map(str,numbers))
        return "".join(numbers)