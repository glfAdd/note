from sanic import Blueprint
from sanic.response import text

status = Blueprint('status', url_prefix='res/status')


@status.route('/')
async def get_status(request):
    return text('返回status')
