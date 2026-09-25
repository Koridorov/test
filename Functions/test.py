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