-- Generated by Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   at:        2025-03-30 23:28:13 EDT
--   site:      Oracle Database 21c
--   type:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE AYT_AUTHOR 
    ( 
     AUTH_ID    NUMBER (5)  NOT NULL , 
     FNAME      VARCHAR2 (30)  NOT NULL , 
     MNAME      VARCHAR2 (10) , 
     LNAME      VARCHAR2 (30) , 
     ADDR_ST    VARCHAR2 (100) , 
     ADDR_CITY  VARCHAR2 (100) , 
     ADDR_STATE VARCHAR2 (100) , 
     ADDR_CTRY  VARCHAR2 (100) , 
     EMAIL      VARCHAR2 (254) 
    ) 
;

COMMENT ON COLUMN AYT_AUTHOR.AUTH_ID IS 'Unique Identifier for the Author' 
;

COMMENT ON COLUMN AYT_AUTHOR.FNAME IS 'First Name of the Author' 
;

COMMENT ON COLUMN AYT_AUTHOR.MNAME IS 'Middle Initials of the Author' 
;

COMMENT ON COLUMN AYT_AUTHOR.LNAME IS 'Last Name of the Author' 
;

COMMENT ON COLUMN AYT_AUTHOR.ADDR_ST IS 'Mailing Address of the Author' 
;

COMMENT ON COLUMN AYT_AUTHOR.ADDR_CITY IS 'Mailing City of the author' 
;

COMMENT ON COLUMN AYT_AUTHOR.ADDR_STATE IS 'Mailing State of the author' 
;

COMMENT ON COLUMN AYT_AUTHOR.ADDR_CTRY IS 'Mailing Country of the Author' 
;

COMMENT ON COLUMN AYT_AUTHOR.EMAIL IS 'Email of the Author' 
;

ALTER TABLE AYT_AUTHOR 
    ADD CONSTRAINT AYT_AUTHOR_PK PRIMARY KEY ( AUTH_ID ) ;

CREATE TABLE AYT_AUTHOR_SEMINAR 
    ( 
     INVITATION_ID NUMBER (10)  NOT NULL , 
     AUTH_ID       NUMBER (5)  NOT NULL , 
     EVENT_ID      NUMBER (10)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_AUTHOR_SEMINAR.INVITATION_ID IS 'Invitation ID for the Seminar' 
;

ALTER TABLE AYT_AUTHOR_SEMINAR 
    ADD CONSTRAINT AYT_AUTHOR_SEMINAR_PK PRIMARY KEY ( INVITATION_ID ) ;

CREATE TABLE AYT_BOOK 
    ( 
     BOOK_ID  NUMBER (7)  NOT NULL , 
     ISBN     VARCHAR2 (13)  NOT NULL , 
     NAME     VARCHAR2 (200)  NOT NULL , 
     TOPIC    VARCHAR2 (50)  NOT NULL , 
     PUB_DATE DATE  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_BOOK.BOOK_ID IS 'Unique Identifier of the book' 
;

COMMENT ON COLUMN AYT_BOOK.ISBN IS 'ISBN Number of the Book' 
;

COMMENT ON COLUMN AYT_BOOK.NAME IS 'Name of the Book' 
;

COMMENT ON COLUMN AYT_BOOK.TOPIC IS 'Topic the book falls under' 
;

COMMENT ON COLUMN AYT_BOOK.PUB_DATE IS 'Date the Book was published' 
;

ALTER TABLE AYT_BOOK 
    ADD CONSTRAINT AYT_BOOK_PK PRIMARY KEY ( BOOK_ID ) ;

CREATE TABLE AYT_BOOK_AUTHOR 
    ( 
     AUTH_ID NUMBER (5)  NOT NULL , 
     BOOK_ID NUMBER (7)  NOT NULL 
    ) 
;

ALTER TABLE AYT_BOOK_AUTHOR 
    ADD CONSTRAINT AYT_BOOK_AUTHOR_PK PRIMARY KEY ( BOOK_ID, AUTH_ID ) ;

CREATE TABLE AYT_BOOK_COPY 
    ( 
     COPY_ID NUMBER (8)  NOT NULL , 
     BOOK_ID NUMBER (7)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_BOOK_COPY.COPY_ID IS 'Unique Identifier for Copy of the Book' 
;

ALTER TABLE AYT_BOOK_COPY 
    ADD CONSTRAINT AYT_BOOK_COPY_PK PRIMARY KEY ( COPY_ID ) ;

CREATE TABLE AYT_CUST 
    ( 
     CUST_ID INTEGER  NOT NULL , 
     FNAME   VARCHAR2 (30)  NOT NULL , 
     LNAME   VARCHAR2 (30)  NOT NULL , 
     PHONE   VARCHAR2 (10)  NOT NULL , 
     EMAIL   VARCHAR2 (254)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_CUST.CUST_ID IS 'Unique Identifier of Customer' 
;

COMMENT ON COLUMN AYT_CUST.FNAME IS 'First Name of the Customer' 
;

COMMENT ON COLUMN AYT_CUST.LNAME IS 'Last Name of the Customer' 
;

COMMENT ON COLUMN AYT_CUST.PHONE IS 'Phone Number of the Customer' 
;

COMMENT ON COLUMN AYT_CUST.EMAIL IS 'Email of the customer' 
;

ALTER TABLE AYT_CUST 
    ADD CONSTRAINT AYT_CUST_PK PRIMARY KEY ( CUST_ID ) ;

CREATE TABLE AYT_CUST_EXHIBITION 
    ( 
     REG_ID   NUMBER (10)  NOT NULL , 
     EVENT_ID NUMBER (10)  NOT NULL , 
     CUST_ID  INTEGER  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_CUST_EXHIBITION.REG_ID IS 'Registration ID of the exhibition' 
;

ALTER TABLE AYT_CUST_EXHIBITION 
    ADD CONSTRAINT AYT_CUST_EXHIBITION_PK PRIMARY KEY ( REG_ID ) ;

CREATE TABLE AYT_CUST_ID 
    ( 
     ID_NUM  VARCHAR2 (10)  NOT NULL , 
     CUST_ID INTEGER  NOT NULL , 
     ID_TYPE VARCHAR2 (10)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_CUST_ID.ID_NUM IS 'Identification Number of the Customer for a Particular Identification Type' 
;

ALTER TABLE AYT_CUST_ID 
    ADD CONSTRAINT AYT_CUST_ID_PK PRIMARY KEY ( ID_NUM, ID_TYPE, CUST_ID ) ;

CREATE TABLE AYT_CUST_ROOM 
    ( 
     RES_ID     INTEGER  NOT NULL , 
     START_TIME TIMESTAMP (0)  NOT NULL , 
     END_TIME   TIMESTAMP (0)  NOT NULL , 
     DESCR      VARCHAR2 (100)  NOT NULL , 
     NUM_INDV   NUMBER (1)  NOT NULL , 
     CUST_ID    INTEGER  NOT NULL , 
     ROOM_ID    VARCHAR2 (4)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_CUST_ROOM.RES_ID IS 'Unique Identifier of the Reservation.' 
;

COMMENT ON COLUMN AYT_CUST_ROOM.START_TIME IS 'Start Time of the Reservation' 
;

COMMENT ON COLUMN AYT_CUST_ROOM.END_TIME IS 'End Time of the Reservation' 
;

COMMENT ON COLUMN AYT_CUST_ROOM.DESCR IS 'Short Description of why the reservation is needed' 
;

COMMENT ON COLUMN AYT_CUST_ROOM.NUM_INDV IS 'Expected number of Individuals that will be in the room during the reservation.' 
;

ALTER TABLE AYT_CUST_ROOM 
    ADD CONSTRAINT AYT_CUST_ROOM_PK PRIMARY KEY ( RES_ID ) ;

CREATE TABLE AYT_EVENT 
    ( 
     EVENT_ID        NUMBER (10)  NOT NULL , 
     EVENT_NAME      VARCHAR2 (100)  NOT NULL , 
     START_DATE_TIME DATE  NOT NULL , 
     END_DATE_TIME   DATE  NOT NULL , 
     EVENT_TOPIC     VARCHAR2 (30)  NOT NULL , 
     EVENT_TYPE      VARCHAR2 (1)  NOT NULL 
    ) 
;

ALTER TABLE AYT_EVENT 
    ADD CONSTRAINT CH_INH_AYT_EVENT 
    CHECK (EVENT_TYPE IN ('E', 'S')) 
;

COMMENT ON COLUMN AYT_EVENT.EVENT_ID IS 'Unique Identifier of the Event' 
;

COMMENT ON COLUMN AYT_EVENT.EVENT_NAME IS 'Name of the event' 
;

COMMENT ON COLUMN AYT_EVENT.START_DATE_TIME IS 'Start Date Time of the Event' 
;

COMMENT ON COLUMN AYT_EVENT.END_DATE_TIME IS 'End Date time of the event' 
;

COMMENT ON COLUMN AYT_EVENT.EVENT_TOPIC IS 'Topic of the Event' 
;

COMMENT ON COLUMN AYT_EVENT.EVENT_TYPE IS 'General Discriminator of the event' 
;

ALTER TABLE AYT_EVENT 
    ADD CONSTRAINT AYT_EVENT_PK PRIMARY KEY ( EVENT_ID ) ;

CREATE TABLE AYT_EXHIBITION 
    ( 
     EVENT_ID NUMBER (10)  NOT NULL , 
     EXPENSES NUMBER (9,2)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_EXHIBITION.EVENT_ID IS 'Unique Identifier of the Event' 
;

COMMENT ON COLUMN AYT_EXHIBITION.EXPENSES IS 'Total Expense spend in the Seminar' 
;

ALTER TABLE AYT_EXHIBITION 
    ADD CONSTRAINT AYT_EXHIBITION_PK PRIMARY KEY ( EVENT_ID ) ;

CREATE TABLE AYT_ID 
    ( 
     ID_TYPE VARCHAR2 (10)  NOT NULL , 
     ID_NAME VARCHAR2 (30)  NOT NULL , 
     DESCR   VARCHAR2 (200)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_ID.ID_TYPE IS 'Unique Identifier for the Identification Types' 
;

COMMENT ON COLUMN AYT_ID.ID_NAME IS 'Name of the Identification Types' 
;

COMMENT ON COLUMN AYT_ID.DESCR IS 'Description of the Identification Type' 
;

ALTER TABLE AYT_ID 
    ADD CONSTRAINT AYT_ID_PK PRIMARY KEY ( ID_TYPE ) ;

CREATE TABLE AYT_INVOICE 
    ( 
     INVOICE_ID   NUMBER (8)  NOT NULL , 
     INVOICE_DATE DATE  NOT NULL , 
     TOTAL_AMOUNT NUMBER (6,2)  NOT NULL , 
     RENTAL_ID    NUMBER (10)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_INVOICE.INVOICE_ID IS 'Unique Identifer of the Invoice' 
;

COMMENT ON COLUMN AYT_INVOICE.INVOICE_DATE IS 'Date the Invoice was generated' 
;

COMMENT ON COLUMN AYT_INVOICE.TOTAL_AMOUNT IS 'Total Due Amount for the invoice' 
;
CREATE UNIQUE INDEX AYT_INVOICE__IDX ON AYT_INVOICE 
    ( 
     RENTAL_ID ASC 
    ) 
;

ALTER TABLE AYT_INVOICE 
    ADD CONSTRAINT AYT_INVOICE_PK PRIMARY KEY ( INVOICE_ID ) ;

CREATE TABLE AYT_PAY 
    ( 
     PAY_ID     NUMBER (10)  NOT NULL , 
     DATE_TIME  DATE  NOT NULL , 
     AMOUNT     NUMBER (6,2)  NOT NULL , 
     INVOICE_ID NUMBER (10)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_PAY.PAY_ID IS 'Unique Identifier for Payment' 
;

COMMENT ON COLUMN AYT_PAY.DATE_TIME IS 'The datetime of the payment' 
;

COMMENT ON COLUMN AYT_PAY.AMOUNT IS 'Amount Paid' 
;

ALTER TABLE AYT_PAY 
    ADD CONSTRAINT AYT_PAY_PK PRIMARY KEY ( PAY_ID ) ;

CREATE TABLE AYT_PAY_TYPE 
    ( 
     TYPE_ID   NUMBER (1)  NOT NULL , 
     TYPE_NAME VARCHAR2 (20)  NOT NULL , 
     DESCR     VARCHAR2 (200) 
    ) 
;

COMMENT ON COLUMN AYT_PAY_TYPE.TYPE_ID IS 'Unique Identifier of the Payment Type' 
;

COMMENT ON COLUMN AYT_PAY_TYPE.TYPE_NAME IS 'Name of the Payment Type. Is it credit card, debit card, etc.' 
;

COMMENT ON COLUMN AYT_PAY_TYPE.DESCR IS 'Description of the Payment Type' 
;

ALTER TABLE AYT_PAY_TYPE 
    ADD CONSTRAINT AYT_PAY_TYPE_PK PRIMARY KEY ( TYPE_ID ) ;

CREATE TABLE AYT_RENTAL 
    ( 
     RENTAL_ID     NUMBER (10)  NOT NULL , 
     BORROW_DATE   DATE  NOT NULL , 
     EXPECTED_DATE DATE  NOT NULL , 
     ACTUAL_DATE   DATE , 
     CUST_ID       INTEGER  NOT NULL , 
     COPY_ID       NUMBER (8)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_RENTAL.RENTAL_ID IS 'Unique Identifier for Rental' 
;

COMMENT ON COLUMN AYT_RENTAL.BORROW_DATE IS 'Borrow Date of the Book Rental' 
;

COMMENT ON COLUMN AYT_RENTAL.EXPECTED_DATE IS 'Expected date the book is to be returned' 
;

COMMENT ON COLUMN AYT_RENTAL.ACTUAL_DATE IS 'Actual Date when the book was returned' 
;

ALTER TABLE AYT_RENTAL 
    ADD CONSTRAINT AYT_RENTAL_PK PRIMARY KEY ( RENTAL_ID ) ;

CREATE TABLE AYT_ROOM 
    ( 
     ROOM_ID  VARCHAR2 (4)  NOT NULL , 
     CAPACITY NUMBER (1)  NOT NULL , 
     DESCR    VARCHAR2 (100)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_ROOM.ROOM_ID IS 'Unique Identifier of the Room. The ID shows which floor the room is on' 
;

COMMENT ON COLUMN AYT_ROOM.CAPACITY IS 'Capacity of the Room. Max Room capacity assumed to be 9' 
;

COMMENT ON COLUMN AYT_ROOM.DESCR IS 'Brief Description of the room' 
;

ALTER TABLE AYT_ROOM 
    ADD CONSTRAINT AYT_ROOM_PK PRIMARY KEY ( ROOM_ID ) ;

CREATE TABLE AYT_SEMINAR 
    ( 
     EVENT_ID        NUMBER (10)  NOT NULL , 
     KEYNOTE_SPEAKER VARCHAR2 (100) , 
     SEMINAR_TYPE    VARCHAR2 (20)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_SEMINAR.EVENT_ID IS 'Unique Identifier of the Event' 
;

COMMENT ON COLUMN AYT_SEMINAR.KEYNOTE_SPEAKER IS 'Name of the Keynote Speaker' 
;

COMMENT ON COLUMN AYT_SEMINAR.SEMINAR_TYPE IS 'What Type of Seminar is being hosted' 
;

ALTER TABLE AYT_SEMINAR 
    ADD CONSTRAINT AYT_SEMINAR_PK PRIMARY KEY ( EVENT_ID ) ;

CREATE TABLE AYT_SPONSOR 
    ( 
     SPONSOR_ID NUMBER (5)  NOT NULL , 
     FNAME      VARCHAR2 (100)  NOT NULL , 
     LNAME      VARCHAR2 (30) , 
     EMAIL      VARCHAR2 (254)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_SPONSOR.SPONSOR_ID IS 'Unique Identifier of Sponsor' 
;

COMMENT ON COLUMN AYT_SPONSOR.FNAME IS 'First Name of the Sponsor. If the sponsor is an organization, full name of the organization' 
;

COMMENT ON COLUMN AYT_SPONSOR.LNAME IS 'Last name of the sponsor. Empty if sponsor is an organization' 
;

COMMENT ON COLUMN AYT_SPONSOR.EMAIL IS 'Email of the sponsor' 
;

ALTER TABLE AYT_SPONSOR 
    ADD CONSTRAINT AYT_SPONSOR_PK PRIMARY KEY ( SPONSOR_ID ) ;

CREATE TABLE AYT_SPONSOR_SEMINAR 
    ( 
     AMOUNT     NUMBER (10,2)  NOT NULL , 
     EVENT_ID   NUMBER (10)  NOT NULL , 
     SPONSOR_ID NUMBER (5)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_SPONSOR_SEMINAR.AMOUNT IS 'Amount Given by the sponsor for the seminar' 
;

ALTER TABLE AYT_SPONSOR_SEMINAR 
    ADD CONSTRAINT AYT_SPONSOR_SEMINAR_PK PRIMARY KEY ( EVENT_ID, SPONSOR_ID ) ;

CREATE TABLE AYT_TYPE_PAY 
    ( 
     INST_NUM  NUMBER (10)  NOT NULL , 
     CARD_NAME VARCHAR2 (100) , 
     PAY_ID    NUMBER (10)  NOT NULL , 
     TYPE_ID   NUMBER (1)  NOT NULL 
    ) 
;

COMMENT ON COLUMN AYT_TYPE_PAY.INST_NUM IS 'Instrumentation Number. If payment is done by cash, then INST_NUM will be 0.' 
;

COMMENT ON COLUMN AYT_TYPE_PAY.CARD_NAME IS 'Name in the Card. Optional since people can pay using cash' 
;

ALTER TABLE AYT_TYPE_PAY 
    ADD CONSTRAINT AYT_TYPE_PAY_PK PRIMARY KEY ( PAY_ID, TYPE_ID ) ;

ALTER TABLE AYT_AUTHOR_SEMINAR 
    ADD CONSTRAINT AYT_AUT_SEM_AYT_AUT_FK FOREIGN KEY 
    ( 
     AUTH_ID
    ) 
    REFERENCES AYT_AUTHOR 
    ( 
     AUTH_ID
    ) 
;

ALTER TABLE AYT_AUTHOR_SEMINAR 
    ADD CONSTRAINT AYT_AUT_SEM_AYT_SEM_FK FOREIGN KEY 
    ( 
     EVENT_ID
    ) 
    REFERENCES AYT_SEMINAR 
    ( 
     EVENT_ID
    ) 
;

ALTER TABLE AYT_BOOK_AUTHOR 
    ADD CONSTRAINT AYT_BOOK_AUTHOR_AYT_AUTHOR_FK FOREIGN KEY 
    ( 
     AUTH_ID
    ) 
    REFERENCES AYT_AUTHOR 
    ( 
     AUTH_ID
    ) 
;

ALTER TABLE AYT_BOOK_AUTHOR 
    ADD CONSTRAINT AYT_BOOK_AUTHOR_AYT_BOOK_FK FOREIGN KEY 
    ( 
     BOOK_ID
    ) 
    REFERENCES AYT_BOOK 
    ( 
     BOOK_ID
    ) 
;

ALTER TABLE AYT_BOOK_COPY 
    ADD CONSTRAINT AYT_BOOK_COPY_AYT_BOOK_FK FOREIGN KEY 
    ( 
     BOOK_ID
    ) 
    REFERENCES AYT_BOOK 
    ( 
     BOOK_ID
    ) 
;

ALTER TABLE AYT_CUST_EXHIBITION 
    ADD CONSTRAINT AYT_CUST_EX_AYT_CUST_FK FOREIGN KEY 
    ( 
     CUST_ID
    ) 
    REFERENCES AYT_CUST 
    ( 
     CUST_ID
    ) 
;

ALTER TABLE AYT_CUST_EXHIBITION 
    ADD CONSTRAINT AYT_CUST_EX_AYT_EX_FK FOREIGN KEY 
    ( 
     EVENT_ID
    ) 
    REFERENCES AYT_EXHIBITION 
    ( 
     EVENT_ID
    ) 
;

ALTER TABLE AYT_CUST_ID 
    ADD CONSTRAINT AYT_CUST_ID_AYT_CUST_FK FOREIGN KEY 
    ( 
     CUST_ID
    ) 
    REFERENCES AYT_CUST 
    ( 
     CUST_ID
    ) 
;

ALTER TABLE AYT_CUST_ID 
    ADD CONSTRAINT AYT_CUST_ID_AYT_ID_FK FOREIGN KEY 
    ( 
     ID_TYPE
    ) 
    REFERENCES AYT_ID 
    ( 
     ID_TYPE
    ) 
;

ALTER TABLE AYT_CUST_ROOM 
    ADD CONSTRAINT AYT_CUST_ROOM_AYT_CUST_FK FOREIGN KEY 
    ( 
     CUST_ID
    ) 
    REFERENCES AYT_CUST 
    ( 
     CUST_ID
    ) 
;

ALTER TABLE AYT_CUST_ROOM 
    ADD CONSTRAINT AYT_CUST_ROOM_AYT_ROOM_FK FOREIGN KEY 
    ( 
     ROOM_ID
    ) 
    REFERENCES AYT_ROOM 
    ( 
     ROOM_ID
    ) 
;

ALTER TABLE AYT_EXHIBITION 
    ADD CONSTRAINT AYT_EXHIBITION_AYT_EVENT_FK FOREIGN KEY 
    ( 
     EVENT_ID
    ) 
    REFERENCES AYT_EVENT 
    ( 
     EVENT_ID
    ) 
;

ALTER TABLE AYT_INVOICE 
    ADD CONSTRAINT AYT_INVOICE_AYT_RENTAL_FK FOREIGN KEY 
    ( 
     RENTAL_ID
    ) 
    REFERENCES AYT_RENTAL 
    ( 
     RENTAL_ID
    ) 
;

ALTER TABLE AYT_PAY 
    ADD CONSTRAINT AYT_PAY_AYT_INVOICE_FK FOREIGN KEY 
    ( 
     INVOICE_ID
    ) 
    REFERENCES AYT_INVOICE 
    ( 
     INVOICE_ID
    ) 
;

ALTER TABLE AYT_RENTAL 
    ADD CONSTRAINT AYT_RENTAL_AYT_BOOK_COPY_FK FOREIGN KEY 
    ( 
     COPY_ID
    ) 
    REFERENCES AYT_BOOK_COPY 
    ( 
     COPY_ID
    ) 
;

ALTER TABLE AYT_RENTAL 
    ADD CONSTRAINT AYT_RENTAL_AYT_CUST_FK FOREIGN KEY 
    ( 
     CUST_ID
    ) 
    REFERENCES AYT_CUST 
    ( 
     CUST_ID
    ) 
;

ALTER TABLE AYT_SEMINAR 
    ADD CONSTRAINT AYT_SEMINAR_AYT_EVENT_FK FOREIGN KEY 
    ( 
     EVENT_ID
    ) 
    REFERENCES AYT_EVENT 
    ( 
     EVENT_ID
    ) 
;

ALTER TABLE AYT_SPONSOR_SEMINAR 
    ADD CONSTRAINT AYT_SP_SEM_AYT_SEM_FK FOREIGN KEY 
    ( 
     EVENT_ID
    ) 
    REFERENCES AYT_SEMINAR 
    ( 
     EVENT_ID
    ) 
;

ALTER TABLE AYT_SPONSOR_SEMINAR 
    ADD CONSTRAINT AYT_SP_SEM_AYT_SP_FK FOREIGN KEY 
    ( 
     SPONSOR_ID
    ) 
    REFERENCES AYT_SPONSOR 
    ( 
     SPONSOR_ID
    ) 
;

ALTER TABLE AYT_TYPE_PAY 
    ADD CONSTRAINT AYT_TYPE_PAY_AYT_PAY_FK FOREIGN KEY 
    ( 
     PAY_ID
    ) 
    REFERENCES AYT_PAY 
    ( 
     PAY_ID
    ) 
;

ALTER TABLE AYT_TYPE_PAY 
    ADD CONSTRAINT AYT_TYPE_PAY_AYT_PAY_TYPE_FK FOREIGN KEY 
    ( 
     TYPE_ID
    ) 
    REFERENCES AYT_PAY_TYPE 
    ( 
     TYPE_ID
    ) 
;

CREATE OR REPLACE TRIGGER ARC_FKArc_3_AYT_SEMINAR 
BEFORE INSERT OR UPDATE OF EVENT_ID 
ON AYT_SEMINAR 
FOR EACH ROW 
DECLARE 
    d VARCHAR2 (1); 
BEGIN 
    SELECT A.EVENT_TYPE INTO d 
    FROM AYT_EVENT A 
    WHERE A.EVENT_ID = :new.EVENT_ID; 
    IF (d IS NULL OR d <> 'S') THEN 
        raise_application_error(-20223,'FK AYT_SEMINAR_AYT_EVENT_FK in Table AYT_SEMINAR violates Arc constraint on Table AYT_EVENT - discriminator column EVENT_TYPE doesn''t have value ''S'''); 
    END IF; 
    EXCEPTION 
    WHEN NO_DATA_FOUND THEN 
        NULL; 
    WHEN OTHERS THEN 
        RAISE; 
END; 
/

CREATE OR REPLACE TRIGGER ARC_FKArc_3_AYT_EXHIBITION 
BEFORE INSERT OR UPDATE OF EVENT_ID 
ON AYT_EXHIBITION 
FOR EACH ROW 
DECLARE 
    d VARCHAR2 (1); 
BEGIN 
    SELECT A.EVENT_TYPE INTO d 
    FROM AYT_EVENT A 
    WHERE A.EVENT_ID = :new.EVENT_ID; 
    IF (d IS NULL OR d <> 'E') THEN 
        raise_application_error(-20223,'FK AYT_EXHIBITION_AYT_EVENT_FK in Table AYT_EXHIBITION violates Arc constraint on Table AYT_EVENT - discriminator column EVENT_TYPE doesn''t have value ''E'''); 
    END IF; 
    EXCEPTION 
    WHEN NO_DATA_FOUND THEN 
        NULL; 
    WHEN OTHERS THEN 
        RAISE; 
END; 
/



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                            21
-- CREATE INDEX                             1
-- ALTER TABLE                             43
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           2
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
