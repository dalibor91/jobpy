from lib.Helpers.Dbg import Colorized
from lib.Helpers import Properties
import json
import os
import socket


class Client:

    socket = None
    socket_file = None

    def __init__(self):

        self.socket_file = Properties.get('socket_file')

        if self.socket_file is None:
            Colorized.red("Socket file is none")
            return False

        if not os.path.exists(self.socket_file):
            Colorized.red("Socket file not found '%s'" % Properties.get('socket_file'))
            return False

        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.socket.connect(self.socket_file)


    def _build_(self, controller, action=None, data=None):
        built = { "ctrl" : controller, "data": data }
        if action is not None:
            built["action"] = action
        return "%s\n" % json.dumps(built)

    def _request_(self, data):
        self.socket.send(data.encode('utf-8'))
        response = ""
        while True:
            data = self.socket.recv(1024)

            response = "%s%s" % (response, str(data.decode('utf-8')))

            if response.endswith("\n"):
                return str(response)

    def request(self, data):
        data = self._request_(data)
        try:
            parsed = json.loads(data.strip())
            if parsed:
                if 'error' in parsed:
                    if parsed['error']:
                        Colorized.red("There was an error")
                        Colorized.red("%s" % (parsed['msg'] if 'msg' in parsed else str(parsed)))
                    else:
                        return parsed['data'] if 'data' in parsed else None
                else:
                    raise Exception("'error' not found in response")
            else:
                raise Exception("Unable to parse")
        except Exception as e:
            Colorized.red("Unable to parse response")
            Colorized.red(str(e))
        return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.socket:
            self.socket.close()

    def close(self):
        if self.socket:
            self.socket.close()