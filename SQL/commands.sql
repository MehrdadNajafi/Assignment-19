INSERT INTO Customers ( id, name, city, country)
VALUES (1, 'mehrdad', 'ahvaz', 'iran');
INSERT INTO Customers ( id, name, city, country)
VALUES (2, 'christopher', 'new york', 'USA')

##################

INSERT INTO Products (id, name, price, count)
VALUES (1, 'shampoo', 14500, 9);
INSERT INTO Products (id, name, price, count)
VALUES (2, '3060 Ti', 30000000, 0)

##################

SELECT * FROM Products
WHERE count != 0;

##################

DELETE FROM Customers WHERE country != 'iran';

##################

UPDATE Products
SET price = price * 80/100
WHERE count != 0;