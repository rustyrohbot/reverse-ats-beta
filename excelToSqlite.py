# excelToSqlite.py

import pandas as pd
import sqlite3
import sys
import os

def main(excel_path, sqlite_path):
    if not os.path.isfile(excel_path):
        print(f"❌ File not found: {excel_path}")
        return

    # Load Excel file
    xls = pd.ExcelFile(excel_path)
    sheet_names = xls.sheet_names
    sheets = {name: xls.parse(name) for name in sheet_names}

    # SQLite schema definitions
    schema = {
        "Companies": """
            CREATE TABLE IF NOT EXISTS Companies (
                companyID INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                url TEXT,
                hqCity TEXT,
                hqState TEXT
            );
        """,
        "Roles": """
            CREATE TABLE IF NOT EXISTS Roles (
                roleID INTEGER PRIMARY KEY,
                companyID INTEGER NOT NULL,
                name TEXT NOT NULL,
                url TEXT,
                description TEXT,
                coverLetter TEXT,
                applied TEXT,
                appliedDate TEXT,
                postedRangeMin INTEGER,
                postedRangeMax INTEGER,
                equity BOOLEAN,
                workCity TEXT,
                workState TEXT,
                location TEXT,
                status TEXT,
                discovery TEXT,
                referral BOOLEAN,
                notes TEXT,
                FOREIGN KEY (companyID) REFERENCES Companies(companyID)
            );
        """,
        "Interviews": """
            CREATE TABLE IF NOT EXISTS Interviews (
                interviewID INTEGER PRIMARY KEY,
                roleID INTEGER NOT NULL,
                date TEXT,
                start TEXT,
                end TEXT,
                notes TEXT,
                type TEXT,
                FOREIGN KEY (roleID) REFERENCES Roles(roleID)
            );
        """,
        "Contacts": """
            CREATE TABLE IF NOT EXISTS Contacts (
                contactID INTEGER PRIMARY KEY,
                companyID INTEGER NOT NULL,
                firstName TEXT,
                lastName TEXT,
                role TEXT,
                email TEXT,
                phone TEXT,
                linkedin TEXT,
                notes TEXT,
                FOREIGN KEY (companyID) REFERENCES Companies(companyID)
            );
        """,
        "InterviewsContacts": """
            CREATE TABLE IF NOT EXISTS InterviewsContacts (
                interviewContactId INTEGER PRIMARY KEY,
                interviewId INTEGER NOT NULL,
                contactId INTEGER NOT NULL,
                FOREIGN KEY (interviewId) REFERENCES Interviews(interviewID),
                FOREIGN KEY (contactId) REFERENCES Contacts(contactID)
            );
        """
    }

    # Connect to SQLite DB
    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    # Create tables
    for table, ddl in schema.items():
        cursor.execute(ddl)

    conn.commit()

    # Insert data
    for table, df in sheets.items():
        df.to_sql(table, conn, if_exists='append', index=False)

    conn.close()
    print(f"✅ Successfully created SQLite DB at {sqlite_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python excelToSqlite.py <excel file> <output sqlite file>")
    else:
        excel_path = sys.argv[1]
        sqlite_path = sys.argv[2]
        main(excel_path, sqlite_path)
