from flask import Flask

app = Flask(__name__)


@app.route('/sample')
def sample():
    return """
    <html>
        <head><title>Sample Flask App</title></head>
        <body style="background-color: green; color:white; text-align: center; padding-top: 50px;">
            <h1>Hello from flask sample app!</h1>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

