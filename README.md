# Controle de Estoque para Minimercado

Este aplicativo foi desenvolvido para atender a necessidade de gerentes e estoquistas de minimercados de bairro, permitindo o controle eficiente do estoque de produtos. Com ele, é possível adicionar, consultar, atualizar e remover produtos de forma simples e rápida, diretamente de um dispositivo móvel ou computador.

## Funcionalidades

- **Adicionar produtos:** Cadastre novos itens que chegaram do fornecedor, incluindo nome, marca, valor, quantidade e imagem.
- **Consultar estoque:** Veja a lista de produtos cadastrados, com informações de preço, quantidade e marca.
- **Atualizar produtos:** Altere rapidamente o preço de venda, quantidade, nome, marca ou imagem de um produto.
- **Remover produtos:** Exclua produtos descontinuados do estoque.
- **Acesso seguro:** Apenas usuários autenticados podem acessar e modificar o estoque.

# Como rodar o aplicativo

Siga o passo a passo abaixo para clonar e executar o projeto localmente:

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <nome_da_pasta_do_projeto>
   ```

2. **Crie um ambiente virtual Python na raiz do projeto:**
   ```bash
   python3 -m venv venv
   ```

3. **Ative o ambiente virtual:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Realize as migrações para criar o banco de dados:**
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário para acessar o painel administrativo:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Execute o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

8. **Acesse a aplicação:**
   - Abra o navegador e acesse a URL fornecida pelo Django (geralmente http://127.0.0.1:8000/).

## Observações

- Para upload de imagens, certifique-se de que o diretório `media/` está criado e configurado nas configurações do Django.
- O acesso às funcionalidades é restrito a usuários autenticados.
- O painel administrativo do Django pode ser acessado em `/admin` para gerenciamento avançado.

## Necessidade Atendida

Este sistema foi projetado para facilitar o dia a dia do estoquista, permitindo:
- Cadastro rápido de produtos recebidos.
- Consulta instantânea de preços e quantidades.
- Atualização ágil de preços de venda.
- Remoção eficiente de produtos descontinuados.

Ideal para pequenos mercados que buscam praticidade e controle no gerenciamento do estoque.
