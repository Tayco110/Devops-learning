# Estudo dirigido StatefulSets

Este repositório contém uma aplicação simples criada com FastAPI, empacotada em um contêiner Docker e implantada no Kubernetes usando o Minikube. A aplicação demonstra a configuração de manifestos Kubernetes, como StatefulSets, service, ingress e secret. A [aplicação](https://github.com/Tayco110/Devops-learning/blob/main/task4-1/app/main.py) em questão tem como foco o uso do `StatefulSet`.

## Instruções de Uso

1. Clone este repositório(via SSH):

```bash
git clone git@github.com:Tayco110/Devops-learning.git
cd Devops-learning/task4-1
```

2. Construa e execute a aplicação localmente:

```bash
# Construir a imagem Docker
docker build --no-cache -t  microservice-name .
```

Os passos para deployment da aplicação são similares aos encontrados [nesta](https://github.com/Tayco110/Devops-learning/blob/main/task-1/README.md) documentação.

## Manifesto StatefulSets

### Introdução

O StatefulSet é um controlador de trabalho no Kubernetes projetado para lidar com aplicações que possuem estados persistentes, como bancos de dados e serviços de armazenamento. Ao contrário dos pods gerenciados por um Deployment, os pods em um StatefulSet têm identificadores únicos e mantêm seus estados mesmo quando são recriados ou redimensionados.

### Casos de Uso

O StatefulSet é útil em cenários onde a ordem, identidade e persistência dos pods são importantes, como:

- **Bancos de Dados**: Bancos de dados distribuídos como o MySQL, PostgreSQL e MongoDB podem se beneficiar do StatefulSet para garantir a ordem de inicialização e a persistência dos dados.
- **Serviços de Cache**: Aplicações de cache como o Redis e o Memcached podem se beneficiar do gerenciamento de pods do StatefulSet para manter os dados armazenados.

### Características-Chave

- **Identificadores Únicos**: Cada pod em um StatefulSet possui um nome e um identificador numérico único que persiste através de reinicializações.
- **Orquestração Ordenada**: O StatefulSet garante a ordem em que os pods são criados, atualizados ou excluídos, o que é crítico para aplicações de dados.
- **Persistência**: Com a persistência dos identificadores e das definições dos pods, a StatefulSet é capaz de recuperar e manter estados persistentes.
- **Gerenciamento de Redimensionamento**: O redimensionamento do StatefulSet é controlado de forma previsível, permitindo que você adicione ou remova pods com segurança.

## Como Criar e Gerenciar um StatefulSet

### 1. Defina um Arquivo YAML do StatefulSet

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: my-statefulset
spec:
  serviceName: "my-service"
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-container
          image: my-image
          ports:
            - containerPort: 80
```

### 2. Aplique o Arquivo YAML

Use o comando `kubectl apply -f <nome>.yaml` para criar o StatefulSet.

### 3. Monitore e Gerencie

Use `kubectl get statefulset` para verificar o status do StatefulSet. Use `kubectl describe statefulset <nome>` para obter detalhes adicionais.

### 4. Escalonamento e Atualizações

Use `kubectl scale statefulset nome --replicas=novo-numero` para escalar o StatefulSet. Para atualizar, modifique o arquivo YAML e execute `kubectl apply -f arquivo-atualizado.yaml`.

## Disclaimer

Este README apresenta uma tradução adaptada da página oficial [Kubernetes StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). Certifique-se de consultar a documentação oficial para obter informações completas e atualizadas sobre StatefulSets Kubernetes.