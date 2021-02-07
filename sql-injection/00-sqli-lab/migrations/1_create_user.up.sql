CREATE TABLE users (
    username varchar(255) NOT NULL,
    password varchar(40) NOT NULL,
    email varchar(45) NOT NULL,
    department varchar(30) NOT NULL
);

CREATE TABLE products (
    product_id int NOT NULL,
    product_name varchar(255) NOT NULL,
    category varchar(40) NOT NULL,
    price int NOT NULL,
    released boolean NOT NULL
);

INSERT INTO users VALUES('admin', '12346', 'admin@admin.com', 'IT');
INSERT INTO users VALUES('idman', 'p@$$w0rd!', 'idman@idman.com', 'Accounting');
INSERT INTO products VALUES(1,'tamiya', 'toys', 10000, false);
INSERT INTO products VALUES(2,'bakugan', 'toys', 10000, true);
INSERT INTO products VALUES(3,'violin', 'instrument', 10000, false);
INSERT INTO products VALUES(4,'guitar', 'instrument', 50000, true);
