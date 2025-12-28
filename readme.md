# Automated SQL Pull

Automates the recurring task of running a stored SQL statement against a PostgreSQL database and exporting the result set to an Excel workbook. The repository is intentionally lightweight so it can be dropped into a Windows host, pointed at any Postgres instance, and scheduled through Task Scheduler.

## Project structure

| File | Purpose |
| --- | --- |
| `asps.py` | Core script that loads credentials, executes `asps.sql`, builds a Pandas DataFrame, and saves the file to the configured drop path. |
| `asps.sql` | Template SQL file that contains the query you want to automate. Edit this with any valid Postgres statement. |
| `asps.bat` | Sample Task Scheduler friendly batch file that activates your Python environment and runs `asps.py`. |

## Requirements

- Python 3.9+
- Packages: `psycopg2` (or `psycopg2-binary`), `pandas`, `sqlalchemy`, `openpyxl`
- Access to the destination PostgreSQL instance and file share where the Excel file will land

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install pandas psycopg2-binary sqlalchemy openpyxl
```

## Configuration

Open `asps.py` and update the placeholders that are flagged near the top of the file:

- `host`, `database`, `port`, `user`, `password` – point these at your Postgres server.
- `cfile` – path to a two-line text file that stores the username on line 1 and password on line 2, e.g.:

  ```
  reporting_user
  supersecretpassword
  ```

- `query_path` – relative or absolute path to the SQL file you want to run (defaults to `asps.sql`).
- `filename` – output Excel file name (use an `.xlsx` extension).
- `drop_path` – folder that will receive the export; `drop_file` is automatically derived.

You can keep multiple SQL templates under version control and point `query_path` to the one you need before running the script.

## Usage

```bash
python asps.py
```

The script will log into Postgres, run the SQL found in `query_path`, and write the results to the Excel file configured via `drop_file`. Success or failure, together with the runtime, is written to stdout.

### Scheduling on Windows

Use `asps.bat` as a starting point:

1. Replace the `@CALL` line with the path to the `activate.bat` for the environment that contains your dependencies.
2. Replace the final `python` command with the path to `asps.py`.
3. Point a Task Scheduler job at the batch file and configure the trigger that matches your reporting cadence.

## Troubleshooting

- **Authentication errors** usually mean the credentials file cannot be located or the username/password in that file are stale.
- **Missing columns in the Excel export** indicate the SQL query did not alias fields the way you expect; inspect `asps.sql` and rerun locally before automating.
