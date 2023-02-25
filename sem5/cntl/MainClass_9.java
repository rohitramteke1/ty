import java.io.BufferedInputStream; 
import java.io.InputStream;
import java.io.OutputStreamWriter; 
import java.io.Writer;  
import java.net.InetAddress; 
import java.net.Socket; 
 
public class MainClass_9 { 
 
public final static int DEFAULT_PORT = 43; 
 
public final static String DEFAULT_HOST = "whois.internic.net"; 
 
public static void main(String[] args) throws Exception { 
    String domainTobeSearched = args[0]; 
 
    String serverName = System.getProperty("WHOIS_SERVER", DEFAULT_HOST); 
 
InetAddress server = null; 
server = InetAddress.getByName(serverName); 
    Socket theSocket = new Socket(server, DEFAULT_PORT); 
    Writer out = new OutputStreamWriter(theSocket.getOutputStream(), 
"8859_1"); 
out.write("domain " + domainTobeSearched + "\r\n"); out.flush(); 
InputStream raw = theSocket.getInputStream(); 
InputStream in = new BufferedInputStream(theSocket.getInputStream()); int c; while ((c = in.read()) != -1) 
System.out.write(c); 
  } 
} 
