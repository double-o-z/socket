import socket
from server_methods import *

commands = {
    "PIL": {"args": r"C:\Users\shai\dev\socket\images\server_screen.jpg", "function": print_screen},
    "GLOB": {"args": r"C:\Users\shai\dev\socket\Scripts\*.*", "function": list_files},
    "REMOVE": {"args": r"C:\Users\shai\dev\socket\images\bamba", "function": remove_file},
    "COPY": {"args": [r"C:\Users\shai\dev\socket\images\1.txt", r"C:\Users\shai\dev\socket\images\2.txt"],
             "function": copy_file},
    "CALL": {"args": r"C:\Windows\notepad.exe", "function": call_process}
}

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 2580))
server_socket.listen(1)

while True:

    (client_socket, client_address) = server_socket.accept()
    client_sent = client_socket.recv(1024)

    if client_sent:
        parts = client_sent.split()
        cmd = parts[0]

        if cmd in commands.keys():
            command = commands.get(cmd)

            if len(parts) == 2:
                args = r"{}".format(parts[1])
            elif len(parts) > 2:
                args = [r"{}".format(arg) for arg in parts[1:]]
            else:
                args = command.get("args")

            function = command.get("function")
            function(client_socket, args)

    print("Finished. Closing connection to Client.")
    client_socket.close()

print("Shutting down Server.")
server_socket.close()
