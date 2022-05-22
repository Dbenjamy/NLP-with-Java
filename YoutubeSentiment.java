import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class YoutubeSentiment 
{
  public static void main(String[] args) 
  {
    // Create json parser
    JSONParser json_parser = new JSONParser();
    try {
      // Parse json and exctract string array of comments
      JSONObject data = (JSONObject) json_parser.parse(new FileReader("data.json"));
      
      ArrayList<String> comments = new ArrayList<String>();
      for (Object item:data.values()) {
        comments.add(item.toString());
      }
      // Compute average comment sentiment (1 bad, 5 great)
      int total = 0;
      int count = 0;
      IMPORTED.init();
      for (String item: comments) {
        total = total + IMPORTED.estimatingSentiment(item);
        count++;
      }
      // Displaying the results
      System.out.println("Average Score(Points/Comment Count):\n" + total/count);
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    } catch (ParseException e) {
      e.printStackTrace();
    }
  }
}

