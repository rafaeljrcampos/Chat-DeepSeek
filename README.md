# Chat-Bot

## Descrição
O **Chat-Bot** é um assistente de conversa baseado no modelo **Deepseek**, utilizando o **Ollama** para inferência. O sistema permite interações inteligentes e respostas naturais, proporcionando uma experiência avançada de chat com IA.

## Requisitos
Antes de rodar o **Chat-Bot**, é necessário ter:
- **Ollama** instalado e em execução como servidor.
- O modelo **Deepseek** baixado e configurado no Ollama.

### Instalação do Ollama
Caso não tenha o Ollama instalado, siga as instruções no site oficial:
```sh
curl -fsSL https://ollama.ai/install.sh | sh
```

### Baixando o modelo Deepseek
```sh
ollama pull deepseek-r1:7b
```

### Iniciando o servidor
Para garantir que o **Chat-Bot** funcione corretamente, é necessário rodar o servidor do **Ollama**:
```sh
ollama serve
```

## Como executar o Chat-Bot
Depois de garantir que o servidor do **Ollama** está rodando, inicie o Chat-Bot com o seguinte comando:
```sh
python chatbot.py
```

## Configuração
Se desejar modificar o modelo ou ajustar parâmetros, edite o arquivo de configuração `config.yaml` e altere o nome do modelo para **Deepseek** ou outro modelo compatível.

## Contribuição
Sinta-se à vontade para contribuir com melhorias e correções! Basta fazer um **fork** do repositório e abrir um **pull request**.

## Licença
Este projeto está licenciado sob a **MIT License**. Para mais detalhes, consulte o arquivo `LICENSE`.

