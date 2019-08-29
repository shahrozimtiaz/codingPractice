package Inheritance;

public class Square extends Shape implements ShapeI {
    int l,w;
    public Square(){
        l = w =0;
    }
    public Square(int l, int w){
        this.l=l;
        this.w=w;
    }

    @Override
    public int area() {
        return l*w;
    }

    @Override
    public int perimeter() {
        return 4*l;
    }

    @Override
    public int test() {
        return 0;
    }

    public static void main(String[] args){
       Square sq = new Square(4,4);
       System.out.println("area: " + sq.area());
       System.out.println("perimeter: " + sq.perimeter());
    }
}