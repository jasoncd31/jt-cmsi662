

import java.util.*;
/**
 * Simple cart class only containing the  cart with its items mapped to prices and 
 * the cost of everything in the cart. 
 * Fields are private so no one can change the cart without
 * using methods. More importantly, the cartTotal can never be modified
 * by a user except by adding an removing items. This makes it
 * secure to prevent any code that could change totals to be
 * smaller and have everything cost less for the customer.
 */
public class FieldAccessibilityCart {
    private Map<String, Double> cart;
    private double cartTotal;

    public FieldAccessibilityCart() {
        this.cart = new HashMap<>();
        this.cartTotal = 0.0;
    }

    public void addToCart(String item, double price) {
        this.cart.put(item, price);
        this.cartTotal += price;
    }

    public boolean removeFromCart(String item) {
        if (this.cart.containsKey(item)) {
            this.cartTotal -= this.cart.get(item);
            this.cart.remove(item);
            return true;
        }
        return false;
    }

    public Map<String, Double> cart() {
        return this.cart;
    }

    public double cartTotal() {
        return this.cartTotal;
    }

   
}
