public class SimpleClass {
    private String a;
    public SimpleClass(String input) {
        a = input;
    }

    public static void main(String args[]) {
        SimpleClass a = new SimpleClass("123");
        SimpleClass b = new SimpleClass("123");
        System.out.println(a.equals(b)); // false (equals between simpleclass)
        System.out.println(a.a.equals(b.a)); // true  (equals between two strings
    }
}