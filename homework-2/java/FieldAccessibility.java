import java.util.*;

public class FieldAccessibility {
    public static void main(String[] args) {
        FieldAccessibilityCart tanyasCart = new FieldAccessibilityCart();
        tanyasCart.addToCart("Banana", 1.0);
        System.out.println("cart: " + tanyasCart.cart());
        System.out.println("price: " + tanyasCart.cartTotal() + "\n");

        tanyasCart.addToCart("Chicken", 10.0);
        System.out.println("cart: " + tanyasCart.cart());
        System.out.println("price: " + tanyasCart.cartTotal() + "\n");

        // Code that won't run due to private fields, keeping these
        // fields safe
        // try {
        //     tanyasCart.cartTotal = 4.0;
        // } catch(Exception e) {
        //     System.out.println("Cannot modify private variable");
        // }

        // try {
        //     tanyasCart.cart.remove("Banana");
        // } catch(Exception e) {
        //     System.out.println("Cannot modify private variable");
        // }

    }
}