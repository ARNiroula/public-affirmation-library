-- Checking if the number of Individuals exceed the room capacity or not
create or replace function room_cap() returns trigger as $room_cap$
declare
    cap smallint;
begin
    -- Get the room capacity
    select capacity into cap
    from AYT_ROOM
    where room_id = new.room_id
    limit 1;

    if (new.NUM_INDV > cap) then
        raise exception 'The Number of Individuals exceed the room capacity';
    end if;
    return new;
end;
$room_cap$ language plpgsql;

create or replace trigger check_room_cap
before insert or update on AYT_CUST_ROOM
    for each row execute function room_cap();

-- Trigger to check if room is already booked or not
create or replace function check_room_book() returns trigger as $check_room_book$
    declare
        counter integer;
    begin
        -- Check if any timestamp overlaps or not
        select count(start_time) into  counter
        from AYT_CUST_ROOM
        where   new.room_id = room_id
                and (start_time, end_time) overlaps (new.start_time, new.end_time);
        
        if counter > 0 then
            raise exception 'Room booking not avalidable for that time range';
        end if;

        return new;
    end;
$check_room_book$ language plpgsql;
create or replace trigger room_book
before insert or update on AYT_CUST_ROOM
    for each row execute function check_room_book();

-- Create the invoice for Rental when the actual_date is updated
create or replace function invoice_generator() returns trigger as $invoice_generator$
    declare
        amt decimal(6, 2);
        curr_cust_id integer;
        bor_date date;
        exp_date date;
        act_date date;
    begin
        -- Extracting all the necessary data
        bor_date = date(old.borrow_date);
        exp_date = date(old.expected_date);
        act_date = date(new.expected_date);
        -- Calculate the Amount
        if act_date > exp_date then
            amt = ((exp_date - bor_date) * 0.2 + (act_date - exp_date) * 0.4);
        else
            amt = (exp_date - bor_date) * 0.2;
        end if;

        select cust_id into curr_cust_id
            from ayt_rental
            where rental_id = new.rental_id;

        -- Create an Invoice Record
        insert into ayt_invoice (invoice_date, total_amount, rental_id)
            values(CURRENT_DATE, amt, new.rental_id);

        raise notice 'New Invoice Created for Customer ID % with Rental ID %', curr_cust_id, new.rental_id;
        return NEW;
    end;
$invoice_generator$ language plpgsql;

create or replace trigger generate_invoice
after update of actual_date on AYT_RENTAL
    for each row execute function invoice_generator();


-- Check if the invitation is sent to Authors who have email address
create or replace function check_author() returns trigger as $check_author$
    declare
        author_email varchar(254);
    begin
        -- Get the author email
        select email into author_email
        from ayt_author
        where auth_id = new.auth_id;

        if author_email is NULL then
            raise exception 'Invalid Invitation. Author Does not have an email';
        end if;
        return new;
    end;
$check_author$ language plpgsql;

create or replace trigger check_author_avail
before insert or update of auth_id on ayt_author_seminar
for each row execute function check_author();

-- Check if the book copy is avalidable or not
create or replace function check_copy() returns trigger as $check_copy$
    declare
        counter integer;
    begin

        -- Get the List of Book
        select count(1) into counter
        from AYT_RENTAL
        where   copy_id = new.copy_id
                and ((actual_date is null) or (actual_date > new.borrow_date));

        if counter > 0 then
            if counter > 1 and new.rental_id <> old.rental_id then
                raise exception 'Book Copy Not avalidable';
            end if;
        end if;
        return new;
    end;
$check_copy$ language plpgsql;

create or replace trigger check_book_copy
    before insert or update on ayt_rental
    for each row execute function check_copy();


-- Check if the pay amount exceeds the invoice_amount or not
create or replace function check_pay_amt() returns trigger as $check_pay_amt$
    declare
        total_curr_amt decimal(6, 2);
        latest_amt decimal(6, 2);
        total_amt decimal(6, 2);
    begin
        -- Get the total requried amount
        select total_amount into total_amt
        from ayt_invoice
        where invoice_id = new.invoice_id;
        
        -- Get the Total Amount Paid Till Now
        select sum(amount) into total_curr_amt
        from ayt_pay
        where invoice_id = new.invoice_id;

        latest_amt = new.amount;
        if (latest_amt + total_curr_amt) > total_amt then
            raise exception 'Total Amount Paid Exceeded the Total Invoice Amount';
        end if;
        return new;
        
    end;
$check_pay_amt$ language plpgsql;

create or replace trigger check_pay_amt_trigger
    before insert on ayt_pay
    for each row execute function check_pay_amt();
