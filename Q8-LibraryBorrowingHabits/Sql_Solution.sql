select 
br.BorrowerName,
GROUP_CONCAT(b.BookName ORDER BY b.BookName SEPARATOR ',')  as BorrowedBooks
from Borrowers br
join Books b
on br.BookID=b.BookID
group by 1
order by br.BorrowerName