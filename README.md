## 🖥️ Configuração do CLI (`flow`)

Para executar o CLI do ArchFlow com um comando curto (`flow`), você pode configurar um alias permanente no seu terminal.
Isso permite chamar diretamente:

```bash
flow --help
flow doctor
flow my-flow-alias
```

### ✅ Criar alias permanente (Zorin OS / Bash)

1. Abra o arquivo `.bashrc`:

```bash
nano ~/.bashrc
```

2. Adicione ao final:

```bash
alias flow='PYTHONPATH=$HOME/Documents/code/arch-flow $HOME/Documents/code/arch-flow/.venv/bin/python $HOME/Documents/code/arch-flow/apps/cli/main.py'
```

3. Salve e recarregue:

```bash
source ~/.bashrc
```

> Isso garante que o comando `flow` esteja sempre disponível, respeitando a estrutura de pacotes do projeto.

---

## 🛠️ Automação com `Makefile`

Este projeto inclui um `Makefile` com comandos para facilitar tarefas de desenvolvimento como instalação, migração de
banco e atualização de dependências.

### Comandos disponíveis

| Comando                     | Descrição                                                             |
|-----------------------------|-----------------------------------------------------------------------|
| `make install`              | Instala as dependências do projeto usando `uv` + `requirements.txt`   |
| `make requirements`         | Gera ou atualiza o `requirements.txt` com as libs do ambiente virtual |
| `make migrate-new NAME=...` | Cria uma nova migração com Alembic (ex: `add_flows_table`)            |
| `make migrate-up`           | Aplica todas as migrações pendentes                                   |
| `make migrate-down`         | Desfaz a última migração aplicada                                     |
| `make help`                 | Exibe os comandos disponíveis                                         |

### 📌 Exemplo de uso:

```bash
make install
make migrate-new NAME="create_flows_table"
make migrate-up
make requirements
```

> Todas as ferramentas (`python`, `alembic`, `pip`) são chamadas a partir do `.venv/bin`, garantindo que você nunca
> interfira no sistema global.

---

## 📦 Requisitos

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) instalado
- Ambiente virtual `.venv` ativo