import os
import matplotlib.pyplot as plt


class SalesVisualizer:

    def __init__(self, analyzer):
        self.analyzer = analyzer

        # Create reports folder if it doesn't exist
        os.makedirs("reports", exist_ok=True)

    # -------------------------
    # Monthly Sales Line Chart
    # -------------------------

    def monthly_sales_chart(self):

        data = self.analyzer.monthly_sales()

        plt.figure(figsize=(8, 5))
        plt.plot(data.index, data.values, marker="o")
        plt.title("Monthly Sales")
        plt.xlabel("Month")
        plt.ylabel("Revenue (₹)")
        plt.grid(True)

        plt.tight_layout()
        plt.savefig("reports/monthly_sales.png")
        plt.close()

    # -------------------------
    # Category Sales Bar Chart
    # -------------------------

    def category_sales_chart(self):

        data = self.analyzer.category_sales()

        plt.figure(figsize=(8, 5))
        plt.bar(data.index, data.values)

        plt.title("Category Sales")
        plt.xlabel("Category")
        plt.ylabel("Revenue (₹)")

        plt.xticks(rotation=20)

        plt.tight_layout()
        plt.savefig("reports/category_sales.png")
        plt.close()

    # -------------------------
    # Payment Mode Pie Chart
    # -------------------------

    def payment_mode_chart(self):

        data = self.analyzer.payment_analysis()

        plt.figure(figsize=(6, 6))

        plt.pie(
            data.values,
            labels=data.index,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Payment Mode Distribution")

        plt.tight_layout()
        plt.savefig("reports/payment_mode.png")
        plt.close()

    # -------------------------
    # Top Products Bar Chart
    # -------------------------

    def top_products_chart(self):

        data = self.analyzer.top_products()

        plt.figure(figsize=(8, 5))

        plt.bar(data.index, data.values)

        plt.title("Top Products")
        plt.xlabel("Product")
        plt.ylabel("Revenue (₹)")

        plt.xticks(rotation=25)

        plt.tight_layout()
        plt.savefig("reports/top_products.png")
        plt.close()

    # -------------------------
    # City Sales Bar Chart
    # -------------------------

    def city_sales_chart(self):

        data = self.analyzer.city_sales()

        plt.figure(figsize=(9, 5))

        plt.bar(data.index, data.values)

        plt.title("City Wise Sales")
        plt.xlabel("City")
        plt.ylabel("Revenue (₹)")

        plt.xticks(rotation=25)

        plt.tight_layout()
        plt.savefig("reports/city_sales.png")
        plt.close()

    # -------------------------
    # Generate All Charts
    # -------------------------

    def generate_all_charts(self):

        self.monthly_sales_chart()
        self.category_sales_chart()
        self.payment_mode_chart()
        self.top_products_chart()
        self.city_sales_chart()

        print("\nAll charts saved successfully inside 'reports/' folder.")