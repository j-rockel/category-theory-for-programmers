interface Shape {
	public double area();
  public double circ();
}

public class Circle 
  implements Shape {
  private double radius;
  
  public Circle(double r){
    radius = r;
  }
  
  public double area() {
    double area = Math.PI * radius * radius;
    return area;
  }

  public double circ() {
    double circumference = 2.0 * Math.PI * radius;
    return circumference;
  }
}

public class Rect 
  implements Shape {
  private double width;
  private double height;
  
  public Rect(double w, double h){
  	width = w;
    height = h;
  }
  
  public double area() {
    double area = width * height;
    return area;
  }
  
  public double circ() {
    double circumference = 2.0 * (width + height);
    return circumference;
  }
}

public class Square 
  implements Shape {
  private double edge;
  
  public Square(double e){
  	edge = e;
  }
  
  public double area() {
    double area = edge * edge;
    return area;
  }
  
  public double circ() {
    double circumference = 2.0 * (edge + edge);
    return circumference;
  }
}

Rect testRect = new Rect(2,2);
System.out.println(testRect.area());
System.out.println(testRect.circ());