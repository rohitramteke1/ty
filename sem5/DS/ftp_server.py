from xmlrpc.server import SimpleXMLRPCServer

import os

# Put in your server IP here

server = SimpleXMLRPCServer(("",8000))

def server_receive_file(arg, filename):
    curDir = os.path.dirname(os.path.realpath(__file__))
    output_file_path = curDir + '/' + filename
    print('output_file_path -> ({})'.format(output_file_path))
    with open(output_file_path, "wb") as handle:
        handle.write(arg.data)
        print('Output file: {}'.format(output_file_path))
        return True

server.register_function(server_receive_file, 'server_receive_file')
print('Server is running ...!')
server.serve_forever()

