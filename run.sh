source venv/bin/activate
cd react-frontend/
npm run build
cd ..
python3 flask-backend/main.py
