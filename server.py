import socket
from threading import Thread
import json

from config import SERVER_ADDRESS, BUFSIZE

# database sementara untuk memegang info clients
clients = {}


def system_message(client, text):
    client.send(
        bytes(json.dumps({'type': 'system', 'text': text}), 'utf8'))


def broadcast(data):
    for client in clients:
        client.send(bytes(json.dumps(data), 'utf8'))


def handle_client(client):
    while True:
        try:
            data = client.recv(BUFSIZE).decode('utf8')
            if data:
                msg = json.loads(data)
                print(msg)
                # Contoh protokol pesan sederhana:
                # {"type": "init", "name": "eka", "pubkey": "13"}
                # {"type": "message", "text": "Halo"}

                if msg.get('type') == 'init':
                    clients[client] = msg

                    if len(clients) < 2:
                        # baru 1 orang, tunggu...
                        system_message(client, 'Menunggu teman chat...')
                    else:
                        # sudah lengkap, kirimkan info ke lawan chat
                        for client1 in clients:
                            for client2 in clients:
                                if client1 != client2:
                                    client1.send(
                                        bytes(json.dumps(clients[client2]), 'utf8'))

                if msg.get('type') == 'message':
                    if msg.get('text') == 'quit':
                        raise Exception('quit')

                    msg['name'] = clients[client].get('name')
                    broadcast(msg)

        except Exception as e:
            del clients[client]
            break

    client.close()


if __name__ == '__main__':

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('[INFO] Server berjalan di localhost:8000')
    server.bind(SERVER_ADDRESS)
    server.listen(1)

    while True:
        client, addr = server.accept()
        # Biar simple kita batasi client cuma 2
        if len(clients) == 2:
            system_message(client, 'quit')
            client.close()
        else:
            Thread(target=handle_client, args=(client,)).start()

    server.close()
