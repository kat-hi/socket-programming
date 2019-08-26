import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Server extends Connection {

    public static void main(String[] args) throws IOException {
        ServerSocket serversocket = new ServerSocket(12345);
        Socket socketConnection = serversocket.accept();
        Connection.updateConnectionList(socketConnection);

        while (true) {
            socketConnection = serversocket.accept();
            Server.updateConnectionList(socketConnection);
            for(connection : connectionSet){
                socketConnection.getInputStream();
            }
            String message = in.readLine();
            out.println(message);
        }
    }//main

}//class
