**multiple clients and one server**<br>
this code runs on several raspberry pi's that got a static ip address. That's why the socket connection is hard coded. Feel free to test with localhost.

**what happens**<br>
the server receives a message from any client. This message will be send to all clients that have been registered since the session started but it won't be send to the client that initiate this message. "Registration" happens when a socket connection is established. 

**author**: k.s.
