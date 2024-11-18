from alembic.autogenerate import renderers
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError
from .. import models
from ..models.user_model import User
import json

#Função de view para home

@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}


@view_config(route_name='create_user', request_method='GET', renderer='templates/create_user.jinja2')
def create_user_form(request):
    # Retornar um template vazio ou com dados padrões (como nome, email, etc.)
    return {'name': '', 'email': '', 'phone': ''}


# Função de view para a create_user.jinja2
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError
from ..models.user_model import User
import json

@view_config(route_name='create_user', request_method='POST', renderer='templates/create_user.jinja2')
def create_user(request):
    try:
        # Verificar se o conteúdo da requisição é JSON ou formulário
        if request.content_type == 'application/json':
            user_data = request.json_body
        else:
            user_data = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'phone': request.POST.get('phone')
            }

        name = user_data.get('name')
        email = user_data.get('email')
        phone = user_data.get('phone')

        # Validar os dados
        if not (name and email and phone):
            # Passar mensagem de erro para o template
            return {
                'error_message': 'Todos os campos são obrigatórios.',
                'name': name,
                'email': email,
                'phone': phone
            }

        # Criar o novo usuário
        new_user = User(name=name, email=email, phone=phone)
        request.dbsession.add(new_user)
        request.dbsession.flush()

        # Passar a mensagem de sucesso e limpar os campos do formulário
        return {
            'success_message': 'Usuário criado com sucesso.',
            'name': '',  # Limpar campos
            'email': '',
            'phone': ''
        }

    except SQLAlchemyError as e:
        return {
            'error_message': f'Erro ao criar o usuário: {str(e)}',
            'name': name,
            'email': email,
            'phone': phone
        }



@view_config(route_name='user_list', renderer='templates/user_list.jinja2')
def user_list(request):
    try:
        # Consulta todos os usuários no banco
        users = request.dbsession.query(User).all()

        # Passa os usuários para o template
        return {'users': users}

    except SQLAlchemyError as e:
        # Em caso de erro, você pode renderizar uma página com erro
        return {'error_message': f'Erro ao carregar os usuários: {str(e)}'}



# Mensagem de erro se ocorrer falha ao conectar ao banco
db_err_msg = """\
Pyramid is having a problem using your SQL database. The problem
might be caused by one of the following things:

1. You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2. Your database server may not be running. Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
