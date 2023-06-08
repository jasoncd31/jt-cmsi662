// A Java class that is the implementation of the Stack ADT
import java.util.EmptyStackException;
import java.util.Objects;

interface Validate {
    static void ok(boolean condition, String message) {
        if (!condition) {
            throw new IllegalArgumentException(message);
        }
    }

    static void notNull(Object value) {
        Objects.requireNonNull(value, "String must not be null");
    }

    static void notEmpty(int topIndex) {
        if (topIndex == -1) {
            throw new EmptyStackException();
        }
    }

    static void integerRange(int value, int minimum, int maximum) {
        ok(value >= minimum, "Must be at least " + minimum);
        ok(value <= maximum, "Must be at most " + maximum);

    }
}


public class Stack {
    private String[] elements;
    private int topIndex;
    private static final double ENLARGE = 2;
    private static final double SHRINK = .5;

    public Stack(int capacity) {
        Validate.integerRange(capacity, 1, Integer.MAX_VALUE);
        elements = new String[capacity];
        topIndex = -1;
    }

    public void push(String stringToAdd) {
        Validate.notNull(stringToAdd);
        elements[++topIndex] = stringToAdd;
        refactorCapacity();
    }

    public String pop() {
        Validate.notEmpty(topIndex);
        String popped = elements[topIndex];
        elements[topIndex--] = null;
        refactorCapacity();
        return popped;
    }

    public String peek() {
        Validate.notEmpty(topIndex);
        return elements[topIndex];
    }

    public boolean empty() {
        return (topIndex == -1);
    }

    public int size() {
        return topIndex + 1;
    }

    /**
     * Refactors the array elements are stored in
     * doubling the size when the array is full and 
     * shrinking it by half when the array is only 1/4 
     * filled, except for when the array is empty or there
     * is only one element
     */
    private void refactorCapacity() {
        int size = topIndex+1;
        if ((size == 1 && elements.length !=1) || topIndex == -1 || (size < elements.length && size > ((int)(elements.length / 4)))) {
            return;
    	}
        double factor = (size == elements.length ? ENLARGE : SHRINK);
        Validate.integerRange(elements.length, 0, Integer.MAX_VALUE);
        String[] refactoredStack = new String[(int)(elements.length * factor)];
        System.arraycopy(elements, 0, refactoredStack, 0, topIndex+1);
        elements = refactoredStack;
    }

}