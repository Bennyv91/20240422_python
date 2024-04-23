def main() -> None:
   #infinite loop
   while True:
       #capture suser input from command line
       command = input ("Enter a command:")

       if command == "exit":
           #break will end loop
            break
       
       print (f"Received command: {command}")




if __name__=="__main__":
    main()
