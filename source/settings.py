DOMAIN = {
    'user': {
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username',
            },
        'disable_documentation': True,
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
            'username': {
                'type': 'string',
                 'unique': True
            },
            'password': {
                'type': 'string'
            },
            'phone': {
                'type': 'string'
            }
        }
    }
}

RESOURCE_METHODS = ['GET', 'POST']
