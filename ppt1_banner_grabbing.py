# Forma de conocer qué infraestructura o sistema se encuentra detrás de una aplicación web o servicio
import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(s.recv(1024))

def main():
    try:
        ip = input("IP: ")
        #  190.187.119.61
        port = str(input("Puerto: "))
        # 2022
        banner(ip, port)
    except:
        print("No se encontro informacion")

main()































# # Banner_grabbing
# import http.client
# from os import path

# if path.exists("vulnerables.txt"):
#     host = "localhost"

#     http = http.client.HTTPConnection(host, timeout=2)
#     http.request("HEAD", "")

#     server = http.getresponse().getheader("server")
#     vulnerables = open("vulnerables.txt", "r")
#     esVulnerable = False

#     for servicio in vulnerables:
#         s = servicio.split(" ")
#         if s[0] in server:
#             print(host, "tiene servicio", s[0], "con posible vulnerabilidad", s[1])
#             esVulnerable = True
#     if not esVulnerable:
#         print(
#             host,
#             "no cuenta con un servicio vulnerable de la lista, o no da la informacion",
#         )
# else:
#     print("No se encuentra la lista")












