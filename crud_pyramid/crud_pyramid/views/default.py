from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError
from ..models.user_model import User

#Função de view para home
@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}


# Função de view para a create_user.jinja2
@view_config(route_name='user_list', renderer='templates/user_list.jinja2')
def user_list(request):
    try:
        users = request.dbsession.query(User).all()
        return {'users': users}
    except SQLAlchemyError as e:
        return {'error_message': 'Erro ao carregar os usuários.'}

@view_config(route_name='create_user', renderer='templates/create_user.jinja2', request_method=['GET', 'POST'])
def create_user(request):
    if request.method == 'GET':
        return {'name': '', 'email': '', 'phone': ''}
    try:
        user_data = request.POST
        name, email, phone = user_data.get('name'), user_data.get('email'), user_data.get('phone')
        if not all([name, email, phone]):
            return {'error_message': 'Todos os campos são obrigatórios.', 'name': name, 'email': email, 'phone': phone}
        new_user = User(name=name, email=email, phone=phone)
        request.dbsession.add(new_user)
        request.dbsession.flush()
        return {'success_message': 'Usuário criado com sucesso.', 'name': '', 'email': '', 'phone': ''}
    except SQLAlchemyError:
        return {'error_message': 'Erro ao criar o usuário.'}

@view_config(route_name='delete_user', request_method='GET')
def delete_user(request):
    user_id = request.matchdict.get('id')
    if not user_id:
        return Response("Usuário não encontrado", status=404)

    try:
        user = request.dbsession.query(User).filter(User.id == user_id).first()
        if not user:
            return Response("Usuário não encontrado", status=404)
        request.dbsession.delete(user)
        request.dbsession.flush()
        return HTTPFound(location=request.route_url('user_list'))
    except SQLAlchemyError:
        return Response("Erro ao excluir usuário.", status=500)
