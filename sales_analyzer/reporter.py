import os


class ReportGenerator:

    def __init__(self, analyzer):
        self.analyzer = analyzer

        # Create reports folder if it doesn't exist
        os.makedirs("reports", exist_ok=True)

    def generate_summary(self):

        with open("reports/sales_summary.txt", "w", encoding="utf-8") as file:

            file.write("========== SALES ANALYSIS REPORT ==========\n\n")

            file.write(f"Total Orders        : {self.analyzer.total_orders()}\n")
            file.write(f"Total Revenue       : ₹{self.analyzer.total_revenue():,.2f}\n")
            file.write(f"Average Order Value : ₹{self.analyzer.average_order_value():,.2f}\n")
            file.write(f"Average Discount    : {self.analyzer.average_discount():.2f}%\n")

        print("✓ sales_summary.txt generated")

    def export_reports(self):

        self.analyzer.top_products().to_csv(
            "reports/top_products.csv",
            header=["Revenue"]
        )

        self.analyzer.monthly_sales().to_csv(
            "reports/monthly_sales.csv",
            header=["Revenue"]
        )

        self.analyzer.category_sales().to_csv(
            "reports/category_sales.csv",
            header=["Revenue"]
        )

        self.analyzer.city_sales().to_csv(
            "reports/city_sales.csv",
            header=["Revenue"]
        )

        self.analyzer.top_customers().to_csv(
            "reports/top_customers.csv",
            header=["Revenue"]
        )

        print("✓ CSV reports exported successfully")