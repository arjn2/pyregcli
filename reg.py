'''
Develop a Python Script for Windows Registry Manipulation

The Windows Registry is a crucial system database used by the Windows operating system to store configuration settings for the system and applications that opt to use the registry. Your assignment is to develop a Python script capable of interacting with the Windows Registry. The script should be able to write new entries, read existing entries, and handle potential errors effectively.

Write a Function to Add Entries to the Registry

Function Name: add_registry_entry
Purpose: Adds a new entry to a specified path in the registry.
Parameters: key_path (string), value_name (string), value_data (string or number, depending on the data type).
Error Handling: The function must be able to handle and report errors, such as permission issues or invalid data inputs.
Task: Create this function ensuring it provides clear feedback on the operation's success or failure.

Write a Function to Read Entries from the Registry

Function Name: read_registry_entry
Purpose: Reads an entry from a specified path in the registry.
Parameters: key_path (string), value_name (string).
Error Handling: The function should manage scenarios where the specified entry does not exist and other potential errors, providing appropriate feedback.
Task: Implement this function to handle exceptions gracefully and output relevant error messages or the value read.

Implement Basic User Input and Output

Interaction: Allow the user to specify whether they want to add or read a registry entry through command line input.
Input Details: Prompt the user for necessary details such as key_path, value_name, and value_data (for adding entries).
Output: Display the results of any registry interactions to the user, including successful operations or any error messages encountered.

Submit the completed script along with a brief report detailing:

How the script functions. Challenges encountered during development and how they were resolved. How the script handles different error scenarios.

Test the script in a controlled or virtual environment to avoid unintended changes to your operating system. Use non-critical registry paths for testing purposes to ensure system stability.


Prerequisites:  

Experience with importing and using modules in Python. Specific knowledge of the winreg module will be particularly useful.
Ability to handle files and exceptions in Python for reading from and writing to the Windows Registry safely.
Understand how to use try-except blocks to manage errors and exceptions in Python.
Awareness of the security implications of modifying the Windows Registry.
Understanding of Windows user permissions and how they might affect the ability to read from or write to the registry.
Basic knowledge of what the Windows Registry is and why it is important.
Familiarity with the structure of the Windows Registry, including understanding what keys, subkeys, and values are.
Ref. official Python documentation or tutorials specific to the winreg module.
'''



import winreg as wrg


pt2,pt,path_history='','',''

def menu():
    global root
    global pt
    global pt2
    global path_history

    ch=0
    try :
        
        while(ch!=7):
            print("------------------------------------------------\n Current path=",path_trace(),"\n---------------------------------------------------")
            ch=int(input("\n MENU \n 1.SET_ROOT_LOCATION \n 2.GOTO_ANY_PATH \n 3.MAKE_KEY \n 4.DEFINE_VALUE \n 5.LIST_KEYS \n 6.RESET_PATH \n 7.EXIT \n Enter choice: "))
            if(ch==1):
                rootloc()
            elif(ch==2):
                cdpath()
            elif(ch==3):
                mkkey()
            elif(ch==4):
                mkvalue()
            elif(ch==5):
                lsreg()
            elif(ch==6):
                reset_path()
    except Exception as e:
            print("ERROR",e)
        
def path_trace():
    full_path=pt+r"\\"+pt2
    return full_path

def rootloc():
    global root
    global pt
    root=''
    
    ch=0
    try:
        while(ch!=6):
                reset_path()
                ch=int(input("\n ROOT KEYS \n 1.HKEY_CLASSES_ROOT \n 2.HKEY_CURRENT_USER \n 3.HKEY_LOCAL_MACHINE \n 4.HKEY_USERS \n 5.HKEY_CURRENT_CONFIG\n 6.QUIT \n Enter choice: "))
                if(ch==1):
                    root=wrg.HKEY_CLASSES_ROOT
                    pt='HKEY_CLASSES_ROOT'
                elif(ch==2):
                    root=wrg.HKEY_CURRENT_USER
                    pt='HKEY_CURRENT_USER'

                elif(ch==3):
                    root=wrg.HKEY_LOCAL_MACHINE
                    pt='HKEY_LOCAL_MACHINE'

                elif(ch==4):
                    root=wrg.HKEY_USERS
                    pt='HKEY_USERS'

                elif(ch==5):
                    root=wrg.HKEY_CURRENT_CONFIG
                    pt='HKEY_CURRENT_CONFIG'

                elif(ch==6):
                    print("PROGRAM EXITED")
                    root=0
                    
                else:
                    print("INVALID KEY")
                    root=0
                
                return root
    except Exception as e:
            print("ERROR",e)
    
def cdpath():
    global pt2
    global key
    global path_history
    
    pa=str(input("Enter key name or a full path to open (eg:SOFTWARE or SOFTWARE\\Classes or list the key): "))
    if(path_history):
        pa=path_history+"\\"+pa
        
    #else:
    #    path_history=pt2
    
    try:
        
        key=wrg.OpenKeyEx(root,pa)
        if(key):
            pt2=pa
            path_history = pt2  # Update path_history to reflect the new path
            print(f"Successfully opened path: {pa}")
    except Exception as e:
        
        print("Error", e)

def mkkey():
    key=str(input("Enter key_name: "))
    path=path_trace()
    try:
        wrg.CreateKey(path,key)
    except Exception as e:
        print("Error",e)
        
def lsreg():
    no=int(input("Enter no of result to be shown: "))
    print('--------------------------\nKeys\n-------------------------')
    for i in range(no):
        subkey = wrg.EnumKey(key, i)
        print(subkey)
    pass
        

def mkvalue():
    pass
def reset_path():
    global full_path
    global pt
    global pt2
    global path_history
    global key
    full_path=''
    pt=''
    pt2=''
    path_history=''
    key=''


menu() #MAIN_FUNCTION

