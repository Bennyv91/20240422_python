def main() -> None:
    result = 0
    while True:
        command = input("Enter a command (add, subtract, multiply, divide, clear, exit): ").strip().lower()

        if command == "exit":
            print("Exiting the program.")
            break
        elif command == "clear":
            result = 0
            print("Result: 0")
        elif command in ["add", "subtract", "multiply", "divide"]:
            try:
                operand = float(input("Please enter an operand: "))
                if command == "add":
                    result += operand
                elif command == "subtract":
                    result -= operand
                elif command == "multiply":
                    result *= operand
                elif command == "divide":
                    if operand == 0:
                        print("Error: Division by zero.")
                        continue
                    result /= operand
                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid input for operand.")
        else:
            print("Error: Unknown command.")
            
if __name__ == "__main__":
    main()