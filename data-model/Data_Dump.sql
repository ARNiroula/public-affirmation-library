-- Author Data
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_1', 'Auth_Lname_2', '10th St', 'NYC', 'NY', 'USA', 'auth_fname_1@example.com');
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_2', 'Auth_Lname_2', '11th St', 'NYC', 'NY', 'USA', 'auth_fname_2@example.com');
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_3', 'Auth_Lname_3', '12th St', 'NYC', 'NY', 'USA', 'auth_fname_3@example.com');
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_4', 'Auth_Lname_4', '14th St', 'NYC', 'NY', 'USA', 'auth_fname_4@example.com');
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_5', 'Auth_Lname_5', '15th St', 'NYC', 'NY', 'USA', 'auth_fname_5@example.com');
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_6', 'Auth_Lname_6', '16th St', 'NYC', 'NY', 'USA', 'auth_fname_6@example.com');
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_7', 'Auth_Lname_7', '17th St', 'NYC', 'NY', 'USA', 'auth_fname_7@example.com');
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_8', 'Auth_Lname_8', '18th St', 'NYC', 'NY', 'USA', 'auth_fname_8@example.com');
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_9', 'Auth_Lname_9', '19th St', 'NYC', 'NY', 'USA', 'auth_fname_9@example.com');
insert into ayt_author(fname, lname, addr_st, addr_city, addr_state, addr_ctry, EMAIL)
    values('Auth_Fname_10', 'Auth_Lname_10', '20th St', 'NYC', 'NY', 'USA', 'auth_fname_10@example.com');
insert into ayt_author(fname)
    values('Aristotle');
insert into ayt_author(fname)
    values('Plato');

-- Book Data
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('1', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('2', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('3', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('4', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('5', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('6', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('7', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('8', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('9', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));
insert into ayt_book(ISBN, NAME, TOPIC, PUB_DATE)
    values('10', 'Sample', 'Topic', to_date('2024-10-10', 'YYYY-MM-DD'));

-- Book Author Data
insert into ayt_book_author(auth_id, book_id) values(1, 1);
insert into ayt_book_author(auth_id, book_id) values(2, 2);
insert into ayt_book_author(auth_id, book_id) values(3, 3);
insert into ayt_book_author(auth_id, book_id) values(4, 4);
insert into ayt_book_author(auth_id, book_id) values(5, 5);
insert into ayt_book_author(auth_id, book_id) values(6, 6);
insert into ayt_book_author(auth_id, book_id) values(7, 7);
insert into ayt_book_author(auth_id, book_id) values(8, 8);
insert into ayt_book_author(auth_id, book_id) values(9, 9);
insert into ayt_book_author(auth_id, book_id) values(10, 10);

-- Book Copy Data
insert into ayt_book_copy(BOOK_ID)
    values(1);
insert into ayt_book_copy(BOOK_ID)
    values(1);
insert into ayt_book_copy(BOOK_ID)
    values(1);
insert into ayt_book_copy(BOOK_ID)
    values(1);
insert into ayt_book_copy(BOOK_ID)
    values(2);
insert into ayt_book_copy(BOOK_ID)
    values(2);
insert into ayt_book_copy(BOOK_ID)
    values(2);
insert into ayt_book_copy(BOOK_ID)
    values(3);
insert into ayt_book_copy(BOOK_ID)
    values(3);
insert into ayt_book_copy(BOOK_ID)
    values(3);
insert into ayt_book_copy(BOOK_ID)
    values(3);
insert into ayt_book_copy(BOOK_ID)
    values(3);
insert into ayt_book_copy(BOOK_ID)
    values(4);
insert into ayt_book_copy(BOOK_ID)
    values(5);
insert into ayt_book_copy(BOOK_ID)
    values(6);
insert into ayt_book_copy(BOOK_ID)
    values(7);
insert into ayt_book_copy(BOOK_ID)
    values(8);
insert into ayt_book_copy(BOOK_ID)
    values(9);
insert into ayt_book_copy(BOOK_ID)
    values(10);

-- Pay Type
insert into ayt_pay_type(type_id, type_name, descr)
    values(1, 'Credit Card', 'Description Type');
insert into ayt_pay_type(type_id, type_name, descr)
    values(2, 'Debit Card', 'Description Type');
insert into ayt_pay_type(type_id, type_name, descr)
    values(3, 'Cash', 'Description Type');

-- Room Data
insert into AYT_ROOM(room_id, capacity, descr) values
('100', 10, 'Sample Room');
insert into AYT_ROOM(room_id, capacity, descr) values
('101', 9, 'Sample Room');
insert into AYT_ROOM(room_id, capacity, descr) values
('102', 10, 'Sample Room');
insert into AYT_ROOM(room_id, capacity, descr) values
('103', 10, 'Sample Room');
insert into AYT_ROOM(room_id, capacity, descr) values
('104', 15, 'Sample Room');
insert into AYT_ROOM(room_id, capacity, descr) values
('105', 10, 'Sample Room');
insert into AYT_ROOM(room_id, capacity, descr) values
('106', 5, 'Sample Room');
insert into AYT_ROOM(room_id, capacity, descr) values
('107', 2, 'Sample Room');
insert into AYT_ROOM(room_id, capacity, descr) values
('108', 10, 'Sample Room');
insert into AYT_ROOM(room_id, capacity, descr) values
('109', 4, 'Sample Room');

-- ID Type
insert into ayt_id(ID_TYPE, ID_NAME, DESCR)
    values('1', 'Passport', 'Passport Info');
insert into ayt_id(ID_TYPE, ID_NAME, DESCR)
    values('2', 'Citizenship', 'Citizenship Info');
insert into ayt_id(ID_TYPE, ID_NAME, DESCR)
    values('3', 'Driving Liscense', 'Driving Info');
insert into ayt_id(ID_TYPE, ID_NAME, DESCR)
    values('4', 'College ID', 'College Info');


-- Customer Data Insert
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
    values ('Cust_Fname_1', 'Cust_Lname_2', '1', 'cust_1@test.com');
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
    values ('Cust_Fname_2', 'Cust_Lname_2', '2', 'cust_2@test.com');
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
    values ('Cust_Fname_3', 'Cust_Lname_3', '3', 'cust_3@test.com');
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
    values ('Cust_Fname_4', 'Cust_Lname_4', '4', 'cust_4@test.com');
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
  values ('Cust_Fname_5', 'Cust_Lname_5', '5', 'cust_5@test.com');
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
    values ('Cust_Fname_6', 'Cust_Lname_6', '6', 'cust_6@test.com');
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
    values ('Cust_Fname_7', 'Cust_Lname_7', '7', 'cust_7@test.com');
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
    values ('Cust_Fname_8', 'Cust_Lname_8', '8', 'cust_8@test.com');
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
    values ('Cust_Fname_9', 'Cust_Lname_9', '9', 'cust_9@test.com');
insert into ayt_cust(FNAME, LNAME, PHONE, EMAIL)
    values ('Cust_Fname_10', 'Cust_Lname_10', '10', 'cust_10@test.com');

-- Customer ID data
insert into ayt_cust_id(id_num, cust_id, id_type) values('1', 1, '1');
insert into ayt_cust_id(id_num, cust_id, id_type) values('2', 2, '1');
insert into ayt_cust_id(id_num, cust_id, id_type) values('3', 3, '2');
insert into ayt_cust_id(id_num, cust_id, id_type) values('4', 4, '3');
insert into ayt_cust_id(id_num, cust_id, id_type) values('5', 5, '3');
insert into ayt_cust_id(id_num, cust_id, id_type) values('6', 6, '1');
insert into ayt_cust_id(id_num, cust_id, id_type) values('7', 7, '1');
insert into ayt_cust_id(id_num, cust_id, id_type) values('8', 8, '1');
insert into ayt_cust_id(id_num, cust_id, id_type) values('9', 9, '1');
insert into ayt_cust_id(id_num, cust_id, id_type) values('10', 10, '1');

-- Customer Room Reservation
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        4,
        1,
        '100'
    );
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        4,
        2,
        '101'
    );
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        4,
        3,
        '102'
    );
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        4,
        4,
        '103'
    );
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        4,
        5,
        '104'
    );
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        4,
        6,
        '105'
    );
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        4,
        7,
        '106'
    );
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        1,
        8,
        '107'
    );
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        4,
        9,
        '108'
    );
insert into ayt_cust_room(start_time, end_time, descr, num_indv, cust_id, room_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Sample Descr',
        4,
        10,
        '109'
    );

-- Customer Rental
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        1,
        1
    );
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        2,
        2
    );
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        3,
        3
    );
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        4,
        4
    );
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        5,
        5
    );
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        6,
        6
    );
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        7,
        7
    );
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        8,
        8
    );
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        9,
        9
    );
insert into ayt_rental(borrow_date, expected_date, cust_id, copy_id)
    values(
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-01 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        10,
        10
    );


-- Event(Seminar) Type
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        1,
        'Keynote Speaker',
        'Random'
    );
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        2,
        'Keynote Speaker',
        'Random'
    );
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        3,
        'Keynote Speaker',
        'Random'
    );
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        4,
        'Keynote Speaker',
        'Random'
    );
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        5,
        'Keynote Speaker',
        'Random'
    );
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        6,
        'Keynote Speaker',
        'Random'
    );
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        7,
        'Keynote Speaker',
        'Random'
    );
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        8,
        'Keynote Speaker',
        'Random'
    );
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        9,
        'Keynote Speaker',
        'Random'
    );
insert into ayt_event(event_name, start_date_time, end_date_time, event_topic, event_type)
    values(
        'E1',
        to_timestamp('2025-04-01 9:30', 'YYYY-MM-DD HH24:MI:SS'),
        to_timestamp('2025-04-02 12:30', 'YYYY-MM-DD HH24:MI:SS'),
        'Topic',
        'S'
    );
insert into ayt_seminar(event_id, keynote_speaker, seminar_type)
    values(
        10,
        'Keynote Speaker',
        'Random'
    );
