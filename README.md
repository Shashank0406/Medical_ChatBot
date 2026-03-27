# 🏥 Medical ChatBot

A sophisticated AI-powered medical assistant that leverages Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers to medical questions. Built with modern LLM technologies and designed for reliable medical information retrieval.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.1-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)
![AWS](https://img.shields.io/badge/AWS-Deployed-FF9900.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌐 Live Demo

**Try the Medical ChatBot now**: [https://shashankmedicalchatbot.streamlit.app](https://shashankmedicalchatbot.streamlit.app) ✨

*Note: The live demo is hosted on Streamlit Cloud. Start asking medical questions and get instant AI-powered responses!*

## ✨ Features

- 🤖 **RAG-Powered Responses**: Uses Retrieval-Augmented Generation for accurate medical information
- 🔍 **Vector Search**: Pinecone-based semantic search for relevant medical documents
- 💬 **Interactive Chat Interface**: Clean, user-friendly web interface for asking medical questions
- 🚀 **Fast LLM Inference**: Powered by Groq's Llama 3.1 8B model for quick responses
- 🐳 **Docker Support**: Easy deployment with included Dockerfile
- 🔐 **Environment Configuration**: Secure API key management with `.env` files
- 📚 **Smart Context**: Retrieves top 3 most relevant documents for each query
- ☁️ **AWS-Ready**: Fully containerized and deployed on AWS with ECS/Fargate
- 🔄 **CI/CD Pipeline**: Automated testing, building, and deployment via GitHub Actions

## 🛠️ Tech Stack

- **Framework**: Flask
- **LLM Orchestration**: LangChain
- **Vector Database**: Pinecone
- **Language Model**: Groq (Llama 3.1 8B Instant)
- **Embeddings**: Sentence Transformers
- **Document Processing**: PyPDF
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker
- **Cloud Platform**: AWS (EC2, ECS, Fargate, ECR, CloudWatch)
- **CI/CD**: GitHub Actions
- **Secrets Management**: AWS Secrets Manager

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- API Keys:
  - Groq API key (from [Groq Console](https://console.groq.com))
  - Pinecone API key (from [Pinecone Console](https://app.pinecone.io))
  - HuggingFace API key (for embeddings)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Medical_ChatBot.git
   cd Medical_ChatBot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here(optional)
   ```

## 💻 Usage

### Running the Flask Application

```bash
python app.py
```

The application will start on `http://localhost:8080/`

### Using the Chat Interface

1. Open your browser and navigate to `http://localhost:8080/`
2. Type your medical question in the chat box
3. The chatbot will retrieve relevant medical documents and provide a concise answer
4. Continue the conversation as needed

### Example Questions

- "What are the symptoms of diabetes?"
- "How is hypertension managed?"
- "What causes heart disease?"

## 🐳 Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t medical-chatbot .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 --env-file .env medical-chatbot
   ```

3. **Access the application**
   Open `http://localhost:8080/` in your browser

## � AWS Deployment with CI/CD

### Prerequisites for AWS Deployment

- AWS Account with appropriate permissions
- EC2 instance or Elastic Container Service (ECS) setup
- AWS IAM credentials configured
- GitHub repository with Actions enabled

### GitHub Actions CI/CD Pipeline

The project uses GitHub Actions for automated testing, building, and deployment to AWS.

#### Automated Workflow

Create `.github/workflows/deploy.yml` for automatic deployment:

#### GitHub Secrets Configuration

Add the following secrets to your GitHub repository (`Settings > Secrets and variables > Actions`):

- `AWS_ACCESS_KEY_ID`: Your AWS access key
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key
- `AWS_ACCOUNT_ID`: Your AWS account ID (12-digit number)
- `GROQ_API_KEY`: Groq API key
- `PINECONE_API_KEY`: Pinecone API key

### AWS ECS Deployment

#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

## Install docker in instance

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

6. Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one

## �📁 Project Structure

```
Medical_ChatBot/
├── app.py                 # Main Flask application
├── mediapp.py            # Steamlit app 
├── medicalapp.py         # Additional app configuration
├── store_index.py        # Vector store indexing script
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── setup.py              # Package setup configuration
├── .env.example          # Environment variables template
│
├── src/
│   ├── __init__.py
│   ├── helper.py         # Helper functions for embeddings
│   ├── prompt.py         # System prompts for the LLM
│   └── __pycache__/
│
├── templates/
│   └── chat.html         # Chat interface template
│
├── static/
│   └── style.css         # Styling for web interface
│
├── data/                 # Medical documents storage
│
├── research/
│   └── ttrails.ipynb     # Research and experimentation notebook
│
└── README.md             # This file
```

## 🔧 Configuration

### Customizing the Medical Assistant

Edit `src/prompt.py` to modify the system prompt for different medical specialties:

```python
sys_prompt = (
    "You are a Medical assistant for answering questions related to medical conditions. "
    "Use the following retrieved documents to answer the question. "
    "If you don't know the answer, say you don't know."
    "Use 3 sentences to answer the question. Keep the answer concise and to the point."
    "{context}"
)
```

### Adjusting Search Parameters

In `app.py`, modify the retriever configuration:
- `search_type`: Change to "mmr" for Maximum Marginal Relevance search
- `search_kwargs={"k":3}`: Increase/decrease number of retrieved documents

## 📚 How It Works

1. **Document Processing**: Medical documents are converted to embeddings using Sentence Transformers
2. **Vector Storage**: Embeddings are stored in Pinecone for fast semantic search
3. **Query Processing**: User questions are also converted to embeddings
4. **Retrieval**: Top 3 most relevant documents are retrieved from Pinecone
5. **Generation**: Groq's Llama 3.1 model generates concise answers based on retrieved context
6. **Response**: Answer is returned to the user through the web interface

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋 Support

If you have any questions or run into issues, please:
- Check the existing issues on GitHub
- Create a new GitHub issue with a detailed description
- Include your setup details and error messages

## 🎯 Future Enhancements

- [x] AWS deployment with CI/CD
- [x] Docker containerization
- [x] GitHub Actions automation
- [ ] Multi-language support
- [ ] Medical image analysis integration
- [ ] Patient history tracking
- [ ] Advanced filtering by medical specialty
- [ ] Real-time document indexing
- [ ] Enhanced caching for faster responses
- [ ] Authentication and user profiles
- [ ] Load balancing and auto-scaling
- [ ] Advanced monitoring and alerting
- [ ] Database integration for conversation history

## 📧 Contact

**Author**: Shashank Kurakula  
**Email**: shashankkurakula5@gmail.com

---

⭐ If you found this project helpful, please consider giving it a star!