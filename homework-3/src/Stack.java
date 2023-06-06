// A Java class that is the implementation of the Stack ADT
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
        ok(topIndex != -1, "Stack is empty");
    }

    static void integerRange(int value, int minimum, int maximum) {
        ok(value >= minimum, "Must be at least " + minimum);
        ok(value <= maximum, "Must be at most " + maximum);

    }
}


public class Stack {
    private int maxSize;
    private String[] stackArray;
    private int topIndex;

    public Stack(int max) {
        Validate.integerRange(max, 1, Integer.MAX_VALUE);
        maxSize = max;
        stackArray = new String[maxSize];
        topIndex = -1;
    }

    public void push(String stringToAdd) {
        Validate.notNull(stringToAdd);
        expandStack();
        stackArray[++topIndex] = stringToAdd;
    }

    public String pop() {
        Validate.notEmpty(topIndex);
        return stackArray[topIndex--];
    }

    public String peek() {
        Validate.notEmpty(topIndex);
        return stackArray[topIndex];
    }

    public boolean empty() {
        return (topIndex == -1);
    }

    public int size() {
        return topIndex + 1;
    }

    private void expandStack () {
    	if (topIndex+1 < stackArray.length) {
    		return;
    	}
        Validate.integerRange(maxSize, 0, Integer.MAX_VALUE);
    	String[] expandedStack = new String[stackArray.length * 2];
    	for (int i = 0; i < stackArray.length; i++) {
    		expandedStack[i] = stackArray[i];
    	}
    	stackArray = expandedStack;
    }
}