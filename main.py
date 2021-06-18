# https://www.youtube.com/watch?v=dam0GPOAvVI
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)