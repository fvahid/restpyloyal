from eve import Eve
from eve_healthcheck import EveHealthCheck


app = Eve()
hc = EveHealthCheck(app, '/healthcheck')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
