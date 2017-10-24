import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class CSVReader {
    public static void main(String[] args) {
        try{
            File file = new File("reviews.csv");
            Scanner scnr = new Scanner(file);
        }catch(FileNotFoundException e){
            e.getStackTrace();
        }
    }
}