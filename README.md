# Monitoramento de Logs de Segurança

Este projeto contém um script Python que coleta eventos suspeitos de segurança, como tentativas de login inválido, e os salva em um arquivo CSV. O script pode ser executado manualmente ou automaticamente via GitHub Actions.

## Funcionalidades

- Coleta de tentativas de login inválido.
- Armazenamento dos dados em CSV.
- Execução automática configurada com GitHub Actions.

## Como usar

1. Clone o repositório.
2. Simule logs no arquivo `auth_simulado.log`.
3. Execute `python3 coletor.py`.

## Automação

Este repositório inclui um workflow do GitHub Actions que executa o script automaticamente a cada hora.

## Exemplo de saída

```
2025-06-04 14:35:00,Tentativa de Login Inválido,admin,192.168.1.100
```

## Ferramentas recomendadas

- Wazuh
- Graylog