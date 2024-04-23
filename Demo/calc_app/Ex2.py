def main() -> None:
    result = 0
    history =[]
    command_id = 1
    while True:
        command = input("Enter a command (add, subtract, multiply, divide, clear, exit, history): ").strip().lower()

        if command == "exit":
            print("Exiting the program.")
            break
        elif command == "clear":
            result = 0
            print("Result: 0")
        elif command == "history":
            if not history:
                print("No history")
            else:
                for entry in history:
                    print(f"ID: {entry['id']}, Command: {entry['command']}, Operand: {entry['operand']}")
        elif command in ["add", "subtract", "multiply", "divide"]:
            try:
                operand = float(input("Please enter an operand: "))
                history.append({"id": command_id, "command": command, 
                                "operand": operand})
                command_id += 1

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