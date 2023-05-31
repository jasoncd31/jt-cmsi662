public class FieldAccessibilityExample {
    public static void main(String[] args) {
        SimpleShoppingCart tanyasCart = new SimpleShoppingCart();
        tanyasCart.addToCart("Banana", 1.0);
        System.out.println("cart: " + tanyasCart.cart());
        System.out.println("price: " + tanyasCart.cartTotal() + "\n");

        tanyasCart.addToCart("Chicken", 10.0);
        System.out.println("cart: " + tanyasCart.cart());
        System.out.println("price: " + tanyasCart.cartTotal() + "\n");

        // Code that won't run due to private fields, keeping these
        // fields safe
        // tanyasCart.cartTotal = 4.0;
        // tanyasCart.cart.remove("Banana");


    }
}