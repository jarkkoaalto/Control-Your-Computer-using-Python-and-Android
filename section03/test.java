public class test {

    public void main(String[] args) {
        int a = 10;
        double b = 10.5;
        String c = "Hi";
        boolean d = true;

        System.out.println("Hello world");
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);

        if (a == 10) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        while (b > 10) {
            System.out.println("Pieni");
            b = b - 1;
        }

        for (int x = 0; x < 4; i++) {
            System.out.println("x");
        }

        do {
            System.out.println("a");
            a = a - 1;
        } while (a > 8);

    }

}