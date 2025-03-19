def calculate_statistics(numbers):
    n = len(numbers)
    if n == 0:
        return None, None, None, None
    
    #Mean calculation
    total = sum(numbers)
    mean = total / n

    #Median calculation
    sorted_numbers = sorted(numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers [n // 2 - 1]) + (sorted_numbers [n // 2 + 1]) / 2

    #Variance calculation
    variance = sum((x - mean) ** 2 for x in numbers) / n

    #Mode calculation
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    mode = [num for num, freq in frequency.items() if freq == max_freq]
    if len(mode) == 1:
        mode = mode[0]
    
    return mean, median, variance, mode

def main():
    print("Welcome the calculator of statistic")
    print('Please enter the numbers which are you want to calculate press "q" to finish')

    numbers = []
    while True:
        print("Enter number or press (q) to finish")
        user_input = input("")
        if user_input.lower() == 'q':
            break
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Please enter the valid numbers")
    
    if not numbers:
        print("Hiç sayı girilmedi.")
    else:
        mean, median, variance, mode = calculate_statistics(numbers)
        print("\nCalculated Statistics:")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Variance: {variance}")
        print(f"Mode: {mode}")

if __name__ == "__main__":
    main()