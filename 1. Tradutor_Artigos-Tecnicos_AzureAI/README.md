# 🌐 Tradutor de Artigos com Azure AI

Este projeto implementa um tradutor de artigos técnicos utilizando Azure AI, permitindo a tradução de conteúdo a partir de URLs e arquivos de texto.

## 📋 Funcionalidades

- Tradução de páginas web via URL
- Tradução de arquivos de texto
- Suporte a múltiplos idiomas
- Extração automática de conteúdo relevante
- Formatação em Markdown do texto traduzido

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Azure OpenAI Service
- Bibliotecas Python:
  - requests
  - beautifulsoup4
  - langchain_openai

## ⚙️ Pré-requisitos

- Python 3.8 ou superior
- Conta Azure com acesso ao Azure OpenAI Service
- Conexão com internet estável

## 🔧 Configuração

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd <nome-do-diretorio>
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente em um arquivo `.env`:
```plaintext
AZURE_ENDPOINT=<seu-endpoint>
AZURE_API_KEY=<sua-api-key>
AZURE_API_VERSION=2024-02-15-preview
AZURE_DEPLOYMENT_NAME=<nome-do-deployment>
```

## 🚀 Como Usar

### Tradução via URL:
```python
from translator import extract_text_from_url, translate_Article

# Extrair e traduzir conteúdo de uma URL
url = 'https://exemplo.com/artigo'
text = extract_text_from_url(url)
translated = translate_Article(text, "pt-br")
```

## 📝 Exemplo de Uso

```python
# Traduzir artigo da web
url = 'https://dev.to/article'
text = extract_text_from_url(url)
article = translate_Article(text, "pt-br")
print(article)
```

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add: nova funcionalidade'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.



## 📚 Documentação Adicional

Para mais informações sobre os serviços utilizados:
- [Azure OpenAI Service](https://azure.microsoft.com/services/openai-service)
- [Documentação Azure AI](https://docs.microsoft.com/azure/ai-services)