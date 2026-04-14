CREATE TABLE IF NOT EXISTS users (
  id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  name TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS custom_expenses_groups (
  id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL,
  name TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS banks (
  id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  cnpj TEXT NOT NULL,
  code TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS banks_users (
  id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  bank_id uuid NOT NULL,
  user_id uuid NOT NULL,
  account_balance DECIMAL(10, 2) NOT NULL,
  credit_card_expiration_date DATE,
  FOREIGN KEY (bank_id) REFERENCES banks(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS expenses (
  id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL,
  bank_id uuid NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  category TEXT,
  description TEXT,
  date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (bank_id) REFERENCES banks(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS custom_expenses_groups_expenses (
  id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  custom_expenses_group_id uuid NOT NULL,
  expense_id uuid NOT NULL,
  FOREIGN KEY (custom_expenses_group_id) REFERENCES custom_expenses_groups(id) ON DELETE CASCADE,
  FOREIGN KEY (expense_id) REFERENCES expenses(id) ON DELETE CASCADE
);
