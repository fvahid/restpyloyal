from eve import Eve
from eve_swagger import swagger, add_documentation
from eve_healthcheck import EveHealthCheck
import logging


def log_every_get(resource, request, payload):
    # custom INFO-level message is sent to the log file
    app.logger.info('We just answered to a GET request!')


app = Eve()
app.register_blueprint(swagger)
app.on_post_GET += log_every_get
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
app.config['SWAGGER_HOST'] = '198.23.172.239'

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

    # enable logging to 'app.log' file
    handler = logging.FileHandler('app.log')

    # set a custom log format, and add request
    # metadata to each log line
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(filename)s:%(lineno)d] -- ip: %(clientip)s, '
        'url: %(url)s, method:%(method)s'))

    # the default log level is set to WARNING, so
    # we have to explictly set the logging level
    # to INFO to get our custom message logged.
    app.logger.setLevel(logging.INFO)

    # append the handler to the default application logger
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0')

