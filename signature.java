import java.security.*;
import java.nio.charset.StandardCharsets;

public class DigitalSignatureExample {

    public static void main(String[] args) throws Exception {

        String message = "This is the message to sign";
        byte[] messageBytes = message.getBytes(StandardCharsets.UTF_8);

        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        KeyPair keyPair = kpg.generateKeyPair();
        PrivateKey privateKey = keyPair.getPrivate();
        PublicKey publicKey = keyPair.getPublic();

        Signature sig = Signature.getInstance("SHA256withRSA");

        sig.initSign(privateKey);

        sig.update(messageBytes);

        byte[] digitalSignature = sig.sign();
        
        System.out.println("--- Sender Side ---");
        System.out.println("Message: " + message);
        System.out.println("Signature: " + bytesToHex(digitalSignature));
        System.out.println("-------------------");

        sig.initVerify(publicKey); 

        sig.update(messageBytes);

        boolean isVerified = sig.verify(digitalSignature);
        
        System.out.println("\n--- Receiver Side ---");
        if(isVerified) {
            System.out.println("VERDICT: Signature is VALID.");
        } else {
            System.out.println("VERDICT: Signature is INVALID.");
        }
        System.out.println("---------------------");
    }
    
    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02X", b));
        }
        return sb.toString();
    }
}