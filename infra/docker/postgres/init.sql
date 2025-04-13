-- Enable the pgcrypto extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- SET TIME ZONE 'Central Time (US & Canada)';
SET TIME ZONE 'America/Chicago';


-- Create users table for authentication and demographics
CREATE TABLE IF NOT EXISTS user_auth (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Create user demographics table
CREATE TABLE IF NOT EXISTS user_demographics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES user_auth(id) ON DELETE CASCADE,

    age INT CHECK (age >= 0),
    gender VARCHAR(100),
    location VARCHAR(255),
    occupation VARCHAR(100),
    company VARCHAR(100),
    country VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create auth_tokens table for storing authentication tokens
CREATE TABLE auth_tokens (
  token_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES user_auth(id),
  token TEXT NOT NULL,
  expires_at TIMESTAMP NOT NULL
);

-- Create user_activity table for tracking user activity
CREATE TABLE user_subscriptions (
  user_id UUID REFERENCES user_auth(id),
  subreddit VARCHAR(255),
  followed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, subreddit)
);

-- -- Optional: insert a sample user (replace password hash with bcrypt'd one)
-- INSERT INTO users (username, email, password_hash, age, country)
-- VALUES (
--     'demo_user',
--     'demo@example.com',
--     '$2b$12$eImGQbTr1uG1UrvT4NnGcePiA/zXqz7u1R6h4sGk3PbJMzZ3B8z9K', -- "password"
--     25,
--     'USA'
-- );