from fastapi import APIRouter

PROJECT_URL='https://xskmowjtfufmqdhhtrgk.supabase.co'

API_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhza21vd2p0ZnVmbXFkaGh0cmdrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ4NTUxOTIsImV4cCI6MjA4MDQzMTE5Mn0.ugaIRMa5hwu7wTQbX9oi0Q-rrG0hokhQihqPHPqlWlY'

router = APIRouter()

@router.get('/projects')
def get_projects():
    return "success"