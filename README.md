# DuckDB Demo — YZV 322E Applied Data Engineering

A working example for the Individual Tool Presentation assignment.  
**Tool:** DuckDB | **Student:** Venera Vangjeli | **ID:** 150240933 | **Date:** 1 May 2026

---

## 1. What is this tool?

DuckDB is an in-process, embeddable analytical SQL database engine. It runs entirely inside your application process — no server, no daemon, no network round-trip. It reads CSV, Parquet, and JSON files directly with full SQL support, columnar execution, and multi-core parallelism. It is often described as "SQLite for analytics."

---

## 2. Prerequisites

| Requirement | Version |
|---|---|
| OS | Linux, macOS, or Windows |
| Docker | 24.0 or later |
| Docker Compose | v2.20 or later |
| Python (optional, local run) | 3.9 or later |

To check your Docker version:

```bash
docker --version
docker compose version
```

---

## 3. Installation

### Option A — Docker (Recommended)

```bash
# 1. Clone this repository
git clone https://github.com/VeneraVangjeli/duckdb-demo.git
cd duckdb-demo

# 2. Copy the environment file
cp .env.example .env

# 3. Build and run the container
docker compose up --build
```

That is all. Docker installs Python, DuckDB, and all dependencies inside the container automatically.

### Option B — Local Python

```bash
# 1. Clone and enter the repository
git clone https://github.com/VeneraVangjeli/duckdb-demo.git
cd duckdb-demo

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the example
python example.py
```

---

## 4. Running the Example

```bash
docker compose up --build
```

The script will:
1. Generate a sample Parquet dataset (`data/trips.parquet`) if it does not exist
2. Run SQL analytics on the dataset using DuckDB
3. Print results to the terminal
4. Save the output to `output/result.csv`

---

## 5. Expected Output

```
Running DuckDB analytics on data/trips.parquet ...

   city     rides  avg_fare
0  Istanbul  48201     24.50
1  Ankara    31057     19.80
2  Izmir     22348     17.30

Results saved to output/result.csv
Done in 0.38s
```

You should see a DataFrame printed to the terminal and a `result.csv` file appear in the `output/` directory.

---

## 6. Repository Structure

```
duckdb-demo/
├── README.md             # This file
├── docker-compose.yml    # Container orchestration
├── Dockerfile            # Python + DuckDB environment
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
├── example.py            # Main analytics script
├── data/
│   └── trips.parquet     # Sample dataset (auto-generated)
├── output/               # Query results (generated at runtime)
└── ai_usage.md           # AI tool usage disclosure
```

---

## 7. AI Usage Disclosure

AI Tools like Gemini were used for learning more about the tool, assistance and structuring. All commands and code examples were tested manually.
