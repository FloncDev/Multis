CREATE TABLE guilds (
    id INT PRIMARY KEY NOT NULL,
    prefix_auto_cap BOOL NOT NULL
);

-- @block
CREATE TABLE prefixes (
    guild_id INT NOT NULL,
    prefix VARCHAR(10) NOT NULL
);

-- @block
CREATE TABLE pins_settings (
    guild_id INT NOT NULL,
    pins_enabled BOOL NOT NULL,
    pin_channel_id INT,
    pin_emoji_amount INT
);

-- @block
CREATE TABLE suggestions_settings (
    guild_id INT NOT NULL,
    suggestions_enabled BOOL NOT NULL,
    suggestion_channel_id INT