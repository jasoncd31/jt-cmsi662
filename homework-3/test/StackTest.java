import static org.junit.Assert.*;

import java.util.EmptyStackException;

import org.junit.Test;

public class StackTest {
    //JUNIT tests here for Stack class
    //Check if the Stack constructor works
    @Test
    public void testStack() {
        Stack stack = new Stack(1);
        assertEquals(0, stack.size());
        stack.push("Hi");
        assertEquals(1, stack.size());
        assertEquals(stack.peek(), "Hi");
    }

    @Test
    public void testPop(){
        Stack stack = new Stack(1);
        stack.push("Hi");
        assertEquals(stack.pop(), "Hi");
        assertEquals(stack.size(), 0);
    }

    @Test
    public void testPeek(){
        Stack stack = new Stack(1);
        stack.push("Hi");
        assertEquals(stack.peek(), "Hi");
        assertEquals(stack.size(), 1);
    }

    @Test
    public void testEmpty(){
        Stack stack = new Stack(1);
        assertEquals(stack.empty(), true);
        stack.push("Hi");
        assertEquals(stack.empty(), false);
    }

    @Test
    public void testPush() {
        Stack stack = new Stack(1);
        stack.push("Hola");
        stack.push("Bonjour");
    }

    
    @Test(expected = EmptyStackException.class)
    public void testNotEmpty() {
        Stack stack = new Stack(1);
        stack.pop();
        stack.peek();
    }

    @Test(expected = NullPointerException.class)
    public void testNotNull() {
        Validate.notNull(null);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testIntegerRange() {
        Stack stack1 = new Stack(0);
        Stack stack2 = new Stack(2147483647);
    }

    @Test(expected = NullPointerException.class)
    public void testStringNotNull() {
        String s = null;
        Stack stack = new Stack(1);
        stack.push(s);
    }

    @Test
    public void testRefactorBigger() {
        Stack stack = new Stack(4);
        stack.push("one");
        stack.push("two");
        stack.push("three");
        stack.push("four");
        stack.push("five");
        stack.push("six");
        stack.push("seven");
        assertEquals("seven", stack.peek());
        stack.pop();
        stack.pop();
        stack.pop();
        stack.pop();
        stack.pop();
        stack.pop();
        stack.pop();
    }

}