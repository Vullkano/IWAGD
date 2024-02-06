# IWAGD

Este repositório contém dois trabalhos diferentes: um projeto mais simples desenvolvido ao longo das aulas, denominado **sitepr**, e um projeto final mais complexo chamado **reddit**, inspirado no famoso site Reddit.

## Estrutura do Repositório

- **sitepr**: Este é o trabalho desenvolvido ao longo das aulas. É um projeto mais simples e básico.

- **reddit**: Este é o projeto final, um clone do Reddit. Possui funcionalidades mais avançadas (desde autenticação pela google, captcha e a API do Chat GPT) e é um exemplo de aplicação web Django completa. O nome do website elaborado pelo grupo chama-se **Serit.Inc**

![Logotipo do Website](Serit_5.png)

## Como Rodar o Projeto Final 
Todo o código que for mostrado em seguida é suposto ser aplicado no terminal (para a realização deste foi usado o pycharm)

### Configurar Ambiente Virtual

Certifique-se de possuir um ambiente virtual (venv) configurado. Se não tiver, crie um novo ambiente virtual no seu diretório de projeto e ative-o:

```bash
python3 -m venv venv
venv/Scripts/Activate
```

### Instalar Dependências:
Instale as dependências do Django e do Django Allauth usando o pip:

```bash
pip install django
pip install django django-allauth
```

### Executar o Servidor:
Para iniciar o servidor, vá até o diretório que contém o arquivo manage.py e execute o seguinte comando no terminal:

```bash
python manage.py runserver --insecure
```
O argumento --insecure é necessário para servir arquivos estáticos durante o desenvolvimento.

### Acessar o Projeto:
Após iniciar o servidor, você poderá acessar o projeto no seu navegador através de http://127.0.0.1:8000/.

#### Nota 
Este trabalho possui 2 chaves, sendo elas:
- ChatGPT: https://platform.openai.com/account/api-keys
- Recaptcha: https://www.google.com/recaptcha/admin/create (Usar a V2 com caixa de seleção)
É necessário colocar estas chaves nos ficheiros: *views.py*, *login.html*, *settings.py*

Ambas as chaves, presentes no código, foram encriptadas no site https://www.tools4noobs.com/online_tools/encrypt/, utilizando os seguintes parâmetros:
- Key: Serit
- Algorithm: Cast-256
- Mode: CBC
