import socket
import sys
import os

def correr_robot_chat():
    # 📡 INTERFAZ DE CONEXIÓN IRC ESTÁNDAR DE KICK (Servidor de Chat Puro)
    HOST = "irc.kick.com"
    PUERTO = 6667
    
    # Chupa el nombre de tu canal desde las variables ocultas de GitHub
    CANAL = os.getenv("KICK_CHANNEL", "streamdrome").lower()
    # Nombre fantasma para el bot en la red de chat
    NICK = "mutiny_tv_bot" 

    print(f"[🤖 ROBOT]: Conectando a las venas de Kick IRC en el canal: #{CANAL}...")
    
    try:
        s = socket.socket()
        s.connect((HOST, PUERTO))
        
        # Protocolo de saludo obligatorio para entrar a la Matrix del chat
        s.send(f"NICK {NICK}\r\n".encode('utf-8'))
        s.send(f"JOIN #{CANAL}\r\n".encode('utf-8'))
        
        print("[🤖 ROBOT]: Conexión blindada. Escuchando el chat en caliente...")
        
        # Bucle de milisegundos infinito (Consume 0% de CPU y 15MB de RAM)
        while True:
            respuesta = s.recv(2048).decode('utf-8')
            if not respuesta: break
            
            # Responder al ping del servidor de Kick para que no nos corte el cable
            if respuesta.startswith("PING"):
                s.send("PONG :pingis\r\n".encode('utf-8'))
                continue
                
            # 🔬 DETECTOR INTERACTIVO QUIRÚRGICO:
            # Filtra las líneas del chat para extraer el nombre del usuario y su texto
            if "PRIVMSG" in respuesta:
                partes = respuesta.split(":", 2)
                if len(partes) >= 3:
                    usuario = partes[1].split("!")[0]
                    mensaje_usuario = partes[2].strip()
                    
                    print(f"[CHAT DETECTADO]: @{usuario}: {mensaje_usuario}")
                    
                    # Formateamos el texto ciberpunk recortado para que quepa en la marquesina
                    texto_pantalla = f"🍿 MUTINY TV | @{usuario}: {mensaje_usuario[:45]}"
                    
                    # ¡PUM! Pisamos el archivo de texto en la sombra del disco virtual
                    with open("abajo.txt", "w", encoding="utf-8") as f:
                        f.write(texto_pantalla)
                        
    except Exception as e:
        print(f"[🤖 ROBOT - WARN]: Error en la cañería del chat ({e}). Reiniciando...")
        sys.exit(1)

if __name__ == "__main__":
    correr_robot_chat()
