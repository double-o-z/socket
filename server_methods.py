from PIL import ImageGrab
import glob
import os
import shutil
import subprocess


def print_screen(client_socket, args):
    im = ImageGrab.grab()
    im.save(args[0])
    f = open(args[0], 'rb')
    l = f.read(1024)
    while l:
        print("Sending Image Data..")
        client_socket.send(l)
        l = f.read(1024)
    f.close()


def list_files(client_socket, args):
    files_list = glob.glob(args)
    print("Sending client a list of files at path: {}".format(args))
    for f in files_list:
        client_socket.send(f.replace("C:\Users\shai\dev\socket\Scripts\\", ""))


def remove_file(client_socket, args):
    print("Removing file: {}".format(args))
    os.remove(args)
    client_socket.send("File: {} - Removed.".format(args))


def copy_file(client_socket, args):
    print("Copying file: {} to {}.".format(args[0], args[1]))
    shutil.copy(args[0], args[1])
    client_socket.send("File: {} copied to {}.".format(args[0], args[1]))


def call_process(client_socket, args):
    print("Calling process: {}.".format(args))
    client_socket.send("Calling process: {}.".format(args))
    subprocess.call(args)
