import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;

public class ImageAnalyer {
    public static void main(String[] args) throws IOException {
        print(isRetriever("dog1.jpg"));
    }
    private static boolean isRetriever(String fileName) throws IOException{
        HashMap<Color,Integer> map = new HashMap();
        File file = new File(fileName);
        BufferedImage image = ImageIO.read(file);
//        Color[][] colors = new Color[image.getHeight()][image.getWidth()];
        for(int i = 0;i< image.getHeight();i++){
            for(int j = 0; j< image.getWidth();j++){
                Color color = new Color(image.getRGB(j,i));
                map.put(color,0);
            }
        }
        HashMap original = toCompare();
        int count = 0;
        for(Color c : map.keySet()){
            if(original.containsKey(c)){
                count++;
            }
        }
        print(count);
        return count > 550;
    }
    private static HashMap toCompare() throws IOException{
        HashMap<Color,Integer> map = new HashMap();
        File file = new File("dog.jpg");
        BufferedImage image = ImageIO.read(file);
        Color[][] colors = new Color[image.getHeight()][image.getWidth()];
        for(int i = 0;i< image.getHeight();i++){
            for(int j = 0; j< image.getWidth();j++){
                Color color = new Color(image.getRGB(j,i));
                map.put(color,map.getOrDefault(color,0)+1);
            }
        }
        map.remove(Color.WHITE);
        return map;
    }
    private static void print(Object color) {
        System.out.println(color);
    }
}
