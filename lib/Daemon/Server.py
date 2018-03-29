import socket
import threading
import os
import sys
import signal


class Server:

    callback = None
    stop_server = False
    connections = 0

    def __init__(self, file):
        self.file = file
        if os.path.exists(self.file):
            os.unlink(self.file)

        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.socket.bind(self.file)

    def listen(self):
        self.socket.listen(10)

        signal.signal(signal.SIGTERM, self.shutdown)
        signal.signal(signal.SIGINT, self.shutdown)

        while True:
            if self.stop_server:
                break
            client, address = self.socket.accept()
            self.__add_thread__(client, address)
        self.__cleanup__()


    def __add_thread__(self, client, address):
        client.settimeout(360)
        tmpthread = threading.Thread(target=self.__onConnection__, args=(client, address))
        tmpthread.start()

    def setCallback(self, callback):
        self.callback = callback

    def getCallback(self):
        return self.callback

    def __cleanup__ (self):
        self.socket.close()
        os.unlink(self.file)

    def shutdown(self, s, f):
        print("Stop server: %s" % str(s))
        print("Connections: %d" % len(self.threads))
        self.stop_server = True
        self.__cleanup__()
        sys.exit()

    def __onConnection__(self, client, address):
        size = 1024
        read = "";
        while True:
            if self.stop_server:
                client.close()
                raise Exception("Stop server")

            try:
                data = client.recv(size)
                if data:

                    decoded = data.decode('utf-8')

                    if decoded.endswith("\n"):
                        #do send
                        if self.getCallback() is not None:
                            self.getCallback()(decoded.strip(), client, address)
                        read = ""
                    else:
                        read = "%s%s" %(read, decoded)
                else:
                    raise Exception('Client disconnected')
            except Exception as e:
                client.close()
                raise e