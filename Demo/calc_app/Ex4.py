from typing import Any

def print_history(history):
    if not history:
        print("No history available.")
    else:
        for entry in history:
            print(f"ID: {entry['id']}, Command: {entry['command']}, Operand: {entry['operand']}")

def remove_history_entry(history):
    try:
        id_to_remove = int(input("Enter the ID of the history entry to remove: "))
        original_length = len(history)
        history = [entry for entry in history if entry['id'] != id_to_remove]
        if len(history) < original_length:
            print("Entry removed.")
        else:
            print("No entry found with that ID.")
    except ValueError:
        print("Error: Invalid input for ID.")
    return history

def perform_operation(command, operand, result):
    if command == "add":
        return result + operand
    elif command == "subtract":
        return result - operand
    elif command == "multiply":
        return result * operand
    elif command == "divide":
        if operand == 0:
            print("Error: Division by zero.")
            return result
        return result / operand
    return result

def main() -> None:
    result = 0
    history: list[dict[str, Any]] =[]
    command_id = 1

    while True:
        command = input("Enter a command (add, subtract, multiply, divide, clear, exit, history, remove): ").strip().lower()

        if command == "exit":
            print("Exiting the program.")
            break
        elif command == "clear":
            result = 0
            history = []
            print("Result and history cleared.")
        elif command == "history":
            print_history(history)
        elif command == "remove":
            history = remove_history_entry(history)
        elif command in ["add", "subtract", "multiply", "divide"]:
            try:
                operand = float(input("Please enter an operand: "))
                history.append({"id": command_id, "command": command, "operand": operand})
                command_id += 1
                result = perform_operation(command, operand, result)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid input for operand.")
        else:
            print("Error: Unknown command.")

if __name__ == "__main__":
    main()
