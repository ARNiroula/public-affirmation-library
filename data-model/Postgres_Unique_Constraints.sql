ALTER TABLE ayt_cust add constraint cust_email_unique UNIQUE(email);

ALTER TABLE ayt_cust add constraint cust_phone_unique UNIQUE(phone);

ALTER TABLE ayt_author add constraint auth_email_unique UNIQUE(email);

ALTER TABLE ayt_book add constraint book_isbn_unique UNIQUE(ISBN);
