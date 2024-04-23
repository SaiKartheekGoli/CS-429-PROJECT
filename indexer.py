from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class Indexer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()  # Initialize TF-IDF vectorizer
        self.index = None  # Initialize index to store TF-IDF representations of documents

    def build_index(self, documents):
        """
        Build the index from a list of documents.

        Parameters:
        - documents (list): List of strings representing documents.
        """
        tfidf_matrix = self.vectorizer.fit_transform(documents)  # Compute TF-IDF matrix
        self.index = tfidf_matrix  # Store TF-IDF matrix in the index

    def save_index(self, filename):
        """
        Save the index to a pickle file.

        Parameters:
        - filename (str): Name of the file to save the index.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self.index, f)  # Serialize and save the index to a file

    def load_index(self, filename):
        """
        Load the index from a pickle file.

        Parameters:
        - filename (str): Name of the file containing the index.
        """
        with open(filename, 'rb') as f:
            self.index = pickle.load(f)  # Load the serialized index from the file

    def query_index(self, query):
        """
        Perform a similarity search on the index using a query.

        Parameters:
        - query (str): Query string.

        Returns:
        - similarities (array): Array of cosine similarities between the query and documents in the index.
        """
        query_vec = self.vectorizer.transform([query])  # Compute TF-IDF representation of the query
        similarities = cosine_similarity(query_vec, self.index)  # Compute cosine similarities
        return similarities.argsort()[0][::-1][:5]  # Return indices of top 5 most similar documents

# Usage example
if __name__ == "__main__":
    # Initialize the indexer
    indexer = Indexer()

    # Load content from documents.txt
    with open('natural.txt', 'r', encoding='utf-8') as file:
        documents = file.readlines()

    # Build the index
    indexer.build_index(documents)

    # Save the index to file
    indexer.save_index('index.pkl')

    # Query the index
    query = 'language'
    print(f"Query: {query}")
    similarities = indexer.query_index(query)
    print("Top 5 most similar documents:")
    for idx in similarities:
        print(f"- Document {idx}: {documents[idx]}")
