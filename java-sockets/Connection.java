import java.io.*;
import java.net.Socket;
import java.util.HashSet;
import java.util.Set;
import java.util.Scanner;

public class Connection {
    protected static Set<Socket> connectionSet = new HashSet<>();
    private Socket socket;

    public Connection(Socket socketconnection){
        this.socket = socketconnection;
    }

    public void receiveMessage() throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(this.socket.getInputStream()));
        while(true){
            String message = in.readLine();
            System.out.println(message);
        }
    }

    public void sendMessage() throws IOException {
        Scanner input = new Scanner(System.in);
        PrintWriter out = new PrintWriter(this.socket.getOutputStream());
        String message = input.nextLine();
        out.println(message);
    }

    public static void updateConnectionList(Socket connection) {
        Connection.connectionSet.add(connection);
    }


} // class
