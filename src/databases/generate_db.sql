CREATE TABLE IF NOT EXISTS users (
  id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  name TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS custom_expenses_groups (
  id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL,
  name TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS expenses (
  id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  category TEXT,
  description TEXT,
  date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

