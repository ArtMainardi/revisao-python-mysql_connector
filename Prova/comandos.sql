create database lanchonete;
use lanchonete;

# === CRIAÇÃO DA TABELA: ===
CREATE TABLE cardapio (
  id int PRIMARY KEY AUTO_INCREMENT,
  nome varchar(100) NOT NULL,
  preco decimal(10,2) NOT NULL,
  tipo varchar(30) DEFAULT NULL,
  disponivel boolean DEFAULT TRUE
);

# === INSERÇÃO DE DADOS: ===
# a) ->
INSERT INTO cardapio(nome, preco, tipo, disponivel) VALUES 
('Agua', 3.90, 'Bebida', true),
('Refrigerante', 7.99,'Bebida', false),
('X-Salada', 19.99, 'Lanche', true),
('X-Egg', 22.90, 'Lanche', false),
('Paleta italiana', 10.99, 'Sobremesa', false),
('Sorvete', 5.99, 'Sobremesa', true),
('Agua com gas', 6.50, 'Bebida', false);

# === BUSCAS: ===
# b) -> Do mais barato para o mais caro:
SELECT * FROM cardapio ORDER BY preco ASC;
# c) -> Preço específico:
SELECT * FROM cardapio WHERE preco = 5.99;
# d) -> Busca por palavra à escolha:
SELECT * FROM cardapio WHERE nome LIKE '%ga%';

# === MODIFICAÇÕES: ===
# e) -> Atualizar preço:
UPDATE cardapio SET preco = 5 WHERE id = 2;
# f) -> Marcar um item como esgotado:
UPDATE cardapio SET disponivel = false WHERE id = 3;