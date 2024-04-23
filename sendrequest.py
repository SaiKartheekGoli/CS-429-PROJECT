from flask import Flask, request, render_template_string, jsonify
import requests
import subprocess

# Initialize Flask app
app = Flask(__name__)

# HTML template for user interface
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Similarity Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: auto;
            padding-top: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
            padding: 20px;
        }
        .form {
            margin-bottom: 20px;
        }
        input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        .results {
            margin-top: 20px;
        }
        .error {
            color: red;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 5px;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="form">
            <h1 style="text-align: center;">Document Similarity Analysis</h1>
            <form method="post">
                <input type="text" id="query" name="query" placeholder="Enter your query...">
                <input type="submit" value="Search">
            </form>
            <div style="display: flex; justify-content: space-between;">
                <form method="post" action="/crawl_data" style="width: 49%;">
                    <input type="submit" value="Crawl Data">
                </form>
                <form method="post" action="/index_data" style="width: 49%;">
                    <input type="submit" value="Index Data">
                </form>
            </div>
        </div>
        {% if response_content %}
            <div class="results">
                {% if response_content.get('error') %}
                    <section class="error">{{ response_content['error'] }}</section>
                {% else %}
                    <ul>
                        {% for result in response_content['results'] %}
                            <li>{{ result['document_content'] }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}
            </div>
        {% endif %}
    </div>
</body>
</html>

'''


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            # Define the URL Port For Query API
            url = 'http://127.0.0.1:5000/query'
            # Define the JSON data
            json_data = {'query': query, 'top_k': 5}
            # Send the POST request
            response = requests.post(url, json=json_data)
            if response.status_code == 200:
                return render_template_string(HTML_TEMPLATE, response_content=response.json())
            else:
                return render_template_string(HTML_TEMPLATE, response_content={'error': 'Error fetching results'})
        else:
            return render_template_string(HTML_TEMPLATE, response_content={'error': 'Query parameter is missing or empty'})
    else:
        # GET request, just render the form
        return render_template_string(HTML_TEMPLATE)


@app.route('/crawl_data', methods=['POST'])
def crawl_data():
    # Execute crawler.py
    subprocess.run(['python', 'crawler.py'])
    return render_template_string(HTML_TEMPLATE)


@app.route('/index_data', methods=['POST'])
def index_data():
    # Execute indexer.py
    subprocess.run(['python', 'indexer.py'])
    return render_template_string(HTML_TEMPLATE)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
