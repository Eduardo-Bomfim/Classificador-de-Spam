# 📧 Classificador de Spam com Naive Bayes

Este é um projeto de estudo que implementa um classificador de **spam para mensagens SMS**, utilizando o algoritmo **Multinomial Naive Bayes**.
O modelo é treinado para diferenciar mensagens comuns ("ham") de mensagens indesejadas ("spam") com base na frequência das palavras.

O código foi desenvolvido em **Python**, utilizando:

* **scikit-learn** → modelo de Machine Learning e métricas de avaliação.
* **pandas** → carregamento e manipulação de dados.

---

## ✨ Features

* 🔎 Classificação de mensagens de texto para identificar **spam**.
* 🤖 Modelo treinado com o algoritmo **Multinomial Naive Bayes**.
* 📦 Estrutura modular e orientada a objetos (classe `SpamClassifier`).
* ▶️ Script principal para **treinar** o modelo e **testar** novas frases.

---

## 🛠️ Tecnologias Utilizadas

* Python **3.10+**
* [scikit-learn](https://scikit-learn.org/stable/)
* [pandas](https://pandas.pydata.org/)
* **venv** para gerenciamento do ambiente virtual

---

## 🚀 Como Rodar o Projeto

### 📌 Pré-requisitos

* Python 3.10 ou superior
* Git

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/seu-usuario/classificador-de-spam.git
cd Classificador-de-Spam
```

### 2️⃣ Crie e Ative o Ambiente Virtual

```bash
# Criar ambiente
python -m venv .venv

# Ativar ambiente
# Windows (CMD/PowerShell)
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

> Caso ainda não exista, você pode gerar o arquivo `requirements.txt` com:

```bash
pip freeze > requirements.txt
```

### 4️⃣ Execute o Projeto

```bash
python src/main.py
```

---

## 📂 Estrutura do Projeto

```
classificador-de-spam/
├── .venv/                   # Ambiente virtual (ignorado pelo Git)
├── src/                     # Código-fonte principal
│   ├── main.py              # Ponto de entrada para treinamento e predição
│   └── models/              # Módulos relacionados ao modelo
│       └── SpamClassifier.py # Classe SpamClassifier com a lógica do modelo
├── requirements.txt         # Dependências do projeto
├── .gitignore               # Arquivos/pastas ignorados pelo Git
└── README.md                # Documentação do projeto
```

---

## 📄 Licença

Este projeto está sob a licença **MIT**.
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
