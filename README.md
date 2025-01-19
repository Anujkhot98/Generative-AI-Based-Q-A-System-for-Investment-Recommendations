# Generative-AI-Based-Q-A-System-for-Investment-Recommendations
This project implements a real-time Q&A bot designed to provide conversational AI responses based on user inputs. It utilizes FastAPI for backend development and WebSocket for seamless, streaming communication with the frontend. Powered by the Llama-3.3-70b Versatile model via LangChain-Groq, the bot offers high-performance inference with token-by-token streaming responses.

# Features
Real-time, token-by-token streaming of responses.
Powered by Llama-3.3 model with Groq Cloud for fast inference.
Built with FastAPI and WebSocket for seamless communication.

# Installation
Clone the repository:
git clone <repo-url>
cd <repo-folder>

Set up a Python environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Replace groq_api_key in the code with your actual API key.

Usage
Start the FastAPI server:

uvicorn main:app --reload

Connect to the WebSocket endpoint /ws from a frontend client to interact with the bot.

