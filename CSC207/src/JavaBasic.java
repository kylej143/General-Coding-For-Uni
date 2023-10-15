public class JavaBasic {

    public JavaBasic q;

    // constructor (same name as Class, takes in parameter)
    public JavaBasic(JavaBasic x) {
        q = x;
    }

    public static void main(String[] args) {
        int i = 5;
        i = 3;
        System.out.println(i);

        int c = 3, d = 3;
        System.out.println(c+d);

        String sa = "1234";
        String sb = "1234";
        String poolItem = "hi";
        // True because sa, and sb's addresses point to the same object in the string pool
        System.out.println( sa == sb );
        // in the memory model, String Pool: {"1234", "hi"}

        String sc = new String("1234"); // notice how it is marked "original by intellij"
        // False because sc is an object and different from the string in the string pool
        System.out.println( sa == sc );
        String sd = new String("1234");
        // False; refers to different objects with the same values (compares addresses)
        System.out.println( sc == sd );

        JavaBasic JBobject = new JavaBasic(null);
        JavaBasic aliase1 = JBobject; // the address of aliase1 is the same as JBobject
        // if the object is mutable changing an object will change both.

        JavaBasic aliase2 = new JavaBasic(JBobject);
        // here the q is still an aliase of alise2's q
        JavaBasic stillaliase = new JavaBasic(aliase2.q);
        // to avoid aliase do this: (Deep Copy)
        JavaBasic tempQ = new JavaBasic(JBobject.q);
        JavaBasic notaliase = new JavaBasic(tempQ);


        System.out.println(aliase1);
        System.out.println(stillaliase.q);
        System.out.println(notaliase.q);

        // note primitives cannot make aliases

    }
}
