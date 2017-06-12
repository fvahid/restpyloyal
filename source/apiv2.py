from eve import Eve
from eve_swagger import swagger, add_documentation
from eve_healthcheck import EveHealthCheck

app = Eve()
app.register_blueprint(swagger)
hc = EveHealthCheck(app, '/healthcheck')
# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'General Mobile API',
    'version': '1.0',
    'description': 'Easy to use anyware Mobile API',
    'termsOfService': 'my terms of service',
    'contact': {
        'name': 'vahid fardi',
        'url': 'https://gmail.com'
    },
    'license': {
        'name': 'GPLv3',
        'url': 'https://www.gnu.org/licenses/gpl-3.0.en.html',
    }
}

# optional. Will use flask.request.host if missing.
app.config['SWAGGER_HOST'] = 'loyalmobi.co.ir'

# optional. Add/Update elements in the documentation at run-time without deleting subtrees.
add_documentation({'paths': {'/status': {'get': {'parameters': [
    {
        'in': 'querytest',
        'name': 'foobar',
        'required': False,
        'description': 'special query parameter',
        'type': 'string'
    }]
}}}})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

