ALTER TABLE ayt_cust add constraint cust_email_unique UNIQUE(email);

ALTER TABLE ayt_cust add constraint cust_phone_unique UNIQUE(phone);

ALTER TABLE ayt_cust_id add constraint cust_id_num_unique UNIQUE(id_num);

ALTER TABLE ayt_author add constraint auth_email_unique UNIQUE(email);

ALTER TABLE ayt_book add constraint book_isbn_unique UNIQUE(ISBN);

ALTER TABLE ayt_sponsor add constraint sponsor_email_unique UNIQUE(email);
