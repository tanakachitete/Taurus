public class StackTestHarness {
    public static void main(String[] args) {
        try {
            //  Instantiation
            Stack<Object> stack = new Stack<Object>();
            
            // Accessors and Mutators
            System.out.println("push Test (View code)");
            pushTest(stack, 100);
            System.out.println("Number of elements: " + stack.size());
            System.out.println("peek Test\nElement 0: " + stack.peek());
            System.out.println("pop Test\nTOP OF THE STACK");
            popTest(stack);
            System.out.println("BOTTOM OF THE STACK");
        }
        catch(IllegalStateException e) {
            System.out.println(e.getMessage());
        }
        catch(UnsupportedOperationException e) {
            System.out.println(e.getMessage());
        }
    }

    private static void pushTest(Stack<Object> stack, int numEnqueueElements) {
        for (int i = 0; i < numEnqueueElements; i++) {
            stack.push(Integer.valueOf(i));
        }
    }

    private static void popTest(Stack<Object> stack) {
        int numElements = stack.size();

        for (int i = 0; i < numElements; i++) {
            System.out.println("Element " + i + ": " + stack.pop());
        }
    }
}