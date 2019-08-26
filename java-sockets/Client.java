import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client {


    public static void main(String[] args) throws IOException {

        Socket clientsocket = new Socket("127.0.0.1", 12345);
        PrintWriter out = new PrintWriter(clientsocket.getOutputStream());
        pingForRegistration(clientsocket, out);
        BufferedReader in = new BufferedReader(new InputStreamReader(clientsocket.getInputStream()));
        Scanner input = new Scanner(System.in);

        while (True) {
            new Thread(new ReceiveThread(in)).start();
            Client.receiveMessage(in);
            Client.sendMessage(input, out);
        }
    }

    public static void pingForRegistration(Socket clientsocket, PrintWriter out) {
        out.println("Ping");
    }

    public static void receiveMessage(BufferedReader in) throws IOException {
        String message = in.readLine();
        System.out.println(message);
    }

    public static void sendMessage(Scanner input, PrintWriter out) {
        String message = input.nextLine();
        out.println(message);
    }


    static class SendThread implements Runnable{
        PrintWriter out;
        Scanner input;

        public SendThread(Scanner input, PrintWriter out){
            this.input = input;
            this.out = out;
        }

        @Override
        public void run() {
            try {
                Client.receiveMessage(in);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    static class ReceiveThread implements Runnable{
        BufferedReader in;

        public ReceiveThread(BufferedReader in) {
            this.in = in;
        }

        @Override
        public void run() {
            Client.sendMessage(input, out);

        }
    }

}