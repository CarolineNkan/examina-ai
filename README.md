Examina — AI Exam Prep Assistant
Reimagining studying with adaptive exam modes, instant feedback, and personalized learning insights.

🚀 Overview

Examina is an AI-powered exam preparation assistant built for the CS Girlies “Make Learning Cool Again” Hackathon.

It transforms your uploaded notes into:

Auto-generated questions

Explanations powered by GPT-4

Score breakdown via Plotly charts

Multiple exam modes (Calm / Hardcore / Timed)

(Phase 2) Multilingual support via Translate API

(Phase 3) Global Leaderboard

Built using Flask + Streamlit + OpenAI + Plotly + Pandas.

🧩 Features (Phase 1)
Feature	Status
Notes upload (PDF/Text)	✅
GPT-4 question generator	✅
Web search context expansion	🟡 placeholder
Flask backend orchestration	✅
Streamlit UI	🟡 scaffold
Plotly weak-topic charts	🟡 in progress
Multilingual mode	🔜 Phase 2
Global leaderboard	🔜 Phase 3
🏗️ Architecture Diagram

architecture_v1.png
(Includes Translate API “Phase 2” placeholder)

Notes Upload → Web Search API → OpenAI GPT → Flask Backend → Streamlit UI → Plotly Charts
                              ↘︎ Future: Translate API

🎨 Branding & Logo

Located in /static/:

logo_light.png

logo_dark.png

logo_compact_light.png

logo_compact_dark.png

logo_icon_blue.png

logo_icon_red.png

Color palette:

Mode	Hex
Softcore	#90CAF9
Hardcore	#E57373
Multilingual	#FFD54F
Text	#FFFFFF
📂 Folder Structure
examina-ai/
│   app.py
│   requirements.txt
│   README.md
│
├── static/
│   ├── logo_light.png
│   ├── logo_dark.png
│   ├── logo_compact_light.png
│   ├── logo_compact_dark.png
│   ├── logo_icon_blue.png
│   └── logo_icon_red.png
│
├── templates/
│   └── (HTML files for Flask - coming next)
│
├── demo_assets/
│   ├── architecture_v1.png
│   └── audio/
│        ├── exam_tension.mp3
│        ├── lofi_intro.mp3
│        └── ATTRIBUTION.txt
│
└── venv310/   (ignored)

🛠️ Tech Stack

Backend: Flask

Frontend: Streamlit

AI Model: OpenAI GPT-4

Charts: Plotly

Data: Pandas

Branding: Figma Make

Audio: Bensound (licensed)

🎧 Audio Credits

All audio files are properly licensed and stored in /demo_assets/audio/.

Music by https://www.bensound.com/free-music-for-videos
License code: BGEOOFRI6JUOFYJG
Artist: Benjamin Tissot (Bensound)

Music by https://www.bensound.com/free-music-for-videos
License code: PXOKKPYC0RNQJBUG
Artist: Benjamin Tissot (Bensound)

🧪 Running Locally

Activate environment

source venv310/Scripts/activate  # Windows


Run Flask

python app.py


Run Streamlit

streamlit run app.py


Both should open:

Flask → http://127.0.0.1:5000

Streamlit → http://localhost:8501

📌 Phase 2 Roadmap

Add Translate API for multilingual exam mode

Add leaderboard feature

Add LLM personalization

Add UI polish + transitions

🙌 Credits

Built by Caroline Nkan for the CS Girlies Hackathon — November 2025.