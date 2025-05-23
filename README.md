# Reverse ATS - BETA

A beta prototype for a tool to organize track what roles you've applied to, the companies those roles belong to, and interviews related to the role, and relevant contacts for each company.

## Overview

[Previously](https://github.com/rustyrohbot/reverse-ats-alpha) I got a system working with an Excel workbook that had five sheets: Companies, Roles, Contacts, Interviews, and InterviewContacts.

Now we are taking that excel file and converting it to a SQLite database. We'll be using these CREATEs similar to these to build each table when we map the data over.

Companies Table

```sql
CREATE TABLE IF NOT EXISTS Companies (
    companyID INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    url TEXT,
    hqCity TEXT,
    hqState TEXT
);
```

Roles
```sql
CREATE TABLE IF NOT EXISTS Roles (
    roleID INTEGER PRIMARY KEY,
    companyID INTEGER,
    name TEXT,
    url TEXT,
    description TEXT,
    coverLetter TEXT,
    applicationLocation TEXT,
    appliedDate TEXT,
    closedDate TEXT,
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
```

Interviews
```sql
CREATE TABLE IF NOT EXISTS Interviews (
    interviewID INTEGER PRIMARY KEY,
    roleID INTEGER,
    date TEXT,
    start TEXT,
    end TEXT,
    notes TEXT,
    type TEXT,
    FOREIGN KEY (roleID) REFERENCES Roles(roleID)
);
```

Contacts
```sql
CREATE TABLE IF NOT EXISTS Contacts (
    contactID INTEGER PRIMARY KEY,
    companyID INTEGER,
    firstName TEXT,
    lastName TEXT,
    role TEXT,
    email TEXT,
    phone TEXT,
    linkedin TEXT,
    notes TEXT,
    FOREIGN KEY (companyID) REFERENCES Companies(companyID)
);
```

InterviewsContacts
```sql
CREATE TABLE IF NOT EXISTS InterviewsContacts (
    interviewsContactId INTEGER PRIMARY KEY,
    interviewId INTEGER,
    contactId INTEGER,
    FOREIGN KEY (interviewId) REFERENCES Interviews(interviewID),
    FOREIGN KEY (contactId) REFERENCES Contacts(contactID)
);
```


## Requirement

- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - pandas
  - openpyxl

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/rustyrohbot/reverse-ats-beta.git
   cd reverse-ats-beta
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script to generate the database:

```
python excelToSqlite.py <schema.py> <excel file> <output sqlite file>
```

For example, running

```
python excelToSqlite.py schema.py Reverse_ATS.xlsx database.sqlite
```

will produce a SQLite database nammed `database.sqlite` in the same folder you ran the script


## Privacy

The generated template contains entirely fictional company names, recruiter information, and job details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.