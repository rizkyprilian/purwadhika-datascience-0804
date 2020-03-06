# Function to find that number  
# divisible by 3 or not 
def check(num) : 
    counter = 0  
    # Compute sum of digits 
    digitSum = 0
    while num > 0 : 
        counter += 1
        rem = num % 10
        print(f'{counter} rem {rem}')
        digitSum = digitSum + rem
        print(f'{counter} digitSum {digitSum}')  
        num = num / 10
        print(f'{counter} num {num}')

    # Check if sum of digits is  
    # divisible by 3. 
    return (digitSum % 3 == 0) 


print(check(1332))