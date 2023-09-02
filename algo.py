""" 
Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().
"""

def visible_buildings(building_heights):
    visible_buildings = []
    max_height = 0

    for height in building_heights:
        if height > max_height:
            visible_buildings.append(height)
            max_height = height
        
    return visible_buildings

building_heights = [-1,1,1,7,3]
result = visible_buildings(building_heights)
print(result) 

"""
Create a standalone function that accepts two arrays and combines their values sequentially into a new array. Extra values from either array should be included afterward. Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100].
"""
def combine_arrays(arr1, arr2):
    combined = []
    len1, len2 = len(arr1), len(arr2)
    i, j = 0, 0

    while i < len1 and j < len2:
        combined.append(arr1[i])
        combined.append(arr2[j])
        i += 1
        j += 1

    while i < len1:
        combined.append(arr1[i])
        i += 1

    while j < len2:
        combined.append(arr2[j])
        j += 1

    return combined

arr1 = [4,15,100]
arr2 = [10,20,30,40]
result = combine_arrays(arr1,arr2)
print(result)

"""
Credit Card Validation (Bonus)
The Luhn formula is sometimes used to validate credit card numbers. Create the function isCreditCardValid(digitArr) that accepts an array of digits on the card (13-19 depending on the card), and returns a boolean whether the card digits satisfy the Luhn formula, as follows:

Set aside the last digit; do not include it in these calculations (until step 5);
Starting from the back, multiply the digits in odd positions (last, third-to-last, etc.) by 2;
If any results are larger than 9, subtract 9 from them;
Add all numbers (not just our odds) together;
Now add the last digit back in – the sum should be a multiple of 10.
"""
def is_credit_card_valid(digit_arr):
    last_digit = digit_arr.pop()

    for i in range(len(digit_arr) -1, -1, -2):
        digit_arr[i] *= 2
        if digit_arr[i] > 9:
            digit_arr[i] -= 9

    total = sum(digit_arr)

    total += last_digit

    return total % 10 == 0

digit_arr = [5, 2, 2, 8, 2]
result = is_credit_card_valid(digit_arr)
print(result)