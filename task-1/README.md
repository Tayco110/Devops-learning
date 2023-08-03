# Projeto Microservice FastAPI

Este é um projeto simples de um microserviço em FastAPI que pode ser implantado localmente usando Docker e Kubernetes. Siga as etapas abaixo para configurar e executar o projeto em seu ambiente local.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em sua máquina:

- [Python](https://www.python.org/downloads/) (versão 3.10.6 ou superior)
- [Docker](https://www.docker.com/get-started)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) (se você optar por usar o Kubernetes)

## Passo 1: Clonar o repositório

Clone este repositório em sua máquina local usando o seguinte comando:
  ```bash
  git clone git@github.com:Tayco110/Devops-learning.git
  cd Devops-learning
  cd task-1
  ```

## Passo 2: Criar e executar o microserviço localmente

  Nesta etapa, vamos criar o microserviço em FastAPI e executá-lo localmente usando um contêiner Docker.

  1. Certifique-se de estar na pasta raiz do projeto onde o arquivo `requirements.txt` está localizado.
  2. No terminal, execute o seguinte comando para instalar as dependências do projeto:
  ```bash
  pip install -r requirements.txt
  ```
  Isso instalará as dependências listadas no arquivo `requirements.txt`, que incluem o FastAPI e o Uvicorn necessários para o microserviço.
  
  3. Agora, vamos construir a imagem Docker do microserviço. No terminal, execute o seguinte comando:
     ```bash
     docker build -t nome_do_microservico .
     ```
     Escolha um nome adequado para o microserviço implementado.
  
  4. Com a imagem criada, você pode executar o microserviço localmente em um contêiner Docker com o seguinte comando:
     ```bash
     docker run -d -p 8000:8000 nome_do_microservico
     ```
  ## Passo 3: Subir a imagem para o Docker Hub. Caso não tenha uma conta na plataforma supracitada, crie uma neste [link](https://hub.docker.com/signup):
  
  1. Faça login no Docker Hub:
     ```bash
     docker login
     ```
     
  2. "Marque" sua imagem com o nome completo do repositório no Docker Hub. Onde nome_do_usuario é o seu `nome de usuário` no Docker Hub e `tag` é uma tag opcional, como `latest`:
     ```bash
     docker tag nome_do_microservico nome_do_usuario/nome_do_microservico:tag
     ```
  
  4. Faça o push da imagem para o Docker Hub:
     ```bash
     docker push nome_do_usuario/nome_do_microservico:tag
     ```

## Passo 4: Configurar o Kubernetes (Minikube ou Kind):

Nesta etapa, vamos configurar o Kubernetes em sua máquina local. Escolha entre [Minikube](https://minikube.sigs.k8s.io/docs/start/) ou [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/) para criar um cluster Kubernetes local. Os passos abaixo estão dentro do escopo da utilização do [Minikube](https://minikube.sigs.k8s.io/docs/start/).

  1. Instalação:

     ```bash
     curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
     sudo install minikube-linux-amd64 /usr/local/bin/minikube
     ```
  2. Iniciando seu cluster:

     ```bash
     minikube start
     ```
  3. Configurando o kubectl:

     ```bash
     minikube kubectl -- get po -A
     ```
  4. Para tornar a usabilidade mais fácil, adicione a seguinte linha em seu arquivo de configuração do Shell:

     ```bash
     alias kubectl="minikube kubectl --"
     ```

## Passo 5: Implantar o microserviço no Kubernetes:
  Agora que você tem um cluster Kubernetes local, vamos implantar o microserviço nele.

  1. Certifique-se de que o Kubernetes está em execução e configurado corretamente.
  2. No terminal, execute os seguintes comandos para implantar o microserviço:

     ```bash
     kubectl apply -f deployment.yaml
     kubectl apply -f service.yaml
     ```
  3. Verifique se o Pod está em execução:

     ```bash
     kubectl get pods
     ```
  4. Verifique se o serviço está ativo:

     ```bash
     kubectl get services
     ```
     
  5. Acesse o serviço:

     ```bash
     minikube service nome-do-microservico-service
     ```
## Preview do resultado
[Resultado](https://github.com/Tayco110/Devops-learning/assets/44499744/bd6766b5-c58d-4648-bd33-1904410d3cf1)


