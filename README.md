# 🏥 AI Doctor Assistant

Advanced Medical Image Analysis with Voice Interaction - An AI-powered healthcare assistant that combines computer vision and natural language processing to provide medical insights.

## ✨ Features

- 🎤 **Voice Recognition**: Speak naturally about your symptoms
- 👁️ **Medical Image Analysis**: AI-powered analysis of medical images
- 🔊 **Audio Response**: Natural-sounding voice responses
- 🩺 **Detailed Analysis**: Comprehensive medical assessments
- 📱 **Responsive Design**: Works on desktop and mobile devices

## 🚀 Live Demo

[Visit the live application](https://ai-doctor-2-0-voice-and-vision.vercel.app)

## 🛠️ Technology Stack

- **Frontend**: Gradio with custom CSS animations
- **AI Models**: 
  - Groq (Whisper for speech-to-text, Llama for image analysis)
  - ElevenLabs (Text-to-speech)
- **Backend**: Python
- **Deployment**: Vercel

## 📋 Prerequisites

- Python 3.8+
- Groq API Key ([Get it here](https://console.groq.com/))
- ElevenLabs API Key ([Get it here](https://elevenlabs.io/))

## 🔧 Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-doctor-assistant.git
cd ai-doctor-assistant
```

### 2. Install Dependencies

#### Using pip:
```bash
pip install -r requirements.txt
```

#### Using pipenv:
```bash
pipenv install
pipenv shell
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
ELEVEN_API_KEY=your_elevenlabs_api_key_here
```

### 4. Install System Dependencies

#### Windows:
1. Download FFmpeg from [FFmpeg Downloads](https://ffmpeg.org/download.html)
2. Extract and add to PATH
3. Install PortAudio from [PortAudio Downloads](http://www.portaudio.com/download.html)

#### macOS:
```bash
brew install ffmpeg portaudio
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:7860`

## 🌐 Deployment Instructions

### Deploy to Vercel

#### Method 1: Using Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Set Environment Variables**:
   ```bash
   vercel env add GROQ_API_KEY
   vercel env add ELEVEN_API_KEY
   ```

5. **Redeploy with Environment Variables**:
   ```bash
   vercel --prod
   ```

#### Method 2: Using Vercel Dashboard

1. **Connect GitHub Repository**:
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "New Project"
   - Import your GitHub repository

2. **Configure Environment Variables**:
   - In project settings, go to "Environment Variables"
   - Add:
     - `GROQ_API_KEY`: Your Groq API key
     - `ELEVEN_API_KEY`: Your ElevenLabs API key

3. **Deploy**:
   - Vercel will automatically deploy your application
   - Your app will be available at `https://your-project-name.vercel.app`

### Deploy to Other Platforms

#### Hugging Face Spaces
1. Create a new Space on [Hugging Face](https://huggingface.co/spaces)
2. Choose "Gradio" as the SDK
3. Upload your files
4. Add secrets in Space settings:
   - `GROQ_API_KEY`
   - `ELEVEN_API_KEY`

#### Railway
1. Connect your GitHub repository to [Railway](https://railway.app)
2. Add environment variables in the dashboard
3. Deploy automatically

## 📁 Project Structure

```
ai-doctor-assistant/
├── app.py                      # Main Gradio application
├── brain_of_the_doctor.py      # Image analysis logic
├── voice_of_the_patient.py     # Speech-to-text processing
├── voice_of_the_doctor.py      # Text-to-speech processing
├── requirements.txt            # Python dependencies
├── vercel.json                # Vercel configuration
├── .env                       # Environment variables (local)
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
├── acne.jpg                   # Sample medical image
├── dandruff-optimized.webp    # Sample medical image
└── skin_rash.jpg              # Sample medical image
```

## 🔒 Security & API Keys

**IMPORTANT**: This repository is safe to make public because:
- ✅ API keys are stored in environment variables (`.env` file)
- ✅ `.env` file is excluded via `.gitignore`
- ✅ No hardcoded credentials in the source code
- ✅ All sensitive data is handled through environment variables

### 🔑 API Keys Setup

#### Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up/Login
3. Generate an API key
4. Add to your `.env` file: `GROQ_API_KEY=your_key_here`

#### ElevenLabs API Key
1. Visit [ElevenLabs](https://elevenlabs.io/)
2. Sign up/Login
3. Go to Profile → API Keys
4. Generate an API key
5. Add to your `.env` file: `ELEVEN_API_KEY=your_key_here`

## 🎯 Usage Instructions

1. **Record Audio**: Click the microphone and describe your symptoms
2. **Upload Image**: Select a clear medical image for analysis
3. **Submit**: Click "Analyze with AI Doctor" button
4. **Review Results**: Read the analysis and listen to the audio response

## ⚠️ Important Disclaimers

- This application is for **educational purposes only**
- **Always consult qualified healthcare professionals** for medical advice
- Do not use this as a substitute for professional medical diagnosis
- The AI responses are based on image analysis and should not be considered definitive medical opinions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Faizan Khan**
- GitHub: [@faizankhan2595](https://github.com/faizankhan2595)
- LinkedIn: [Faizan Khan](https://linkedin.com/in/faizan-khan-ai)

## 🚀 Quick Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/faizankhan2595/ai-doctor-2.0-voice-and-vision&env=GROQ_API_KEY,ELEVEN_API_KEY)

1. Click the deploy button above
2. Add your API keys in environment variables
3. Deploy instantly!

## 🙏 Acknowledgments

- Groq for providing fast AI inference
- ElevenLabs for natural voice synthesis
- Gradio for the amazing web interface framework
- The open-source community for various tools and libraries

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/ai-doctor-assistant/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about the error and your environment

---

**Built with ❤️ for accessible healthcare technology**