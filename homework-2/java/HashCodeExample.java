public class HashCodeExample {
    public static void main (String[] args) {
        SimpleShoppingCart jasonsCart = new SimpleShoppingCart();
        jasonsCart.addToCart("Cheese", 5);
        jasonsCart.addToCart("Bread", 6);

        SimpleShoppingCart tanyasCart = new SimpleShoppingCart();
        tanyasCart.addToCart("Cheese", 6);
        tanyasCart.addToCart("Bread", 5);

        // Tanya and Jason's carts are not equal
        System.out.println("Tanya's Cart: " + tanyasCart.cart() + ", Jason's Cart: " + jasonsCart.cart());
        System.out.println("Are the carts the same?: " + jasonsCart.equals(tanyasCart));
        System.out.println("Are the HashCodes the same?: " + (jasonsCart.hashCode() == tanyasCart.hashCode()) + "\n");

        SimpleShoppingCart saadsCart = new SimpleShoppingCart();
        saadsCart.addToCart("Cheese", 5);
        saadsCart.addToCart("Bread", 6);

        // Saad's cart and Jason's cart are the same and should have the same hash code
        System.out.println("Saad's Cart: " + saadsCart.cart() + ", Jason's Cart: " + jasonsCart.cart());
        System.out.println("Are the carts the same?: " + jasonsCart.equals(saadsCart));
        System.out.println("Are the HashCodes the same?: " + (jasonsCart.hashCode() == saadsCart.hashCode()));
    }
}