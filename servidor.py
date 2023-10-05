import xmlrpc.server

def jogo(a,b):
    if a == b:
        return 3
    elif  (a == 1 and b == 3) or (a == 2 and b == 1)or  (a==3 and b==1):
        return 1
    else:
        return 2
        
def resultado(resultado):
    if resultado == 1:
        return "O usuario1 ganhou"
    elif  resultado == 2:
        return "O usuario2 ganhou"
    else:
        return "Empate!!"
server = xmlrpc.server.SimpleXMLRPCServer(("localhost",8000))

server.register_function(jogo,"jogo")
server.register_function(resultado,"resultado")

print("Servidor RPD rodando na 8000")

try:
    server.serve_forever()
finally:
    server.server_close()