/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author student
 */
import java.io.*;
import java.net.*;

public class AffineServer {
    private static int modInverse(int a, int m) {
        a = a % m;
        for (int x = 1; x < m; x++) {
            if ((a * x) % m == 1) {
                return x;
            }
        }
        return -1;
    }
    public static int calculateGCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return calculateGCD(b, a % b);
    }

    private static String decryptMessage(String message, int a, int b) {
        StringBuilder decrypted = new StringBuilder();
        int aInverse = modInverse(a, 26);

        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                int y = c - 'a'; // Convert to 0-25 range
                int decryptedChar = (aInverse * (y - b + 26)) % 26;
                decrypted.append((char) (decryptedChar + 'a')); // Convert back to character
            } else {
                decrypted.append(c);
            }
        }

        return decrypted.toString();
    }

    public static void main(String[] args) {
        int port = 12345;

        try {
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server listening on port " + port);

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket.getInetAddress());

                BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter writer = new PrintWriter(clientSocket.getOutputStream(), true);
                int[] key = new int[2];
                String keys = reader.readLine();
                int i = 0;
                for (String c: keys.split(" ")){
                    key[i++] = Integer.parseInt(c);
                }
                String cipherText = reader.readLine(); // Read message
                int a = key[0];int b = key[1];int m = 26;
                int inverse = modInverse(a,m);
                if (calculateGCD(m,a) != 1){
                    System.out.println("Cannot decrypt the given string for the given key");
                } else{
                    String plainText = decryptMessage(cipherText,a,b);
                    System.out.println("Received: " + cipherText);
                    System.out.println("Result: " + plainText);
                }

                reader.close();
                writer.close();
                clientSocket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
