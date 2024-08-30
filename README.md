﻿E-commerce de carros usados

Projeto de Vendas de Carros
Este projeto é uma aplicação de back-end desenvolvida em Python, utilizando o ORM Peewee para interagir com um banco de dados SQLite. A aplicação permite a criação de contas para vendedores e compradores, registro de carros, visualização de saldos e compra de carros.

Funcionalidades
Vendedor
Criação de Conta: Vendedores podem criar uma conta fornecendo CPF, nome e saldo inicial.
Registro de Carros: Vendedores podem registrar carros à venda, incluindo detalhes como nome, placa, modelo e valor.
Visualização de Carros: Vendedores podem visualizar todos os carros que registraram, com status de venda.
Visualização de Saldo: Vendedores podem verificar seu saldo atual.
Comprador
Criação de Conta: Compradores podem criar uma conta fornecendo CPF, nome, saldo inicial e depósito.
Visualização de Carros à Venda: Compradores podem visualizar todos os carros disponíveis para compra.
Compra de Carros: Compradores podem comprar carros, com atualização automática dos saldos do comprador e do vendedor.
Visualização de Saldo: Compradores podem verificar seu saldo atual.
Tecnologias Utilizadas
Python: Linguagem de programação principal.
Peewee: ORM utilizado para interagir com o banco de dados SQLite.
SQLite: Banco de dados utilizado para armazenar as informações.
dotenv: Biblioteca para carregar variáveis de ambiente a partir de um arquivo .env.

