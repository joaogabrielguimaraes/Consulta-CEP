# Consulta CEP

Aplicação web para buscar informações de endereços a partir do CEP digitado, utilizando a API pública [ViaCEP](https://viacep.com.br/).

---

## 🛠️ Funcionalidades

- Consulta rápida e fácil de endereços pelo CEP.
- Validação básica para garantir que o CEP tenha 8 dígitos numéricos.
- Exibição clara dos dados do endereço em formato de tabela.
- Tratamento de erros para CEPs inválidos ou problemas na conexão.
- Interface web simples e responsiva construída com Streamlit.

---

## 🚀 Como usar

### Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas: `streamlit`, `pandas`, `requests`

### Instalação

Instale as dependências com:

```bash
pip install streamlit pandas requests
```

### Executar a aplicação

Execute o comando:

```bash
streamlit run app.py
```

> Substitua `app.py` pelo nome do seu arquivo Python, caso seja diferente.

---

## 📋 Como funciona

1. Digite um CEP válido com 8 números.
2. Clique no botão **Buscar**.
3. O endereço correspondente será exibido em uma tabela.
4. Caso o CEP não seja encontrado ou inválido, mensagens de erro ou alerta serão exibidas.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Abra issues ou pull requests para sugerir melhorias.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
