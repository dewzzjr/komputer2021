-- untuk mengambil total order untuk setiap customer
SELECT Customers.CustomerID, Customers.CustomerName, COUNT(Orders.OrderID) as TotalOrder
FROM Orders 
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID 
GROUP BY Customers.CustomerID;