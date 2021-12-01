package day1;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.stream.IntStream;

public class Day1J{

    public static void main(String[] args) throws Exception {

        // Setup file reader and storing type(ArrayList)
        File f = new File("in.txt");
        BufferedReader read = new BufferedReader(new FileReader(f));
        ArrayList<Integer> list = new ArrayList<>();

        //Read file and parse as ints
        for(String line = null; (line = read.readLine()) != null;){
            list.add(Integer.parseInt(line));
        }

        //Convert list into an int array
        int[] data = list.stream().mapToInt(Integer::intValue).toArray();

        //Part 1 : Count the number if times the next number is higher than the prev
        int count = 0;
        for(int i = 1; i < data.length; i++){
            if(data[i] > data[i-1]) count++;
        }
        System.out.println(count);

        //PART 2-------------
        //Reset count for part 2, make a int array to store the 3 moving values
        count = 0;
        int tr[] = {data[0], data[1], data[2]};

        //Sum up the tracking array for a total value
        int prev = IntStream.of(tr).sum(); 

        //Start 3 up as already tracked first 3, rewrite the tracking values
        // by moving everything down and adding current value as the last
        for(int i = 3; i < data.length; i++){
            tr[0] = tr[1];
            tr[1] = tr[2];
            tr[2] = data[i];
            //Sum up the new tracking array, increase count if higher than prev 
            int s = IntStream.of(tr).sum();
            count += s > prev ? 1 : 0;
            prev = s;
        }
        System.out.println(count);
        //Arrays.toString(list.toArray())); way to print list.
    }

}