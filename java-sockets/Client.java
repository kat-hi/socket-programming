import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client {


    public static void main(String[] args) throws IOException, InterruptedException {

        Socket clientsocket = new Socket("127.0.0.1", 12345);
        PrintWriter out = new PrintWriter(clientsocket.getOutputStream());
        pingForRegistration(out);
        BufferedReader in = new BufferedReader(new InputStreamReader(clientsocket.getInputStream()));
        Scanner input = new Scanner(System.in);

        while (true) {
            Thread receive = new Thread(new ReceiveThread(in));
            receive.setDaemon(true);
            Thread send = new Thread(new SendThread(input,out));
            receive.start();
            send.start();
            send.join();
        }
    }

    public static void pingForRegistration(PrintWriter out) {
        out.println("Ping");
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
            String message = input.nextLine();
            out.println(message);
        }
    }

    public static class ReceiveThread implements Runnable{
        BufferedReader in;

        public ReceiveThread(BufferedReader in) {
            this.in = in;
        }

        @Override
        public void run() {
            String message = null;
            while(true){
                try {
                    message = in.readLine();
                    break;
                } catch (IOException e) {
                    e.printStackTrace();
                }
                System.out.println(message);
            }
        }

    }
}

