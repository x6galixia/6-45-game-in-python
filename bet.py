def get_numbers(prompt, count):
    numbers = set()
    for i in range(1, count + 1):
        while True:
            try:
                number = int(input(f"{prompt} {i}: "))
                if 1 <= number <= 45:
                    numbers.add(number)
                    break
                else:
                    print("Please enter a number between 1 anid 45.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return numbers

def calculate_prize(matches):
    prize_dict = {
        3: 20,
        4: 120,
        5: 4000,
        6: 50000
    }
    return prize_dict.get(matches, 0)

def main():
    print("Enter the winning numbers:")
    winning_numbers = get_numbers("Enter winning number", 6)

    print("\nEnter your bet numbers:")
    bet_numbers = get_numbers("Enter your bet number", 6)

    matches = len(winning_numbers & bet_numbers)

    if matches > 0:
        prize = calculate_prize(matches)
        print(f"\nWinning numbers found are: {' '.join(map(str, winning_numbers & bet_numbers))}")
        print(f"You win ${prize:.2f}")
    else:
        print("No winning numbers found.")

if __name__ == "__main__":
    main()
