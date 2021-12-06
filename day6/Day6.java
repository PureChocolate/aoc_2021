import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.math.BigInteger;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.HashMap;

public class Day6{
    
    public static void main(String[] args) throws Exception {
        Instant t1 = Instant.now();
        File f = new File("in2.txt");
        BufferedReader read = new BufferedReader(new FileReader(f));
        ArrayList<Integer> list = new ArrayList<>();

        //Read file and parse as ints
        for(String line = null; (line = read.readLine()) != null;){
            String st[] = line.split(",");
            for(String s : st){
                list.add(Integer.parseInt(s));
            }
        }
        HashMap<Integer, BigInteger> hm = new HashMap<>();
        for(int i = 0; i < 9; i++){
            hm.put(i,BigInteger.valueOf(0));
        }
        for(int i = 0; i < list.size(); i++){
            hm.put(list.get(i),hm.get(list.get(i)).add(BigInteger.valueOf(1)));
        }
        long end = Duration.between(t1,Instant.now()).toMillis();
        long sec = end / 1000;
        long min = sec / 60;
        System.out.println("Prasing time: " + min + "m " + sec + "s " + end + "ms ");

        int days = 256;
        t1 = Instant.now();
        while(days > 0){
            BigInteger h = hm.get(0);
            for(int i = 0; i <  8; i++){
                hm.put(i,hm.get(i+1));
            }
            hm.put(6,hm.get(6).add(h));
            hm.put(8,h);
            days--;
        }

        BigInteger tot = new BigInteger("0");
        for(int i = 0; i < 9; i++){
            tot = tot.add(hm.get(i));
        }
        end = Duration.between(t1,Instant.now()).toMillis();
        sec = end / 1000;
        min = sec / 60;
        System.out.println(tot);
        System.out.println("Calculate time: " + min + "m " + (sec % 60) + "s " + (end % 1000) + "ms ");
    }
}