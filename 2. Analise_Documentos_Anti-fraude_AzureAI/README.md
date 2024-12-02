# 🔍 Azure Document Analysis - Anti-Fraud Detection

Um projeto que utiliza Azure AI Document Intelligence para análise de documentos e detecção de fraudes em cartões de crédito.

## 📋 Sobre o Projeto

Esta solução combina serviços Azure para criar um sistema robusto de análise de documentos e detecção de fraudes:

- Upload e análise de documentos (imagens e PDFs)
- Verificação de cartões de crédito
- Tradução automática de documentos
- Armazenamento seguro em nuvem

## 🚀 Funcionalidades

- Análise de documentos usando Azure Document Intelligence
- Detecção de informações de cartões de crédito:
  - Número do cartão
  - Nome do titular
  - Data de validade
  - Banco emissor
- Upload de múltiplos formatos (PNG, JPG, JPEG, PDF)
- Armazenamento seguro no Azure Blob Storage
- Tradução de documentos entre idiomas

## 🛠️ Tecnologias

- Azure Document Intelligence
- Azure Blob Storage
- Azure OpenAI
- Python
- Streamlit
- LangChain
- Beautiful Soup

## ⚙️ Pré-requisitos

1. Conta Azure ativa
2. Python 3.8+
3. Serviços Azure configurados:
   - Document Intelligence
   - Blob Storage
   - OpenAI (opcional, para tradução)

## 🔧 Configuração

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd azure-document-analysis
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente (.env):
```
AZURE_ENDPOINT=<seu-endpoint>
AZURE_KEY=<sua-chave>
STORAGE_CONNECTION_STRING=<string-conexao>
CONTAINER_NAME=<nome-container>
```

## 📦 Execução

1. Inicie a aplicação:
```bash
streamlit run app.py
```

2. Acesse através do navegador:
```
http://localhost:8501
```

## 💡 Uso

1. Faça upload do documento na interface web
2. Aguarde a análise automática
3. Visualize os resultados detectados
4. Consulte o armazenamento para verificar o documento salvo
   
## 🔍 Funcionalidades de Análise

- Extração de dados de cartões:
  - Nome do titular
  - Número do cartão
  - Data de validade
  - Banco emissor

- Tradução de documentos:
  - Suporte para múltiplos idiomas
  - Conversão automática para português

## ⚠️ Notas Importantes

- Mantenha suas credenciais Azure seguras
- Não compartilhe o arquivo `.env`
- Use ambiente virtual Python
- Verifique permissões do Azure

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
