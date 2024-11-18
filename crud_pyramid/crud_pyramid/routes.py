def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('user_list', '/user_list')
    config.add_route('create_user', '/create_user')
