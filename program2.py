class Solution(object):
    def romanToInt(self, s: str) -> int:
        # Map of Roman numerals to integer values
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        total = 0  # Variable to store the result

        # Iterate through the string
        for i in range(len(s)):
            # If the current numeral is smaller than the next numeral, subtract its value
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]

        return total