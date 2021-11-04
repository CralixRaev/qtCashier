CREATE TABLE products (
    id          INTEGER       PRIMARY KEY AUTOINCREMENT
                              UNIQUE
                              NOT NULL,
    name        VARCHAR (255) UNIQUE
                              NOT NULL ON CONFLICT REPLACE,
    picture     BLOB,
    price       FLOAT         NOT NULL,
    is_favorite BOOLEAN       DEFAULT (FALSE)
);

CREATE TABLE cheque (
    id          INTEGER  PRIMARY KEY AUTOINCREMENT
                         UNIQUE
                         NOT NULL,
    is_refunded BOOLEAN  DEFAULT (FALSE),
    datetime    DATETIME NOT NULL,
    comment     TEXT     DEFAULT ('Нет комментария')
);

CREATE TABLE barcode (
    id         INTEGER       PRIMARY KEY AUTOINCREMENT
                             NOT NULL
                             UNIQUE,
    barcode    VARCHAR (255) NOT NULL
                             UNIQUE,
    product_id INTEGER       UNIQUE
                             REFERENCES products (id)
                             NOT NULL
);

CREATE TABLE cheque_products (
    id         INTEGER PRIMARY KEY AUTOINCREMENT
                       UNIQUE
                       NOT NULL,
    cheque_id  INTEGER REFERENCES cheque (id)
                       NOT NULL,
    product_id INTEGER REFERENCES products (id)
                       NOT NULL,
    quantity   INTEGER NOT NULL
                       DEFAULT (1)
);
