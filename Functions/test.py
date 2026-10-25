def generate_floyd_triangle(rows: int) -> str:
    """Generates Floyd's Triangle with a given number of rows and returns it as a string."""
    lines = []
    num = 1
    
    for i in range(1, rows + 1):
        row_numbers = []
        for _ in range(i):
            row_numbers.append(str(num))
            num += 1
        lines.append(" ".join(row_numbers))
        
    return "\n".join(lines)

rows=int(input("Enter the number of rows: "))

print(generate_floyd_triangle(rows))

###################################################################################################

def string_operations(s: str, t: str, k: int) -> str:
    """Checks if string 's' can be converted into string 't' in 'k' operations."""
    # Find the length of the common prefix
    common_len = 0
    for char_s, char_t in zip(s, t):
        if char_s != char_t:
            break
        common_len += 1

    # Minimum operations required: delete remaining s + append remaining t
    min_ops = (len(s) - common_len) + (len(t) - common_len)

    # Standard "exact k operations" conditions:
    # 1. We have enough operations (k >= min_ops) AND the remaining moves are even (pop + append cancel out)
    # 2. OR k is large enough to completely erase 's' and rebuild 't' from scratch
    if (k >= min_ops and (k - min_ops) % 2 == 0) or k >= len(s) + len(t):
        return "Yes"
    
    return "No"

print(string_operations("abc", "def", 6))  # Output: Yes