CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT
);

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    issue TEXT,
    status TEXT DEFAULT 'open'
);

CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    text TEXT,
    sentiment TEXT
);
