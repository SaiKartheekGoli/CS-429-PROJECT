<h1 align="center">  CS 429: INFORMATION RETRIEVAL PROJECT
</h1>

# TITLE: TEXT SIMILARITY SEARCH SYSTEM USING NATURAL LANGUAGE PROCESSING

# Author - SaiKartheek Goli - A20546631

## Operation:

1.	Running Scripts: Execute the respective Python scripts (app.py, sendrequest.py, crawler.py, indexer.py) using Python interpreter. App.py must run before sendrequest.py.
2.	Usage: Follow the command-line prompts for crawler.py. For app.py and sendrequest.py, interact via UI or send requests programmatically.
3.	Output: Results will be displayed in the terminal for crawler.py, and in the UI window for sendrequest.py.

### ABSTRACT

The project presents a comprehensive solution for efficiently identifying similar text documents based on user queries. Using advanced natural language processing (NLP) techniques, the system aims to provide accurate and relevant results to users seeking information from large text corpora. The project employs a combination of TF-IDF (Term Frequency-Inverse Document Frequency) vectorization and cosine similarity to compute the similarity between documents. TF-IDF, a fundamental technique in information retrieval, assigns weights to terms based on their frequency in a document and across the entire corpus. Cosine similarity measures the cosine of the angle between two vectors, providing a measure of similarity between documents. The architecture of the system consists of three main components: a Flask-based REST API server, an indexer module responsible for building and querying the TF-IDF index, and an optional web crawler for collecting text documents from web pages. The Flask server serves as the interface for users to submit queries and receive relevant document matches. Operationally, users interact with the system by sending POST requests to the /query endpoint of the Flask server, providing their query string and optionally specifying the number of top results desired. The system then processes the query, retrieves the most similar documents from the index, and returns them to the user.

### OVERVIEW

The text similarity search system using natural language processing (NLP) offers a solution to the increasingly complex task of document retrieval and similarity analysis. In the era of information overload, where vast amounts of textual data are generated every second, the need for efficient methods to search, retrieve, and organize this information has become paramount. Traditional keyword-based search engines often fall short in providing relevant results, especially when dealing with queries or large text corpora. This project addresses these challenges by use of NLP techniques, specifically TF-IDF vectorization and cosine similarity, to deliver accurate and contextually relevant document matches.

Solution Outline:

The proposed solution revolves around the construction of a text similarity search engine that using TF-IDF vectorization and cosine similarity to measure the similarity between textual documents. Cosine similarity then calculates the cosine of the angle between two TF-IDF vectors, providing a measure of similarity between documents.  By combining these techniques, the system can accurately identify documents that are semantically similar to a given query, even in the absence of exact keyword matches.
cosine_similarity(A,B)=(A⋅B)/(∥A∥×∥B∥)
Where:
-->	A and B are the TF-IDF vectors representing the two documents.
-->	A⋅B represents the dot product of the TF-IDF vectors A and B.
-->	∥A∥ and ∥B∥ represent the Euclidean norms (or magnitudes) of the TF-IDF vectors A and B respectively.

These functions are used to initialize the index manager and shut it down, freeing up all the acquired resources.

### Proposed System Overview

The proposed system is a document similarity analysis tool composed of three main components: a web crawler, an indexer, and a query processor. These components work together to crawl web documents, index them using TF-IDF representation, and allow users to query the indexed documents to find similar ones.

### The four main modules:

1.	Crawler Module: This module (crawler.py) is responsible for crawling web documents in HTML format. It utilizes Scrapy, a Python framework for web scraping, to extract content from web pages. The crawler is configurable with parameters such as the seed URL, maximum number of pages to crawl, and maximum depth of crawling.
2.	Indexer Module: The indexer.py module implements a TF-IDF based indexing system using the scikit-learn library. It constructs an inverted index to represent documents in a vector space model. The indexer also provides functionality for saving and loading the index to/from a pickle file.
3.	Flask Application: The Flask application (app.py) serves as the backend for handling free-text queries. It exposes a POST endpoint /query to receive queries in JSON format. Upon receiving a query, it utilizes the indexer to perform a similarity search and returns the top-K ranked results.
4.	Send Request Module: This module (sendrequest.py) provides a UI interface for users to interact with the Flask application. It allows users to enter a query and sends a POST request to the Flask server. Upon receiving the response, it highlights the search word in the output content and displays the results.


### DESIGN - SYSTEM CAPABILITIES, INTERACTIONS, INTEGRATION

The design of the document similarity analysis system encompasses a range of capabilities, interactions, and integrations aimed at providing extensive and scalable solutions for real-world applications. In this section, outline the key components and design considerations that underpin the functionality and performance of the system.

1.	Document Indexing Engine
The document indexing engine is responsible for processing and indexing large volumes of textual documents efficiently. Using techniques such as term frequency-inverse document frequency (TF-IDF) and cosine similarity, the engine generates vector representations of documents, enabling fast and accurate retrieval based on semantic similarity.  Additionally, the engine supports incremental indexing, allowing for real-time updates to the index as new documents are added or existing documents are modified.
2.	Query Processing Module
The query processing module facilitates user interactions with the system by interpreting user queries and retrieving relevant documents from the index. Upon receiving a query, the module applies the same vectorization techniques used during indexing to transform the query into a vector representation compatible with the document space. By computing the cosine similarity between the query vector and indexed document vectors, the module identifies the most relevant documents matching the user's query. 
3.	User Interface and Interaction
The Graphical user interface (UI) serves as the primary interaction point between users and the system, providing intuitive tools for querying, exploring, and display document similarities (UI). The UI features a search interface where users can enter queries and receive ranked lists of relevant documents based on similarity scores (http://127.0.0.1:5000/query confirms connection). Additionally, the UI supports interactive visualization of document clusters and similarity networks, enabling users to gain insights into the underlying structure of the document corpus (port http://127.0.0.1:5000/  to confirm app.py successful execution).


### Interfaces

1.	API Endpoints: The system exposes RESTful API endpoints for programmatic access to its functionalities. These endpoints enable developers to interact with the system programmatically, performing tasks such as querying for document similarities and retrieving indexed documents.
2.	User Interface: The UI component provides a graphical interface for users to interact with the system. It features search interfaces, and interactive components for querying, exploring, and analyzing document similarities.
3.	Data Ingestion Interfaces: The system supports various data ingestion interfaces for importing textual data from external sources.  web scraping utilities, allowing users to ingest data from sources.

### Implementation

1.	Technology Stack: The system is implemented using a combination of programming languages, frameworks, and libraries. Python serves as the primary programming language, using libraries such as scikit-learn for NLP tasks and Flask for building RESTful APIs. 
2.	Scalability and Performance: Implementation considerations include scalability and performance optimizations to handle large volumes of textual data efficiently. Techniques such as distributed computing, parallel processing, and caching are employed to ensure optimal system performance under varying workloads.

### Dependencies

--> The project relies on the following dependencies:
•	Python 3.10+
•	scikit-learn 1.2+
•	Scrapy 2.11+
•	Flask 2.2+
•	Requests
--> These dependencies can be installed via pip using the following commands:
*	pip install scikit-learn scrapy Flask requests or 
*	conda install scikit-learn scrapy Flask requests


### CONCLUSION

The document similarity analysis system demonstrates success in providing a extensive solution for users to perform efficient content-based searches. Through the integration of web crawling, indexing, and query processing components, the system enables users to input queries and retrieve relevant documents accurately. The user interface facilitates interaction with the system, allowing for intuitive query input and visualization of search results. Outputs from the system include top-K ranked documents based on similarity scores, presented in a clear and understandable format. However, caution should be exercised regarding the scalability of the system, particularly with large text corpora, as it may impact performance and resource utilization. Additionally, proper error handling and input validation should be implemented to ensure system stability and security, particularly when handling user-generated queries.