from app import create_app, db
from app.models import Candidate, Department

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Candidate': Candidate, 'Department': Department}

if __name__ == '__main__':
    # Auto-Setup on First Run
    try:
        from setup import setup_database
        setup_database()
    except Exception as e:
        print(f"Warning: Auto-setup failed ({e}). Attempting to start anyway...")

    app.run(debug=True)
