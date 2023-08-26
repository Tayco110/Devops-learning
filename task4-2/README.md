# Estudo dirigido DaemonSet

Este repositório contém uma aplicação simples criada com FastAPI, empacotada em um contêiner Docker e implantada no Kubernetes usando o Minikube. A aplicação demonstra a configuração de manifestos Kubernetes, como DaemonSet, service, ingress e secret. A [aplicação](https://github.com/Tayco110/Devops-learning/blob/main/task4-2/app/main.py) em questão tem como foco o uso do `DaemonSet`.

## Instruções de Uso

1. Clone este repositório(via SSH):

```bash
git clone git@github.com:Tayco110/Devops-learning.git
cd Devops-learning/task4-2
```

2. Construa e execute a aplicação localmente:

```bash
# Construir a imagem Docker
docker build --no-cache -t  microservice-name .
```

Os passos para deployment da aplicação são similares aos encontrados [nesta](https://github.com/Tayco110/Devops-learning/blob/main/task-1/README.md) documentação.

## Manifesto DaemonSet

### Introdução

O DaemonSet é um controlador de recursos no Kubernetes que garante que um pod específico seja executado em todos os nós (nodes) do cluster ou em um subconjunto específico deles. É ideal para cenários em que cada nó requer uma cópia do pod, como para monitoramento de recursos ou coleta de logs.

### Casos de Uso

O DaemonSet é amplamente utilizado para:

- **Logging e Monitoramento**: Executar agentes de monitoramento ou coleta de logs em cada nó, permitindo a observabilidade e análise.
- **Gerenciamento de Recursos**: Distribuir recursos de forma uniforme em todos os nós, como caches ou bancos de dados em memória.
- **Redes e Armazenamento**: Implantação de serviços de rede, armazenamento ou proxy que precisam estar em todos os nós.

### Características-Chave

- **Execução em Todos os Nós**: O DaemonSet garante que pelo menos uma cópia do pod seja executada em todos os nós correspondentes.
- **Automaticidade**: À medida que você adiciona ou remove nós, o DaemonSet ajusta automaticamente o número de pods.
- **Nós de Subconjunto**: Você pode configurar o DaemonSet para selecionar apenas um subconjunto específico de nós para implantação.
- **Não afeta os nós de controle**: O DaemonSet não implantará pods em nós de controle (master nodes).

## Como Criar e Gerenciar um DaemonSet

### 1. Defina um Arquivo YAML do DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: my-daemonset
spec:
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
```

### 2. Aplique o Arquivo YAML

Execute o comando `kubectl apply -f <nome>.yaml` para criar o DaemonSet.

### 3. Monitoramento e Gerenciamento

Use `kubectl get daemonset` para verificar o status do DaemonSet. Utilize `kubectl describe daemonset <nome>` para obter informações adicionais.

### 4. Escalonamento e Atualizações

Use `kubectl scale daemonset nome --replicas=novo-numero` para aumentar ou diminuir o número de réplicas do DaemonSet. Para atualizar, modifique o arquivo YAML e execute `kubectl apply -f arquivo-atualizado.yaml`.

## Disclaimer

Este README apresenta uma tradução adaptada da página oficial [Kubernetes DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/). Certifique-se de consultar a documentação oficial para obter informações completas e atualizadas sobre DaemonSet Kubernetes.