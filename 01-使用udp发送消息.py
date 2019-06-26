import socket


def main():
   udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

   while True:
       send_data = input('请输入您要发送的内容: ')
       if send_data == 'exit':
           return
       else:
           udp_socket.sendto(send_data.encode('utf-8'),('192.168.43.84', 8888))


   udp_socket.close()


if __name__ == '__main__':
    main()
