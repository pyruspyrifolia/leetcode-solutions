class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        # In this for loop, i < len(s) - 1 ensures that we stop iterating over the loop
        # the and statement is for the edge case of when we Roman numerals try to write the number 4
        # Example: "IV" because I < V it will subtract from result which would then be -1
        # In the next iteration we would add V to -1 which would give us 4 

        for i in range(len(s)):
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]

        return result


print(Solution("IV"))
