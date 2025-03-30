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
    for each row execute procedure room_cap();


-- Constraint to check if the student
