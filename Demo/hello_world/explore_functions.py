def num_input(prompt: str) ->
    return int(input(prompt))

def sum_numbers(a: int, b: int) -> int:
    return a + b


def main() -> None:
    num1 = num_input("Enter a number:")
    num2 = num_input("Enter another number")

print (f"Sum: {sum_numbers(num1 + num2)}")

if __name__=="__main__":
    main()
