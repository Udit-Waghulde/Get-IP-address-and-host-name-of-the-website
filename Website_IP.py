import socket


def get_hostname_IP():
    hostname = input("Please enter website address(URL) : ")
    try:
        print(f'Hostname: {hostname}')
        print(f'IP : {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'Invalid host name, error is raised {error}')


get_hostname_IP()