import time
from app import create_app, db
from app.models import Candidate
from sqlalchemy import text

app = create_app()

def check_performance():
    with app.app_context():
        print("--- Database Performance Check ---")
        
        # 1. Connection Check
        start_time = time.time()
        try:
            db.session.execute(text('SELECT 1'))
            print(f"[+] Connection Check: OK ({time.time() - start_time:.4f}s)")
        except Exception as e:
            print(f"[-] Connection Check: FAILED ({e})")
            return

        # 2. Query Performance (Candidate Status Index)
        start_time = time.time()
        candidates = Candidate.query.filter_by(status='Applied').all()
        duration = time.time() - start_time
        print(f"[+] Query 'status=Applied': Found {len(candidates)} records in {duration:.4f}s")
        
        # 3. Query Performance (All Candidates)
        start_time = time.time()
        all_candidates = Candidate.query.all()
        duration = time.time() - start_time
        print(f"[+] Query 'all': Found {len(all_candidates)} records in {duration:.4f}s")

        print("--- Check Complete ---")

if __name__ == '__main__':
    check_performance()
