# Aplicação DevOps com FastAPI, Docker e Kubernetes
## Table of Contents
- [Aplicação DevOps com FastAPI, Docker e Kubernetes](#aplicação-devops-com-fastapi-docker-e-kubernetes)
  - [Table of Contents](#table-of-contents)
  - [Visão Geral](#visão-geral)
  - [Requisitos](#requisitos)
  - [Instruções de Uso](#instruções-de-uso)
  - [Manifestos Kubernetes](#manifestos-kubernetes)
  - [Detalhes da Aplicação](#detalhes-da-aplicação)
  - [Conclusão](#conclusão)
  - [Disclaimer](#disclaimer)


Este repositório contém uma aplicação simples criada com FastAPI, empacotada em um contêiner Docker e implantada no Kubernetes usando o Minikube. A aplicação demonstra a configuração de manifestos Kubernetes, como deployment, service, ingress e secret. A [aplicação](https://github.com/Tayco110/Devops-learning/blob/main/task-3/app/main.py) em questão tem como foco o uso do `secret`.

## Visão Geral

Este projeto consiste em criar uma aplicação FastAPI, criar sua imagem e implantá-la no Kubernetes usando o Minikube. A aplicação possui um único endpoint, `\vars` que **retorna as variáveis de ambiente do sistema**.

## Requisitos

Certifique-se de ter os seguintes componentes instalados em seu ambiente:

- [Python](https://www.python.org/downloads/) (com [FastAPI](https://fastapi.tiangolo.com/) e [Uvicorn](https://www.uvicorn.org/))
- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

Siga os links acima para obter informações detalhadas sobre como instalar cada componente necessário para executar a aplicação. Certifique-se de seguir as instruções de instalação apropriadas para o seu sistema operacional.

## Instruções de Uso

1. Clone este repositório(via SSH):

```bash
git clone git@github.com:Tayco110/Devops-learning.git
cd Devops-learning/task-3
```

2. Construa e execute a aplicação localmente:

```bash
# Construir a imagem Docker
docker build --no-cache -t  microservice-name .
```

Os passos para deployment da aplicação são similares aos encontrados [nesta](https://github.com/Tayco110/Devops-learning/blob/main/task-1/README.md) documentação. Os passos e instruções a respeito do uso do manifesto `ingress` podem ser encontrados [aqui](https://github.com/Tayco110/Devops-learning/blob/main/task-2/README.md). O foco desta aplicação é demonstrar o uso do `secert`.

## Manifestos Kubernetes

Os manifestos Kubernetes estão localizados na pasta `app` e `deploy`.

- [`deploy.yaml`](./kubernetes-manifests/deployment.yaml): Define um deployment que gerencia a replicação da aplicação.
- [`service.yaml`](./kubernetes-manifests/service.yaml): Define um serviço que expõe a aplicação internamente no cluster.
- [`ingress.yaml`](./kubernetes-manifests/ingress.yaml): Define um ingress para permitir o acesso externo à aplicação.
- [`secret.yaml`](./kubernetes-manifests/secret.yaml): Define um secret para armazenar informações sensíveis.

## Detalhes da Aplicação

A aplicação é uma API simples com um único endpoint:

- `GET /vars`: **Retorna as variáveis de ambiente do sistema**.

A aplicação é encapsulada em um contêiner Docker usando um Dockerfile multistage para manter o tamanho da imagem mínimo.

A implantação no Kubernetes é gerenciada por manifestos que criam e configuram deployments, serviços e ingress para a aplicação.

## Conclusão

Após a implementação da aplicação ter sido realizada de forma correta, a mesma poderá ser acessada usando o domínio [`task3.com`](). As informações retornada do `End point` são as informações sensíveis da aplicação.

## Disclaimer

**Esta aplicação busca apenas demonstrar o uso do manifesto secret, é importante notar que as informações retornadas são apenas para fins didáticos.**