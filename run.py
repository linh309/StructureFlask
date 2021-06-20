#Run test server
from app import create_app
main = create_app()
main.run(host='127.0.0.1', port = 8080, debug=True)