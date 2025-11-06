import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class MD5Hashing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text to hash: ");
        String input = sc.nextLine();

        try {
            
            MessageDigest md = MessageDigest.getInstance("MD5");

        
            md.update(input.getBytes());
            byte[] digestBytes = md.digest();

            StringBuilder hexString = new StringBuilder();
            for (byte b : digestBytes) {
                hexString.append(String.format("%02x", b & 0xff));
            }

            System.out.println("MD5 Hash: " + hexString.toString());

        } catch (NoSuchAlgorithmException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
