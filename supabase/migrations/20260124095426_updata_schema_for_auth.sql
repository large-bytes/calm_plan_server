CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    email VARCHAR NOT NULL UNIQUE,
    hashed_password VARCHAR(225),
    disabled BOOLEAN DEFAULT FALSE
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    priority VARCHAR,
    user_id INTEGER REFERENCES users(id)
);

CREATE INDEX ix_tasks_name ON tasks(name);
CREATE INDEX ix_tasks_priority ON tasks(priority);
