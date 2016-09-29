import socket
from client_methods import *

commands = {
    "PIL": {"args": r"C:\Users\shai\dev\socket\images\server_screen.jpg", "function": pil},
    "GLOB": {"args": r"C:\Users\shai\dev\socket\Scripts\*.*", "function": list_files},
    "REMOVE": {"args": r"C:\Users\shai\dev\socket\images\bamba", "function": remove_file},
    "COPY": {"args": [r"C:\Users\shai\dev\socket\images\1.txt", r"C:\Users\shai\dev\socket\images\2.txt"],
             "function": copy_file},
    "CALL": {"args": r"C:\Windows\notepad.exe", "function": call_process}
}

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 2580))
print("List of commands, and their default arguments: {}.\n".format(commands))
print("Write the command and arguments separated by a backspace.\n")
user_input = raw_input(">>>")

if user_input:
    parts = user_input.split()
    cmd = parts[0]
    command = commands.get(cmd)

    if len(parts) == 2:
        args = r"{}".format(parts[1])
    elif len(parts) > 2:
        args = [r"{}".format(arg) for arg in parts[1:]]
    else:
        args = command.get("args")

    function = command.get("function")
    function(client_socket, args)

print("Finished. Closing connection to Server. Shutting down Client")
client_socket.close()
