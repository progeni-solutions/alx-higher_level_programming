-- Creates a new table <second_table> in the hbtn_0c_0 database
-- The table is created only if does not exists
-- Adds the columns <id>, <name> and <score>
-- Adds 4 rows of data 
CREATE TABLE IF NOT EXISTS second_table (id INT,name VARCHAR(256), score INT);
INSERT INTO second_table VALUES(1, "John", 10);
INSERT INTO second_table VALUES(2, "Alex", 3);
INSERT INTO second_table VALUES(3, "Bob", 14);
INSERT INTO second_table VALUES(4, "George", 8);
