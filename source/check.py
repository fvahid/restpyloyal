from eve_healthcheck import EveHealthCheck

app = Eve()
hc = EveHealthCheck(app, '/healthcheck')
