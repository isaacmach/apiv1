# Use a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia todos os arquivos do projeto para o contêiner
COPY . /app

# Instala as dependências manualmente
RUN pip install flask gunicorn requests flask_jwt_extended

# Define a porta em que a aplicação Flask irá escutar
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
