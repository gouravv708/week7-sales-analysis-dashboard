import pandas as pd


class SalesAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

        # Calculate Final Amount after Discount
        self.df["Final_Amount"] = (
            self.df["Quantity"] *
            self.df["Price"] *
            (1 - self.df["Discount"] / 100)
        )

    # -------------------------
    # Basic Statistics
    # -------------------------

    def total_orders(self):
        return len(self.df)

    def total_revenue(self):
        return self.df["Final_Amount"].sum()

    def average_order_value(self):
        return self.df["Final_Amount"].mean()

    # -------------------------
    # Monthly Sales
    # -------------------------

    def monthly_sales(self):

        self.df["Month"] = self.df["Date"].dt.strftime("%b")

        return self.df.groupby("Month")["Final_Amount"].sum()

    # -------------------------
    # Top Products
    # -------------------------

    def top_products(self, n=5):

        return (
            self.df.groupby("Product")["Final_Amount"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

    # -------------------------
    # Category Sales
    # -------------------------

    def category_sales(self):

        return (
            self.df.groupby("Category")["Final_Amount"]
            .sum()
            .sort_values(ascending=False)
        )

    # -------------------------
    # City Sales
    # -------------------------

    def city_sales(self):

        return (
            self.df.groupby("City")["Final_Amount"]
            .sum()
            .sort_values(ascending=False)
        )

    # -------------------------
    # Customer Sales
    # -------------------------

    def top_customers(self, n=5):

        return (
            self.df.groupby("Customer_Name")["Final_Amount"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

    # -------------------------
    # Payment Mode
    # -------------------------

    def payment_analysis(self):

        return self.df["Payment_Mode"].value_counts()

    # -------------------------
    # Discount Analysis
    # -------------------------

    def average_discount(self):

        return self.df["Discount"].mean()

    # -------------------------
    # Summary
    # -------------------------
    def summary(self):

        print("=" * 50)
        print(" SALES ANALYSIS SUMMARY ")
        print("=" * 50)

        print(f"Total Orders         : {self.total_orders()}")
        print(f"Total Revenue        : ₹{self.total_revenue():,.2f}")
        print(f"Average Order Value  : ₹{self.average_order_value():,.2f}")
        print(f"Average Discount     : {self.average_discount():.2f}%")

        print("\nTop Products")
        for product, amount in self.top_products().items():
            print(f"{product:<20} ₹{amount:,.2f}")

        print("\nCategory Sales")
        for category, amount in self.category_sales().items():
            print(f"{category:<20} ₹{amount:,.2f}")

        print("\nCity Sales")
        for city, amount in self.city_sales().items():
            print(f"{city:<15} ₹{amount:,.2f}")

        print("\nTop Customers")
        for customer, amount in self.top_customers().items():
            print(f"{customer:<20} ₹{amount:,.2f}")

        print("\nPayment Mode")
        for mode, count in self.payment_analysis().items():
            print(f"{mode:<15} {count}")

        print("\nMonthly Sales")
        for month, amount in self.monthly_sales().items():
            print(f"{month:<10} ₹{amount:,.2f}")