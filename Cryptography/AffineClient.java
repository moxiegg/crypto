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

public class AffineClient {
    
    private static String encryptMessage(String message, int a, int b) {
        StringBuilder encrypted = new StringBuilder();

        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                int x = c - 'a'; // Convert to 0-25 range
                int encryptedChar = (a * x + b) % 26;
                encrypted.append((char) (encryptedChar + 'a')); // Convert back to character
            } else {
                encrypted.append(c);
            }
        }

        return encrypted.toString();
    }
    public static void main(String[] args) {
        String serverAddress = "localhost";
        int serverPort = 12345;

        try {
            Socket socket = new Socket(serverAddress, serverPort);
            System.out.println("Connected to server");

            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            System.out.println("Enter Message to be sent: ");
            String plainText = reader.readLine();
            int[] key = new int[2];
            System.out.println("Enter Key to be used: ");
            String keys = reader.readLine().toLowerCase();
            int i = 0;
            for (String c: keys.split(" ")){
                key[i++] = Integer.parseInt(c);
            }
            System.out.println("Key to be sent: " + key[0] + "," + key[1]);
            writer.println(keys);
            String encryptedMessage = encryptMessage(plainText,key[0],key[1]);
            System.out.println("Encrypted message to be sent: " + encryptedMessage);
            writer.println(encryptedMessage);
            
            reader.close();
            writer.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
