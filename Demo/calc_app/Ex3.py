from typing import Any

def main() -> None:
    result = 0.0
    history: list[dict[str, Any]] =[]
    command_id = 0
    while True:
        command = input("Enter a command (add, subtract, multiply, divide, clear, exit, history, remove): ")

        if command == "exit":
            print("Exiting program.")
            break
        elif command == "clear":
            result = 0
            history = []
            print("Results and history cleared")
        elif command == "history":
            if not history:
                print("No history")
            else:
                for entry in history:
                    print(f"ID: {entry['id']}, Command: {entry['command']}, Operand: {entry['operand']}")
        elif command == "remove":
            if not history:
                print("No history")
            else:
                try:
                    id_to_remove = int(input("Enter the ID of the history entry to remove: "))
                    history = [
                        entry for entry in history if entry['id'] != id_to_remove]
                    print("Entry removed.")
                except ValueError:
                    print("Error: Invalid input for ID.")
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