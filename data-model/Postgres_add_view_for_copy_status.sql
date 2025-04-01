create view ayt_book_copy_status as
select a.copy_id, a.book_id,
case
    when b.actual_date is NULL then 'Borrowed'
    when b.actual_date > b.expected_date then 'Late'
    else 'Returned'
end as status
from ayt_book_copy as a inner join ayt_rental as b on a.copy_id = b.copy_id;

