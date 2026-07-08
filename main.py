from sales_analyzer.data_loader import DataLoader
from sales_analyzer.data_cleaner import DataCleaner
from sales_analyzer.analyzer import SalesAnalyzer
from sales_analyzer.visualizer import SalesVisualizer
from sales_analyzer.reporter import ReportGenerator


def main():

    # Load Data
    loader = DataLoader("data/raw/sales_data.csv")
    df = loader.load_data()

    # Clean Data
    cleaner = DataCleaner(df)
    df = cleaner.clean_data()
    df = cleaner.convert_date()

    # Analyze Data
    analyzer = SalesAnalyzer(df)

    analyzer.summary()

    # Create Charts
    visualizer = SalesVisualizer(analyzer)

    visualizer.monthly_sales_chart()
    visualizer.category_sales_chart()
    visualizer.top_products_chart()
    visualizer.city_sales_chart()
    visualizer.payment_mode_chart()

    # Generate Reports
    reporter = ReportGenerator(analyzer)

    reporter.generate_summary()
    reporter.export_reports()

    print("\nProject Completed Successfully!")
    print("Check the 'reports' folder for charts and reports.")


if __name__ == "__main__":
    main()