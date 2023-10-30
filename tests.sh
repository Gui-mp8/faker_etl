#!/bin/bash

# Execute os testes usando pytest
pytest tests/

# Verifique o código de saída dos testes
pytest_exit_code=$?

# Inicie os containers usando docker-compose, apenas se os testes passarem
if [ $pytest_exit_code -eq 0 ]; then
  echo "Tests passed. Starting containers..."
  docker compose up
else
  echo "Tests failed. Containers will not be started."
  exit 1 
fi

# Mantenha o script em execução para manter os containers em execução
# Você pode pressionar Ctrl+C para encerrar a execução
while true; do
  sleep 1
done