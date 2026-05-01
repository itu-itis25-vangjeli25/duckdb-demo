"""
DuckDB Working Example — YZV 322E Applied Data Engineering
Venera Vangjeli | 150240933

This script:
  1. Generates a sample Parquet dataset of ride trips if it does not already exist.
  2. Queries it with DuckDB SQL (GROUP BY city, AVG fare, COUNT rides).
  3. Prints the resulting DataFrame to the terminal.
  4. Saves the output to output/result.csv.
"""

import os
import time

import duckdb
import pandas as pd

DATA_PATH = "data/trips.parquet"
OUTPUT_PATH = "output/result.csv"


def generate_sample_data(path: str) -> None:
    """Generate a small synthetic Parquet dataset if it does not exist."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    import random
    random.seed(42)

    cities = ["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya"]
    weights = [0.40, 0.25, 0.18, 0.10, 0.07]
    n = 120_000

    rows = {
        "trip_id": list(range(1, n + 1)),
        "city": random.choices(cities, weights=weights, k=n),
        "fare": [round(random.uniform(5.0, 60.0), 2) for _ in range(n)],
        "distance_km": [round(random.uniform(1.0, 30.0), 1) for _ in range(n)],
    }

    df = pd.DataFrame(rows)
    df.to_parquet(path, index=False)
    print(f"Sample dataset generated: {path} ({n:,} rows)\n")


def run_analytics(data_path: str, output_path: str) -> None:
    """Run SQL analytics with DuckDB and save results."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"Running DuckDB analytics on {data_path} ...\n")
    start = time.perf_counter()

    con = duckdb.connect("analytics.db")

    result: pd.DataFrame = con.execute(
        f"""
        SELECT
            city,
            COUNT(*)         AS rides,
            ROUND(AVG(fare), 2) AS avg_fare,
            ROUND(AVG(distance_km), 1) AS avg_distance_km
        FROM read_parquet('{data_path}')
        GROUP BY city
        ORDER BY rides DESC
        """
    ).df()

    elapsed = time.perf_counter() - start

    print(result.to_string(index=True))
    print()

    result.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")
    print(f"Done in {elapsed:.2f}s")

    con.close()


if __name__ == "__main__":
    if not os.path.exists(DATA_PATH):
        generate_sample_data(DATA_PATH)

    run_analytics(DATA_PATH, OUTPUT_PATH)
