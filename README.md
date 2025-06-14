# 🔍 Smart Search Tool

A powerful search tool built with Streamlit and Pinecone for intelligent course searching using vector embeddings.

## 🌟 Features

- Vector-based semantic search using Pinecone
- HuggingFace embeddings for accurate text representation
- Streamlit-based user interface for easy interaction
- Course metadata storage and retrieval
- Real-time search results

## 🔧 Project Structure
```
smart-search-tool/
├── .streamlit/
│   └── secrets.toml         # Configuration secrets
├── helpers/
│   ├── api.py              # API integration
│   ├── courses.py          # Course management
│   └── db.py              # Database operations
├── models/
│   ├── __init__.py
│   └── course.py          # Course data model
├── src/
│   ├── __init__.py
│   └── streamlit_ui.py    # Streamlit UI components
├── venv/                  # Virtual environment
├── .gitignore
├── main.py               # Main application entry
├── README.md
├── requirements.txt      # Project dependencies
└── utils.py             # Utility functions
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Pinecone API Key
- Virtual Environment

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MayankDiwate/Smart-Search-Tool.git
cd Smart-Search-Tool
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your `.streamlit/secrets.toml`:
```toml
[secrets]
PINECONE_API_KEY = "your-pinecone-api-key"
PINECONE_API_HOST = "your-pinecone-api-host-key"
```

### Running the Application

```bash
streamlit run main.py
```

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) - Web interface
- [Pinecone](https://www.pinecone.io/) - Vector database
- [LangChain](https://python.langchain.com/) - Language model tools
- [HuggingFace](https://huggingface.co/) - Embeddings
- [Sentence Transformers](https://www.sbert.net/) - Text embeddings

## 📦 Dependencies

- streamlit
- beautifulsoup4
- requests
- langchain
- langchain-community
- langchain-huggingface
- pinecone-client
- sentence-transformers
- pydantic
- python-dotenv

## 💡 Usage

1. Launch the application using Streamlit
2. Input your search query in the search bar
3. View semantically relevant course results
4. Explore course details and metadata

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
