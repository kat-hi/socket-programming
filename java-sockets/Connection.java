import java.io.*;
import java.net.Socket;
import java.util.HashSet;
import java.util.Set;

public class Connection {
    private static Set<Socket> connectionSet = new HashSet<>();
    private Socket socket;

    public Connection(Socket connection) throws IOException {
        this.socket = connection;
    }

    public Connection(){
    }

    public void receiveMessage (Socket socketconnection) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(socketconnection.getInputStream()));
    }

    public void sendMessage (Socket socketconnection) throws IOException {
        PrintWriter out = new PrintWriter(socketconnection.getOutputStream());
    }

    public static void updateConnectionList(Socket connection) {
        Connection.connectionSet.add(connection);
    }


} // class
