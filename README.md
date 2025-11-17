# Trabalho Prático - Engenharia de Software II

## Passos para subir o ambiente

```bash
docker compose up --build
```

## Como testar via curl

```bash
curl http://localhost:8100/health
curl "http://localhost:8100/quote?from=USD&to=BRL"

curl http://localhost:8101/health
curl "http://localhost:8101/history?from=USD&to=BRL"
```

## Observações

- Pra testar do terminal é usado `localhost` (ex.: `http://localhost:8100/health`).
- Pra um serviço chamar outro dentro do código Docker, ele usa o nome do serviço (ex.: `http://currency-history:8101/...`).
- Os serviços participam da mesma rede Docker (`micro-net`) que tá no Compose.
