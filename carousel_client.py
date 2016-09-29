import socket
from carousel_methods import get_rand_port

port = 8111
while True:
    # Do Client Job
    client = socket.socket()
    client.connect(('127.0.0.1', port))
    print("Side B connecting to port {}.".format(port))

    port = get_rand_port()
    # user_input = raw_input("Message? ")
    user_input = "Bamba"
    message = "{}|{}".format(user_input, port)

    client.send(message)
    print("Side B: {}".format(user_input))
    client.close()
    print("Side B disconnected")

    # Do Server Job
    server = socket.socket()
    server.bind(('0.0.0.0', port))
    server.listen(1)
    print("Side B listening to port {}".format(port))

    (client_socket, client_address) = server.accept()

    message = client_socket.recv(1024)
    port = int(message.split("|")[1])

    client_socket.close()
    server.close()
