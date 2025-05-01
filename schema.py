schema = {
    "Companies": """
        CREATE TABLE IF NOT EXISTS Companies (
            companyID INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            url TEXT,
            hqCity TEXT,
            hqState TEXT
        );
    """,
    "Roles": """
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
            notes TEXT
        );
    """,
    "Interviews": """
        CREATE TABLE IF NOT EXISTS Interviews (
            interviewID INTEGER PRIMARY KEY,
            roleID INTEGER,
            date TEXT,
            start TEXT,
            end TEXT,
            notes TEXT,
            type TEXT
        );
    """,
    "Contacts": """
        CREATE TABLE IF NOT EXISTS Contacts (
            contactID INTEGER PRIMARY KEY,
            companyID INTEGER,
            firstName TEXT,
            lastName TEXT,
            role TEXT,
            email TEXT,
            phone TEXT,
            linkedin TEXT,
            notes TEXT
        );
    """,
    "InterviewsContacts": """
        CREATE TABLE IF NOT EXISTS InterviewsContacts (
            interviewsContactId INTEGER PRIMARY KEY,
            interviewId INTEGER,
            contactId INTEGER
        );
    """
}
