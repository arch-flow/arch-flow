VENV_BIN := .venv/bin
PYTHON := $(VENV_BIN)/python
ALEMBIC := $(VENV_BIN)/alembic
PIP := $(VENV_BIN)/pip


.PHONY: db-up
db-up:
	@echo "-> Subindo PostgreSQL genérico (usuário: dev, senha: dev)..."
	docker-compose up -d
	@echo "-> PostgreSQL iniciado na porta 5432."

.PHONY: db-down
db-down:
	@echo "-> Finalizando PostgreSQL..."
	docker-compose down
	@echo "-> PostgreSQL encerrado."

.PHONY: db-create
db-create:
	@echo "-> Criando banco '$(DB)' no PostgreSQL..."
	docker exec -i local_postgres psql -U dev -c "CREATE DATABASE $(DB);"
	@echo "-> Banco '$(DB)' criado com sucesso."

.PHONY: install
install:
	@echo "-> Instalando dependências do projeto..."
	uv install -r requirements.txt
	@echo "-> Instalação concluída."

.PHONY: requirements
requirements:
	@echo "-> Gerando arquivo requirements.txt com dependências atuais..."
	uv pip install -r requirements.txt
	@echo "-> Arquivo requirements.txt atualizado com sucesso."

.PHONY: migrate-new
migrate-new:
	@echo "-> Gerando novo script de migração..."
	@if [ -z "$(NAME)" ]; then \
		echo "ERRO: É necessário fornecer o nome da migração (Ex: make migrate-new NAME=\"add_users_table\")"; \
		exit 1; \
	fi
	$(ALEMBIC) revision --autogenerate -m "$(NAME)"
	@echo "-> Script de migração '$(NAME)' gerado com sucesso."

.PHONY: migrate-up
migrate-up:
	@echo "-> Aplicando migrações no banco de dados..."
	$(ALEMBIC) upgrade head
	@echo "-> Migrações aplicadas com sucesso."

.PHONY: migrate-down
migrate-down:
	@echo "-> Desfazendo a última migração aplicada (downgrade)..."
	$(ALEMBIC) downgrade -1
	@echo "-> Downgrade concluído."

.PHONY: create-module
create-module:
	@echo "-> Criando estrutura de módulo para '$(NAME)'..."
	python scripts/create_module_structure.py $(NAME)


.PHONY: help
help:
	@echo "Comandos Makefile disponíveis:"
	@echo "  db-up                    - Sobe o container PostgreSQL local"
	@echo "  db-down                  - Derruba o container PostgreSQL"
	@echo "  db-create DB=nome        - Cria um banco com nome especificado"
	@echo "  install                  - Instala as dependências via requirements.txt"
	@echo "  requirements             - Atualiza o requirements.txt"
	@echo "  migrate-new NAME=desc    - Cria nova migração com nome"
	@echo "  migrate-up               - Aplica migrações no banco"
	@echo "  migrate-down             - Desfaz última migração"
	@echo "  create-module NAME=mod   - Cria estrutura de novo módulo"
