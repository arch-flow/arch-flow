VENV_BIN := .venv/bin
PYTHON := $(VENV_BIN)/python
ALEMBIC := $(VENV_BIN)/alembic
PIP := $(VENV_BIN)/pip

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
	@echo "  install                 - Instala as dependências do projeto via requirements.txt."
	@echo "  requirements            - Gera/atualiza o requirements.txt com os pacotes atuais do .venv."
	@echo "  migrate-new NAME=''     - Cria um novo script de migração com o nome informado."
	@echo "  migrate-up              - Aplica todas as migrações pendentes no banco de dados."
	@echo "  migrate-down            - Desfaz a última migração aplicada (downgrade -1)."
	@echo "  create-module NAME=''   - Cria a estrutura inicial de um novo módulo (ex: make create-module NAME=FlowStep)"
