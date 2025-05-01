import pandas as pd
import sqlite3
import sys
import os
import importlib.util

def load_schema(schema_path):
    spec = importlib.util.spec_from_file_location("schema_module", schema_path)
    schema_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(schema_module)
    return schema_module.schema

def main(schema_path, excel_path, sqlite_path):
    if not os.path.isfile(excel_path):
        print(f"Excel file not found: {excel_path}")
        return
    if not os.path.isfile(schema_path):
        print(f"Schema file not found: {schema_path}")
        return

    # Load external schema
    schema = load_schema(schema_path)

    # Read Excel file
    xls = pd.ExcelFile(excel_path)
    sheets = {name: xls.parse(name) for name in xls.sheet_names}

    # Create SQLite connection
    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    # Create tables
    for table_name, ddl in schema.items():
        cursor.execute(ddl)

    # Insert data from matching sheets
    for table, df in sheets.items():
        if table in schema:
            df.to_sql(table, conn, if_exists='append', index=False)

    conn.commit()
    conn.close()
    print(f"SQLite DB created at: {sqlite_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python excelToSqlite.py <schema.py> <excel file> <output sqlite file>")
    else:
        schema_path = sys.argv[1]
        excel_path = sys.argv[2]
        sqlite_path = sys.argv[3]
        main(schema_path, excel_path, sqlite_path)
