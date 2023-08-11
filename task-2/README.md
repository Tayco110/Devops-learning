
# Kubernetes: Services

## Visão Geral

Um Serviço Kubernetes é uma abstração que define um conjunto de pods e uma política de acesso a eles. A abstração permite que um serviço tenha uma IP estático e DNS, mesmo que a localização dos pods subjacentes possa mudar devido a escala para cima/para baixo ou atualizações.

Os Serviços Kubernetes permitem que um conjunto de pods trabalhe como um serviço único. Eles oferecem um ponto de acesso estável para comunicação com os pods, independentemente de suas localizações reais. Um serviço também permite a descoberta de serviço automática para os pods subjacentes.

## Motivação

Quando você cria um conjunto de pods e usa um objeto de serviço, o Kubernetes cria um IP estático e um nome DNS para o conjunto de pods. Isso permite que você acesse o conjunto de pods via IP ou nome DNS em vez de usar as informações do pod individualmente.

Isso é útil para definir uma abstração de serviço para um conjunto de pods que:

- Fornece escalabilidade horizontal.
- É distribuído por várias réplicas de pods.
- Oferece uma única entrada de rede para um conjunto de pods.
- Permite o balanceamento de carga para os pods.
- Fornece failover de pod.

## Conceitos

### Serviços Básicos

Um Serviço Kubernetes é um objeto abstrato sem estado que define um conjunto de pods e uma forma de acessá-los. Pode-se acessar um Serviço Kubernetes usando a rede de serviços, que é definida automaticamente.

### IPs e Portas

Cada Serviço Kubernetes tem um conjunto único de IP e Portas, que são atribuídos a cada pod individualmente.

### Seletores

Um Seletor é a forma de filtrar um conjunto de pods de um serviço. Por exemplo, é possível selecionar todos os pods com `app=MyApp` e `env=production`.

### Serviços sem Sessão

Um Serviço sem Sessão é um serviço sem estado que não preserva informações de sessão entre as requisições.

### Serviços com Sessão

Um Serviço com Sessão é um serviço com estado que mantém informações de sessão entre as requisições.

### Exposição do Serviço

Existem várias formas de expor um Serviço Kubernetes:

- Externa: expõe o serviço na rede externa.
- Interna: expõe o serviço apenas dentro do cluster.
- Entre Namespaces: expõe o serviço em namespaces diferentes.
- Entre o Cluster: expõe o serviço em clusters diferentes.

### Tipos de Serviço

O Kubernetes suporta vários tipos de Serviços:

- ClusterIP: expõe o serviço em um IP interno do cluster.
- NodePort: expõe o serviço em cada nó no mesmo IP e porta.
- LoadBalancer: expõe o serviço externamente usando um balanceador de carga externo.
- ExternalName: expõe o serviço usando o nome de um DNS externo.

## Exemplos

### Exemplo de um Serviço Básico

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```

Este exemplo cria um Serviço que encaminha o tráfego para pods com o rótulo `app=MyApp` na porta 9376.

### Exemplo de um Serviço Externo

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
  type: LoadBalancer
```

Este exemplo cria um Serviço do tipo LoadBalancer que expõe o serviço externamente usando um balanceador de carga externo.

Para mais detalhes e exemplos, consulte a [documentação oficial dos Serviços Kubernetes](https://kubernetes.io/docs/concepts/services-networking/service/).

---
# Kubernetes: Ingress

O Ingress é um recurso do Kubernetes que permite gerenciar o acesso externo aos serviços dentro de um cluster. Ele fornece regras de roteamento, redirecionamento e gerenciamento de tráfego para serviços em execução dentro do cluster.

## Conceitos Básicos

### O que é um Ingress?

O Ingress é uma API Kubernetes que gerencia o acesso externo aos serviços por meio de regras de roteamento baseadas em HTTP ou HTTPS.

### Controlador de Ingress

Um controlador de Ingress (como o Nginx Ingress Controller) é responsável por implementar as regras definidas em objetos Ingress e garantir que o tráfego externo seja direcionado corretamente para os serviços apropriados dentro do cluster.

### Regras e Rotas

Um objeto Ingress contém uma lista de regras, cada uma das quais define um host e um caminho. Cada regra é associada a um ou mais backends, que são serviços Kubernetes que lidarão com o tráfego correspondente.

## Implantação Básica

1. Instale um controlador de Ingress no seu cluster (por exemplo, Nginx Ingress Controller).

2. Crie um arquivo YAML para definir o objeto Ingress, especificando as regras de roteamento desejadas:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: meu-ingress
spec:
  rules:
    - host: seu-domínio.com
      http:
        paths:
          - path: /caminho
            pathType: Prefix
            backend:
              service:
                name: seu-service
                port:
                  number: 80
```

3. Aplique o manifesto Ingress ao cluster:

```bash
kubectl apply -f seu-arquivo-ingress.yaml
```

4. Configure o DNS para apontar o domínio para o endereço IP público do Ingress Controller.

5. Acesse seu aplicativo usando o domínio configurado.

## Disclaimer

Este README é uma tradução adaptada da página oficial [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/) e [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/). Certifique-se de consultar a documentação original para obter informações completas e atualizadas sobre Services Kubernetes.