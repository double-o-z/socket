

def pil(client_socket, args):
    f = open(r"C:\Users\shai\dev\socket\images\client_screen.jpg", 'wb')
    request = "{} {}".format("PIL", args)
    client_socket.send(request)
    r = client_socket.recv(1024)
    while r:
        print("Receiving Image Data..")
        f.write(r)
        r = client_socket.recv(1024)
    f.close()


def list_files(client_socket, args):
    request = "{} {}".format("GLOB", args)
    client_socket.send(request)
    print("Listing files at path: {}".format(args))
    r = client_socket.recv(1024)
    while r:
        print(r)
        r = client_socket.recv(1024)


def remove_file(client_socket, args):
    request = "{} {}".format("REMOVE", args)
    client_socket.send(request)
    r = client_socket.recv(1024)
    print(r)


def copy_file(client_socket, args):
    request = "{} {} {}".format("COPY", args[0], args[1])
    client_socket.send(request)
    r = client_socket.recv(1024)
    print(r)


def call_process(client_socket, args):
    request = "{} {}".format("CALL", args)
    client_socket.send(request)
    r = client_socket.recv(1024)
    print(r)
