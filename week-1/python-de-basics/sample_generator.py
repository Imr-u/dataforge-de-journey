import csv
import random
from datetime import datetime, timedelta

merchants = [
  ("Amazon", "Shoping"),
  ("Starbucks", "Food & Drink"),
  ("Telebirr", "Transaction"),
  ("Netflix", "Entertainment"),
  ("Uber", "Transport"),
  ("Beu", "Food Delivery")
]

def generate_transactions(num_rows: int, filename: str):
  start_date = datetime(2024, 1, 1)

  with open (filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames = ["date", "amount", "merchant", "category"])
    writer.writeheader
    for i in range(num_rows):
      merchant, category = random.choice(merchants)
      row = {
        "date" : (start_date + timedelta(days = i)).strftime("%Y-%m-%d"),
        "amount" : round (random.uniform(5.00, 1500.00), 2),
        "merchant" : merchant,
        "category" : category
      }
      writer.writerow(row)
  print(f"generated {num_rows} rows into {filename}")

if __name__ == "__main__":
  generate_transactions(5, "sample.csv")
