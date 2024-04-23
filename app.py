from flask import Flask, request, jsonify
from indexer import Indexer
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize the indexer
indexer = Indexer()

# Load content from documents.txt and build the index
file_path = os.path.join(os.path.dirname(__file__), 'natural.txt')
with open(file_path, 'r', encoding='utf-8') as file:
    documents = file.readlines()
indexer.build_index(documents)

# Define route to handle queries
@app.route('/query', methods=['POST'])
def query():
    # Get query from JSON data
    query_data = request.json
    query = query_data.get('query')

    if not query:
        return jsonify({'error': 'Query parameter is missing or empty'}), 400

    # Query the index
    similarities = indexer.query_index(query)

            # Convert similarities array to a standard Python list
    similarities = similarities.tolist()

    # Get top-K ranked results
    k = query_data.get('top_k', 5)
    top_results = []
    for idx in similarities[:k]:
        top_results.append({'document_index': idx, 'document_content': documents[idx]})

    return jsonify({'results': top_results})

if __name__ == "__main__":
    app.run(debug=True)
