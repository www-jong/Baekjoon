import socket

# 서버 호스트와 포트 설정
# 서버 호스트와 포트 설정
HOST = '172.31.196.44'  # 루프백 주소 (로컬 호스트)
PORT = 8081  # 사용할 포트 번호
print('d')
# 서버와 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print('b')
while True:
    # 사용자로부터 숫자 입력 받기
    message = input("숫자를 입력하세요 (종료하려면 'q'를 입력): ")

    # 입력이 'q'인 경우 클라이언트 종료
    if message.lower() == 'q':
        break

    # 서버에 메시지 전송
    client_socket.sendall(message.encode())

    # 서버로부터 응답 받기
    data = client_socket.recv(1024)

    print(f"서버로부터 받은 응답: {data.decode()}")

# 클라이언트 소켓 종료
client_socket.close()