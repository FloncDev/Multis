-- CREATE TABLE pins (
--     message_id BIGINT PRIMARY KEY NOT NULL,
--     channel_id BIGINT NOT NULL
-- )

CREATE TABLE suggestions (
    id BIGINT PRIMARY KEY NOT NULL,
    author BIGINT NOT NULL,
    text text NOT NULL,
    deleted BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)