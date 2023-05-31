class NaNExample {
    public static void main(String[] args) {
        double isNaN = Math.log(-1.0); // ln(-1) is NaN
        if (Double.isNaN(isNaN)) {
            System.out.println("Not a number");
        }
        double notNaN = Math.log(1.0); // ln(1) is 0
        if (!Double.isNaN(notNaN)) {
            System.out.println("Is a number");
        }
    }
}