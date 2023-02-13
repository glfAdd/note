import views
from sanic import Sanic

app = Sanic(__name__)
app.blueprint(views.status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
