class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split("-")
        
        binary = []
        for d in date:
            binary.append(bin(int(d))[2 : ])
        
        return "-".join(binary)