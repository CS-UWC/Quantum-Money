CREATE TABLE ledger (
    "serial" TEXT NOT NULL UNIQUE,
    "bits" TEXT NOT NULL,
    "bases" TEXT NOT NULL,
    "amount" TEXT NOT NULL,
    "lock" INTEGER DEFAULT 0,
    "attempts" INTEGER DEFAULT 0,
    PRIMARY KEY("serial")
);

CREATE TABLE user (
    "id" INTEGER NOT NULL UNIQUE,
    "firstname" TEXT NOT NULL,
    "surname" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE 'admin@quantumbank.com_wallet' (
    "serial" TEXT NOT NULL, 
    "state" TEXT NOT NULL, 
    "amount" INTEGER NOT NULL, 
    PRIMARY KEY("serial")
    )