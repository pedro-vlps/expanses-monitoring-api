-- Popula o banco com dados fictícios para usuários, grupos personalizados e despesas.

INSERT INTO users (id, name, email, password_hash, created_at) VALUES
  ('9f1d2f17-4c3e-4f28-a241-3f5b7e2a8f01', 'Alice Silva', 'alice.silva@example.com', '$2b$12$alicehashplaceholder0123456789', '2026-01-05 10:15:00'),
  ('b6c8d901-2a7c-4eee-91a0-ef4db3f62234', 'Bruno Costa', 'bruno.costa@example.com', '$2b$12$brunohashplaceholder9876543210', '2026-01-10 14:30:00'),
  ('d4e9a72c-7b6f-4381-b2f3-1590ec0d4a56', 'Carla Nunes', 'carla.nunes@example.com', '$2b$12$carlahashplaceholder4567890123', '2026-02-02 09:05:00');

INSERT INTO custom_expenses_groups (id, user_id, name) VALUES
  ('a1c7e192-9268-44f1-8a43-7b8d2c3e9d50', '9f1d2f17-4c3e-4f28-a241-3f5b7e2a8f01', 'Viagens'),
  ('c3b9f2e7-5a4d-4e8f-b2c5-1d8a6f0b2e74', '9f1d2f17-4c3e-4f28-a241-3f5b7e2a8f01', 'Assinaturas'),
  ('e7d4a8b1-6c02-4f97-8051-9b3c1e7d2f88', 'b6c8d901-2a7c-4eee-91a0-ef4db3f62234', 'Lazer'),
  ('f4b0d7c5-9a13-4f41-9d30-2c5e7a1b8f90', 'd4e9a72c-7b6f-4381-b2f3-1590ec0d4a56', 'Moradia');

INSERT INTO expenses (id, user_id, amount, category, description, date, created_at) VALUES
  ('3c5b9d28-1f44-4aef-b6d4-937abc2f5e01', '9f1d2f17-4c3e-4f28-a241-3f5b7e2a8f01', 1250.00, 'Aluguel', 'Pagamento de aluguel do apartamento de fevereiro', '2026-02-03', '2026-02-03 08:20:00'),
  ('5e7d2b61-3a4e-4d10-a3f9-8c0b5f2d6a12', '9f1d2f17-4c3e-4f28-a241-3f5b7e2a8f01', 89.90, 'Assinatura', 'Plano anual de música em streaming', '2026-02-12', '2026-02-12 11:45:00'),
  ('6f8e3c74-5b9a-4d30-b2e1-7f0a4c8d9b23', '9f1d2f17-4c3e-4f28-a241-3f5b7e2a8f01', 320.50, 'Viagem', NULL, '2026-03-18', '2026-03-18 16:10:00'),
  ('8a2d4f53-0b6e-4ceb-b947-2c1f5e7d3a44', 'b6c8d901-2a7c-4eee-91a0-ef4db3f62234', 45.20, 'Alimentação', NULL, '2026-02-21', '2026-02-21 20:05:00'),
  ('9b3f6e82-1d7c-4e1e-a6f5-4b8c0d2e1f45', 'b6c8d901-2a7c-4eee-91a0-ef4db3f62234', 120.00, 'Lazer', 'Cinema e pipoca para estreia de filme', '2026-03-05', '2026-03-05 19:30:00'),
  ('0c4e7a91-2f6b-4c8d-b5e2-9a0f3c1d2b56', 'b6c8d901-2a7c-4eee-91a0-ef4db3f62234', 210.00, 'Transporte', 'Cartão de transporte público recarregado', '2026-03-22', '2026-03-22 09:15:00'),
  ('1d5f8b02-3c7a-4e9f-b6d1-0e2f4a5c7b68', 'd4e9a72c-7b6f-4381-b2f3-1590ec0d4a56', 79.90, 'Casa', NULL, '2026-02-08', '2026-02-08 10:50:00'),
  ('2e6a9c13-4d8b-4f10-a7c2-1f3b5d6e8a79', 'd4e9a72c-7b6f-4381-b2f3-1590ec0d4a56', 240.00, 'Serviços', 'Conserto de eletrodoméstico na cozinha', '2026-03-12', '2026-03-12 13:40:00'),
  ('3f7b0d24-5e1c-4a2f-b8d3-2a4c6f7e9b80', 'd4e9a72c-7b6f-4381-b2f3-1590ec0d4a56', 15.50, 'Lazer', NULL, '2026-03-15', '2026-03-15 17:25:00'),
  ('4a8c1e35-6f2d-4b3e-a9c4-3b5d7f8a0c91', '9f1d2f17-4c3e-4f28-a241-3f5b7e2a8f01', 62.75, 'Compras', 'Compra de itens para o escritório em casa', '2026-04-01', '2026-04-01 12:05:00'),
  ('5b9d2f46-7a3e-4c5b-b0d5-4c6e8f9a1b02', 'b6c8d901-2a7c-4eee-91a0-ef4db3f62234', 18.40, 'Assinatura', 'Renovação mensal de revista digital', '2026-04-02', '2026-04-02 08:50:00');
