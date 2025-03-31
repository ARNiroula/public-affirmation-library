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
-- create or replace function check_room_book() returns trigger $check_room_book$
-- $check_room_book$ language plpgsql;

-- Create the invoice for Rental when the actual_date is updated
create or replace function invoice_generator() returns trigger as $invoice_generator$
    declare
        amt decimal(6, 2);
    begin
        -- Calculate the Amount
        if new.actual_date > old.expected_date then
            amt = ((old.expected_date - old.borrow_date) * 0.2 + (new.actual_date - old.expected_date) * 0.4);
        else
            amt = (old.expected_date - old.borrow_date) * 0.2;
        end if;

        -- Create an Invoice Record
        insert into ayt_invoice (invoice_date, total_amount, rental_id)
            values(CURRENT_DATE, amt, new.rental_id);
        return NEW;
    end;
$invoice_generator$ language plpgsql;

create or replace trigger generate_invoice
after update of actual_date on AYT_RENTAL
    for each row execute function invoice_generator();


