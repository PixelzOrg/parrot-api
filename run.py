import os
from app import create_server

server = create_server()

if __name__ == '__main__':
    if not os.path.exists('app/data/videos/'):
        os.makedirs('app/data/videos/')

    if os.environ.get('PORT') is None:
        PORT = 5000
    else:
        PORT = os.environ.get('PORT')
    
    server.run(debug=True)
