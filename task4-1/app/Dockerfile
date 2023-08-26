# Estágio de construção
FROM python:3.10.6 as builder

# Define a pasta de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Estágio de produção
FROM python:3.10.6-slim

# Define um usuário não-root para maior segurança
RUN useradd -m user
USER user

# Define a pasta de trabalho no contêiner
WORKDIR /app

# Copia os arquivos do estágio de construção para o contêiner
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia os arquivos do projeto para o contêiner
COPY . .

# Define variáveis de ambiente para o Python não criar arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Executa o servidor Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]