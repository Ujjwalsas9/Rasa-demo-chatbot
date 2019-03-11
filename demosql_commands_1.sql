# show databases;
# use DBforChatbot;
-- CREATE TABLE Persons (
--     PersonID int,
--     LastName varchar(255),
--     FirstName varchar(255),
--     StockName varchar(255),
--     StockBalance int
-- );
-- select * from Persons;
-- INSERT INTO Persons (PersonID, LastName, FirstName, StockName, StockBalance)
-- VALUES (0002, 'Anand', 'Utsav', 'SB-123', 231045);

-- SELECT PersonID, LastName 
-- FROM   Persons 
-- WHERE  PersonID IN (SELECT PersonID FROM Persons);
select * from Persons;


use DBforChatbot;
CREATE TABLE Persons (
PersonID int,
LastName varchar(255),
FirstName varchar(255),
StockName varchar(255),
StockBalance int);


INSERT INTO Persons (PersonID, LastName, FirstName, StockName, StockBalance) VALUES (0002, 'Anand', 'Utsav', 'SB-123', 231045);
INSERT INTO Persons (PersonID, LastName, FirstName, StockName, StockBalance) VALUES (0001, 'Anand', 'Ujjwal', 'SB123', 231095);
