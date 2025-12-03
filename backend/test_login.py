import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_login(username, password, role):
    session = requests.Session()
    
    # 1. Get CSRF token (if needed, but for simple test we might skip if CSRF is disabled or we parse it)
    # Actually, Flask-WTF requires CSRF. 
    # Let's try to parse it from the login page.
    response = session.get(f'{BASE_URL}/auth/login')
    if response.status_code != 200:
        print(f"[-] Failed to load login page: {response.status_code}")
        return

    csrf_token = None
    if 'csrf_token' in response.text:
        # Simple extraction (fragile but works for test)
        start = response.text.find('name="csrf_token" value="') + len('name="csrf_token" value="')
        end = response.text.find('"', start)
        csrf_token = response.text[start:end]
        print(f"[+] CSRF Token: {csrf_token}")
    else:
        print("[-] CSRF Token not found")
        return

    # 2. Post Login
    data = {
        'csrf_token': csrf_token,
        'username': username,
        'password': password,
        'remember_me': 'y'
    }
    
    # We need to simulate the headers
    headers = {
        'Referer': f'{BASE_URL}/auth/login'
    }

    response = session.post(f'{BASE_URL}/auth/login', data=data, headers=headers, allow_redirects=False)
    
    print(f"--- Login Test for {role} ({username}) ---")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 302:
        print(f"Redirect Location: {response.headers.get('Location')}")
        if '/dashboard' in response.headers.get('Location', ''):
            print("[+] Login SUCCESS (Redirected to Dashboard)")
        else:
            print("[-] Login Redirect Unexpected")
    else:
        print("[-] Login FAILED (No Redirect)")
        # Print flash messages if any (simple check)
        if 'Invalid username' in response.text:
            print("   Reason: Invalid username or password")
        elif 'pending approval' in response.text:
            print("   Reason: Account pending approval")
        else:
            print("   Reason: Unknown")
            # Print a snippet of the response to see errors
            print(response.text[:1000])

if __name__ == '__main__':
    test_login('admin', 'admin123', 'Admin')
    test_login('candidate0@example.com', 'password123', 'Applicant')
