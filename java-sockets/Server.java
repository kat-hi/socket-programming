import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Server{

    public static void main(String[] args) throws IOException, InterruptedException {
        ServerSocket serversocket = new ServerSocket(12345);
        Socket socketConnection = serversocket.accept();
        Connection.updateConnectionList(socketConnection);

        while (true) {
            socketConnection = serversocket.accept();
            Connection.updateConnectionList(socketConnection);
            for(Socket connection : Connection.connectionSet) {
               Thread Receiver = new Thread(new ReceiverThread(connection));
               Thread Sender = new Thread(new SenderThread(connection));
               Receiver.start();
               Sender.start();
               Receiver.join();
               Sender.join();
            }
        }

    }//main

    static class SenderThread implements Runnable {
        Socket socketconnection;
        Connection con;

        public SenderThread(Socket socketconnection){
            this.socketconnection = socketconnection;
            this.con = new Connection(socketconnection);
        }

        @Override
        public void run() {
            try {
                con.sendMessage();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    static class ReceiverThread implements Runnable {
        Socket socketconnection;
        Connection con;

        public ReceiverThread(Socket socketconnection){
            this.socketconnection = socketconnection;
            this.con = new Connection(socketconnection);
        }

        @Override
        public void run() {
            try {
                con.receiveMessage();
            } catch (IOException e) {
                e.printStackTrace();
            }

        }
    }

}//class
