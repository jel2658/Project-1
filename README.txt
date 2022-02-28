A server-to-client connection using Python sockets, for Computer Communication Networks, Spring 2022.
Transfers a file from server to client. The server files are in the same directory as the server and
client programs, and the client files are downloaded to the 'Downloads' directory.
Start 'server.py,' and it will listen for a client. Start 'client.py' after that, and it will
automatically connect to the server. You can type the full name of the file you want to download
(including the extension), and it will be sent over TCP connection. The exit command is '!exit,' and
will shut down the client connection to the server, but not the server itself. You can alt-F4 the
server or you can just close it.