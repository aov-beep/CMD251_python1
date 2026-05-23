# CMD512 Lesson 7

A small Python lesson project that demonstrates connecting to a SQL Server database using `pyodbc` and loading credentials from a `.env` file.

## Files

- `start.py` - main script that reads database credentials from environment variables and queries the `Users` table.
- `.env.example` - example environment file with placeholder values.
- `requrements.txt` - Python dependencies for the project.
- `env/` - local Python virtual environment directory.

## Setup

1. Activate your virtual environment.
   - PowerShell: `env\Scripts\Activate.ps1`
   - Command Prompt: `env\Scripts\activate.bat`

2. Install dependencies.

   ```powershell
   python -m pip install -r requrements.txt
   ```

3. Copy `.env.example` to `.env` and update the values.

   ```powershell
   copy .env.example .env
   ```

4. Edit `.env` and set:
   - `SERVER`
   - `DATABASE`
   - `USERNAME`
   - `PASSWORD`

## Run

```powershell
python start.py
```

## Notes

- The script uses `ODBC Driver 17 for SQL Server`. Make sure that driver is installed on your machine.
- If you prefer Windows Authentication, update the connection string in `start.py` to include `Trusted_Connection=yes;` instead of `UID`/`PWD`.
