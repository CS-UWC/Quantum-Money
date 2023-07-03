CREATE TABLE ledger (
    "serialno" TEXT NOT NULL UNIQUE,
    "bits" TEXT NOT NULL,
    "bases" TEXT NOT NULL,
    "amount" TEXT NOT NULL,
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