#  Smart Image Captioning API

A modern backend API that automatically generates SEO-friendly captions and hashtags for images using GenAI.

Built with **FastAPI**, **MongoDB**, **Cloudinary**, and **Google Gemini AI**.

## 🚀 Features
- **Smart Image Upload:** Direct upload to Cloudinary (no local storage required).
- **AI Analysis:** Uses Google Gemini Vision to understand image context.
- **Auto-Captioning:** Generates catchy, human-like captions for social media.
- **Hashtag Generation:** Creates 5 relevant, trending hashtags.
- **Production Architecture:** Modular folder structure (Controllers, Services, Utils).
- **Scalable:** Implements global exception handling and Pydantic validation.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Framework:** FastAPI
- **Database:** MongoDB (PyMongo)
- **Cloud Storage:** Cloudinary
- **AI Model:** Google Gemini 
- **Tools:** Uvicorn, Python-Multipart, Dotenv

## 📂 Project Structure
```text
SMART IMAGE CAPTIONING/
├── public/                 # Static files
├── src/
│   ├── controllers/        # Business logic (Upload + AI + DB)
│   ├── models/             # Pydantic data schemas
│   ├── routes/             # API Endpoints
│   ├── services/           # External API logic (Cloudinary/Gemini)
│   ├── utils/              # Standard Responses & Error Handling
│   ├── config.py           # Environment variables
│   ├── database.py         # DB Connection
│   └── main.py             # App entry point
└── requirements.txt        # Dependencies