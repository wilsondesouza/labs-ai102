from bs4 import BeautifulSoup
import requests
import os
from langchain_openai.chat_models.azure import AzureChatOpenAI
from dotenv import load_dotenv
import re
from urllib.parse import urlparse

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as credenciais das variáveis de ambiente
azure_endpoint = os.getenv("AZURE_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_KEY")
deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")
model_name = os.getenv("AZURE_MODEL_NAME")
api_version = os.getenv("AZURE_API_VERSION")


# Validação da Url
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc]) and result.scheme in ['http', 'https']
    except ValueError:
        return False


def extract_text_from_url(url):
    if not is_valid_url(url):
        raise ValueError("URL inválida. Certifique-se de que a URL começa com 'http://' ou 'https://'")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Erro ao acessar a URL: {str(e)}")
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(['script', 'style', 'header', 'footer', 'nav']):
            script_or_style.decompose()

        texto = soup.get_text(separator=' ')
        # Melhorar a limpeza do texto
        texto = re.sub(r'\s+', ' ', texto)
        texto = re.sub(r'[^\w\s.,!?]', '', texto)  # Remover caracteres especiais, exceto pontuação básica
        texto = texto.strip()

        return texto
    except Exception as e:
        raise RuntimeError(f"Erro ao extrair texto da página: {str(e)}")


def translate_article(text, target_language='pt'):
    try:
        llm = AzureChatOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=api_key,
            deployment_name=deployment_name,
            model_name=model_name,
            api_version=api_version,
            max_retries=0,
        )

        prompt = [
            ("system", "Você é um tradutor de textos."),
            ("user", f"Traduza o seguinte texto para o idioma {target_language} e responda em markdown: {text}")
        ]
        response = llm.invoke(prompt)

        return response.content
    except Exception as e:
        raise RuntimeError(f"Erro ao traduzir o texto: {str(e)}")


# URL do artigo a ser traduzido
url = "https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo"

try:
    extracted_text = extract_text_from_url(url)
    translated_text = translate_article(extracted_text, 'português')
    print(translated_text)
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")