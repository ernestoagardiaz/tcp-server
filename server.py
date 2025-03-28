import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()
    print("Servidor escuchando en el puerto 5000...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión establecida con {client_address}")
        
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Cliente envió: {message}")
            
            if message.upper() == "DESCONEXION":
                print("Cliente solicitó desconexión.")
                client_socket.close()
                break
            else:
                client_socket.send(message.upper().encode("utf-8"))

def main():
    start_server()

if __name__ == "__main__":
    main()

# client.py
import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 5000))
    print("Conectado al servidor en localhost:5000")
    
    while True:
        message = input("Ingrese un mensaje: ")
        client_socket.send(message.encode("utf-8"))
        
        if message.upper() == "DESCONEXION":
            print("Cerrando conexión...")
            client_socket.close()
            break
        
        response = client_socket.recv(1024).decode("utf-8")
        print(f"Servidor responde: {response}")

def main():
    start_client()

if __name__ == "__main__":
    main()