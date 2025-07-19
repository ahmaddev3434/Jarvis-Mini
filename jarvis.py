import os 
import webbrowser

print("------------------------Welcome To Jarvis Mini Created By Ahmad------------------------- ")
print("open chrome")
print("open calculator")
print("open notepad")
print("open mspaint")
print("search")
print("Enter q to quit \n")

def logic(x):
    if (x == 'open chrome'):
        print("Starting Chrome ....")
        os.system("start chrome")
    elif (x == 'open calculator'):
        print("Starting Calculator ....")
        os.system("start calc")
    elif (x == 'open notepad'):
        print("Starting Notepad ....")
        os.system("start notepad")
    elif (x == 'open mspaint'):
        print("Starting Mspaint ....")
        os.system("start mspaint")
    elif (x == 'search'):
        print("1 : Youtube")
        print("2 : Google")
        sx = int(input("Enter Where You Wanna search 1 or 2 : "))
        if (sx == 1):
            yt = input("Enter What You Wanna Search On Youtube : ")
            print(f"Searching {yt} On Youtube ....")
            webbrowser.open(f"https://www.youtube.com/results?search_query={yt}")
        elif (sx == 2):
            g = input("Enter What You Wanna Search On Google : ")
            print(f"Searching {g} On Google .....")
            webbrowser.open(f"https://www.google.com/search?q={g}")
        else:
            print("Invalid Command Entered")
    else:
        print("Unknown Command Entered")


while True:
    x = input("Enter The Function You Wanna Perform : ").lower()
    if x == 'q':
        print("Thanks For Using Good Bye")
        break
    logic(x)
