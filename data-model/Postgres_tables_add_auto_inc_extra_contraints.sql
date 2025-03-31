--Add AutoIncrement to ID Primary Key which is Numeric
ALTER TABLE AYT_CUST 
    ALTER COLUMN CUST_ID add generated always as identity;

ALTER TABLE AYT_CUST_ROOM 
    ALTER COLUMN RES_ID add generated always as identity;

ALTER TABLE AYT_INVOICE 
    ALTER COLUMN INVOICE_ID add generated always as identity;

ALTER TABLE AYT_RENTAL 
    ALTER COLUMN RENTAL_ID add generated always as identity;

ALTER TABLE AYT_BOOK_COPY 
    ALTER COLUMN COPY_ID add generated always as identity;

ALTER TABLE AYT_BOOK
    ALTER COLUMN BOOK_ID add generated always as identity;

ALTER TABLE AYT_CUST_EXHIBITION
    ALTER COLUMN REG_ID add generated always as identity;

ALTER TABLE AYT_AUTHOR_SEMINAR
    ALTER COLUMN INVITATION_ID add generated always as identity;

ALTER TABLE AYT_EVENT
    ALTER COLUMN EVENT_ID add generated always as identity;

ALTER TABLE AYT_PAY
    ALTER COLUMN PAY_ID add generated always as identity;

ALTER TABLE AYT_AUTHOR
    ALTER COLUMN AUTH_ID add generated always as identity;

ALTER TABLE AYT_SPONSOR
    ALTER COLUMN SPONSOR_ID add generated always as identity;

ALTER TABLE AYT_CUST_EXHIBITION
    ALTER COLUMN REG_ID add generated always as identity;

-- Add constraints that End Date/Times should be always greater than Start
-- AYT_CUST_ROOM
alter table AYT_CUST_ROOM
	add constraint check_datetime_cust_room check(start_time < end_time);

-- AYT_RENTAL
alter table AYT_RENTAL
    add constraint check_date_rental check(borrow_date < expected_date),
	-- Add constraint when the actual_date is updated
	add constraint check_actual_date_rental check((actual_date is null) or (borrow_date < actual_date));

-- AYT_EVENT
alter table AYT_EVENT
    add constraint check_datetime_event check(start_date_time < end_date_time);

