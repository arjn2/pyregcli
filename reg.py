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
import subprocess

pt2,pt,path_history,keyA='','','',[]

def menu():
    global root
    global pt
    global pt2
    global path_history

    ch=0
    try :
        
        while(ch!=11):
            print("------------------------------------------------\n Current path=",path_trace(),"\n---------------------------------------------------")
            ch=int(input("\n MENU \n 1.READ_REGISTRY_ENTRY \n 2.ADD_REGISTRY_ENTRY \n 3.SET_ROOT_LOCATION (HKEY_LOCAL_MACHINE,HKEY_CURRENT_USER,..) \n 4.GOTO_ANY_PATH \n 5.CREATE_KEY \n 6.CREATE_VALUE \n 7.LIST_KEYS \n 8.LIST_VALUES \n 9.RESET_PATH (FOR DIFFERENT KEYS) \n 10.EXIT- Enter choice: "))
            if(ch==1):
                read_registry_entry()
            elif(ch==2):
                add_registry_entry()
            elif(ch==3):
                rootloc()
            elif(ch==4):
                cdpath()
            elif(ch==5):
                mkkey()
            elif(ch==6):
                mkvalue()
            elif(ch==7):
                lskey()
            elif(ch==8):
                lsval()
            elif(ch==9):
                reset_path()
            elif(ch==10):
                clskeys()
                print("PROGRAM EXITED")
                ch=11
            else:
                print("INVALID KEY")
                
    except Exception as e:
            print("ERROR",e)
        
def path_trace():
    full_path=pt+":"+r"\\"+pt2
    return full_path


def read_registry_entry():
    cdpath()
    lskey()
    lsval()
    reset_path()

def add_registry_entry():
    pass
    

def rootloc():
    global root
    global pt
    global sf
    root=''
    
    ch=0
    try:
        while(ch!=6):
                reset_path()
                ch=int(input("\n ROOT KEYS \n 1.HKEY_CLASSES_ROOT \n 2.HKEY_CURRENT_USER \n 3.HKEY_LOCAL_MACHINE \n 4.HKEY_USERS \n 5.HKEY_CURRENT_CONFIG\n 6.QUIT \n Enter choice: "))
                if(ch==1):
                    root=wrg.HKEY_CLASSES_ROOT
                    pt='HKEY_CLASSES_ROOT'
                    sf='HKCR'

                elif(ch==2):
                    root=wrg.HKEY_CURRENT_USER
                    pt='HKEY_CURRENT_USER'
                    sf='HKCU'

                elif(ch==3):
                    root=wrg.HKEY_LOCAL_MACHINE
                    pt='HKEY_LOCAL_MACHINE'
                    sf='HKLM'

                elif(ch==4):
                    root=wrg.HKEY_USERS
                    pt='HKEY_USERS'
                    sf='HKU'

                elif(ch==5):
                    root=wrg.HKEY_CURRENT_CONFIG
                    pt='HKEY_CURRENT_CONFIG'
                    sf='HKCC'
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
    global keyA
    global k
    # if(not key):
        
    try:
        if(key==''):
            print("\nPlease select a hive before proceeding...")
            rootloc()
            print("------------------------------------------------\n Current path=",path_trace(),"\n---------------------------------------------------")
    except NameError:
        print("\nPlease select a hive before proceeding...")
        rootloc()
        print("------------------------------------------------\n Current path=",path_trace(),"\n---------------------------------------------------")
  


    pa=str(input("Enter registry path or keyname (eg:SOFTWARE or SOFTWARE\\\\Classes): "))
    k=pa

    if(path_history):
        pa=path_history+r"\\"+pa
    
    try:
        key=wrg.OpenKeyEx(root,pa)
        keyA.append(key)
        if(key):
            pt2=pa
            path_history=pt2  # update path_history
            #print(f"Successfully opened path: {pa}")


    except Exception as e:
        
        print("Error", e)

def mkkey():
    keyn=str(input("Enter key_name: "))
    path=path_trace()
    try:
        nk=wrg.CreateKey(key,keyn)
        if(nk):
            print(f"Successfully created key: {keyn}")
    except Exception as e:
        print("Error",e)
        
def lskey():
    qn=input("Do you want to show all the keys -y(yes)/n(no)/c(cancel)")
    if(qn==('y' or 'yes')):
        print('--------------------------\nKeys\n-------------------------')
        i=0
        t=True
        while t==True:
            try :
                    subkey=wrg.EnumKey(key, i)
                    print(subkey)
                    i+=1
            except OSError:
                t=False
        print('\n --------------------\nkeys-end\n------------------------------\n')

    elif(qn==('n' or 'no')):
        no=int(input("Enter no of result to be shown: "))
        print('--------------------------\nKeys\n-------------------------')
        try :
            for i in range(no):
                subkey=wrg.EnumKey(key, i)
                print(subkey)
        except OSError:
                print('\n --------------------\nkeys-end\n------------------------------\n')
    
    elif(qn==('c' or 'cancel')):
        pass
    
    else:
        print("Invalid-Key")
        lskey()
    
def lsval():
    qn=input("Do you want to show all the values -y(yes)/n(no)/c(cancel)")
    if(qn==('y' or 'yes')):
        print('--------------------------\nValues\n-------------------------')
        i=0
        t=True
        while t==True:
            try :
                    subkey=wrg.EnumValue(key, i)
                    print(subkey)
                    i+=1
            except OSError:
                t=False
        print('\n --------------------\nValues-end\n------------------------------\n')


    elif(qn==('n' or 'no')):
        no=int(input("Enter no of result to be shown: "))
        print('--------------------------\nValues\n-------------------------')
        try :
            for i in range(no):
                subkey=wrg.EnumValue(key, i)
                print(subkey)
        except OSError:
                print('\n --------------------Values-end------------------------------\n')

    elif(qn==('c' or 'cancel')):
        pass
    
    else:
        print("Invalid-Key")
        lsval()

    
    # no=int(input("Enter no of result to be shown: "))
    # print('--------------------------\nvalues\n-------------------------')
    # try:
    #     for i in range(no):
    #         subkey=wrg.EnumValue(key, i)
    #         print(subkey)
    # except OSError:
    #     print('\n --------------------values-end------------------------------\n')




def mkvalue():
    try:
        # osaccess()
        ch=int(input("Enter type of value: \n 1.STRING \n 2.BINARY \n 3.DWORD-32 \n 4.DWORD-64 \n 5.Multi-String \n 6.Expandable-String \n Enter choice: "))
        if(ch==1):
            # vt=wrg.REG_SZ
            dt='String'
            val=str(input("Enter String-value: "))
        elif ch==2:
            # vt=wrg.REG_BINARY
            val=str(input("Enter Binary-value: "))
            dt='Binary'
        elif ch==3:
            # vt=wrg.REG_DWORD
            val=int(input("Enter DWORD value: "))
            dt='DWord'
        elif ch==4:
            # vt=wrg.REG_QWORD
            val=int(input("Enter QWORD value: "))
            dt='QWord'
        elif ch==5:
            # vt=wrg.REG_MULTI_SZ
            val=str(input("Enter Multi-String: ")).split(',')
            dt='MultiString'
        elif ch==6:
            # vt=wrg.REG_EXPAND_SZ
            val=str(input("Enter Expandable-String: "))
            dt='ExpandString'

        else:
            print("INVALID KEY")

        if(val):
            
            vn=str(input("Enter name: "))
            # re=wrg.SetValueEx(key, vn, 0, vt, val)
            k = path_trace().replace(pt, sf)
            psh=f"""New-ItemProperty -Path "{k}" -Name "{vn}" -Value "{val}" -Type {dt} -Force"""
            re=subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", psh])
            if(re):
                print("Value set successfully!")
        
    except Exception as e:
        print("Error:", e)

    
def reset_path():
    global full_path
    global pt
    global pt2
    global path_history
    global key
    clskeys()
    full_path=''
    pt=''
    pt2=''
    path_history=''
    key=''

def cdback():
    global pt2
    global path_history
    bck=path_history-k
    try:
        key=wrg.OpenKeyEx(root,bck)
        if(key):
            wrg.CloseKey(keyA(len(keyA)-1))
            path_history=bck # update path_history
            #print(f"Successfully opened path: {pa}")


    except Exception as e:
        
        print("Error", e)


def clskeys():
    if keyA:
        #print("keyA", keyA)
        for i in keyA:
            try:
                ck=wrg.CloseKey(i)
            except OSError as e:
                print("failed to close", i, "error code:", e)



menu() #MAIN_FUNCTION

