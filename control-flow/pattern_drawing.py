def draw_pattern():
    size = int(input("Enter the size of the pattern: "))
    
    row = 0
    
    while row < size:
        for col in range(size):
            print("*", end="")  # Print asterisk without newline
        print()
        row += 1

if __name__ == "__main__":
    draw_pattern()
