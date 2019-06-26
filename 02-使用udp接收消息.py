import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(('',8888))

    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)
        print(recv_data[0].decode('utf-8'))

    udp_socket.close()


if __name__ == '__main__':
    main()
