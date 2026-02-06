# Healthcare Chatbot AI

A modern, AI-powered healthcare assistant featuring a 3D interactive avatar and real-time symptom analysis. Built with FastAPI, Three.js, and Scikit-learn.

## Features

- **Interactive 3D Avatar**: A futuristic, animated 3D orb that reacts to conversations (built with Three.js).
- **Symptom Analysis**: Uses Natural Language Processing (NLP) to analyze symptoms and suggest potential conditions.
- **Modern Interface**: A responsive, dark-mode UI with glassmorphism effects.
- **Chat History**: Automatically saves and manages conversation history locally.
- **Department Booking**: Intelligent routing to appropriate medical departments.
- **Real-time Streaming**: "Typewriter" effect for bot responses for a natural serving experience.

## Prerequisites

- Python 3.7+

## Installation

### 1. Backend Setup

Navigate to the backend directory and install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

### 2. Model Training

Before running the API, train the chatbot model:

```bash
cd backend
python train.py
```
*This will generate `model_data.pkl` based on `intents.json`.*

## Usage

### 1. Start the API

Run the FastAPI backend:

```bash
cd backend
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`.

### 2. Launch the Frontend

Simply open `frontend/index.html` in your browser.

For a better experience (to avoid CORS issues with certain browser security settings), serve it locally:

```bash
# Using Python's built-in server
cd frontend
python -m http.server 3000
```
Then visit `http://localhost:3000`.

## Project Structure

```
Healthcare_Project/
├── backend/
│   ├── main.py          # FastAPI server
│   ├── chat.py          # Chatbot prediction logic
│   ├── train.py         # Model training script
│   ├── intents.json     # Knowledge base/Dataset
│   └── requirements.txt # Python dependencies
├── frontend/
│   ├── index.html       # Main UI
│   ├── script.js        # Frontend logic & Three.js 3D avatar
│   └── style.css        # Modern dark-mode styles
└── README.md
```
