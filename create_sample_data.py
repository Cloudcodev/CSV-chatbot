import pandas as pd

def create_sample_data():
    """Generates a sample product catalog CSV for testing the chatbot."""
    
    data = {
        "product_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "product_name": [
            "Wireless bluetooth headphones", "USB-C charging cable", 
            "27-inch 4K monitor", "Mechanical gaming keyboard", 
            "Laptop stand (Aluminum)", "Portable hard drive 1TB",
            "Monitor light bar", "Wireless mouse", 
            "Smartphone screen protector", "HDMI 2.1 cable (8K)"
        ],
        "category": [
            "Audio", "Accessories", "Monitors", "Peripherals", 
            "Accessories", "Storage", "Lighting", "Peripherals", 
            "Protection", "Cables"
        ],
        "price_usd": [79.99, 12.99, 349.99, 149.99, 39.99, 59.99, 89.99, 29.99, 9.99, 24.99],
        "rating": [4.5, 4.8, 4.7, 4.6, 4.9, 4.4, 4.3, 4.7, 4.6, 4.8],
        "description": [
            "High-quality wireless headphones with noise cancellation. Great for music and calls.",
            "Durable USB-C cable for fast charging. 6ft length, supports 100W power.",
            "Beautiful 4K display with HDR support. Perfect for creative professionals.",
            "Mechanical switches with RGB lighting. Great for gaming and typing.",
            "Premium aluminum stand to elevate your laptop. Adjustable and portable.",
            "Fast external hard drive for backups. USB 3.1 connection.",
            "Desk lamp that attaches to your monitor. Reduces eye strain.",
            "Wireless mouse with silent clicks. Long battery life.",
            "Tempered glass protector for smartphone. Anti-fingerprint coating.",
            "Premium HDMI cable supporting 8K resolution. Future-proof your setup."
        ]
    }

    df = pd.DataFrame(data)
    csv_filename = "sample_products.csv"
    df.to_csv(csv_filename, index=False)

    print(f"Successfully created {csv_filename} ({len(df)} records).")
    print("\nData Preview:")
    print(df.head())

if __name__ == "__main__":
    create_sample_data()
