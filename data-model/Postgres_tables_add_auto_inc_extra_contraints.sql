-- Add constraints that End Date/Times should be always greater than Start
-- AYT_CUST_ROOM
alter table AYT_CUST_ROOM
add constraints check_datetime check(start_time < end_time);

-- AYT_RENTAL
alter table AYT_RENTAL
    add constraints check_date check(borrow_date < expected_date);
