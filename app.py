from flask import Flask
from routes import index, summarize, download_pdf

app = Flask(__name__)

# Register routes
app.add_url_rule('/', 'index', index, methods=['GET'])
app.add_url_rule('/summarize', 'summarize', summarize, methods=['POST'])
app.add_url_rule('/download_pdf', 'download_pdf', download_pdf, methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)
