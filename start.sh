#!/bin/bash

# AI Doctor Assistant Startup Script

echo "🏥 Starting AI Doctor Assistant..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check for environment variables
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Please create a .env file with your API keys:"
    echo "GROQ_API_KEY=your_groq_api_key"
    echo "ELEVEN_API_KEY=your_elevenlabs_api_key"
    exit 1
fi

# Start the application
echo "🚀 Launching AI Doctor Assistant..."
python app.py