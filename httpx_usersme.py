import httpx

login_payload = {
  "email": "user1@example.com",
  "password": "12345"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json= login_payload)
login_response_data = login_response.json()
print("Login response", login_response_data)
print("Status code", login_response.status_code)



headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers= headers)
print(users_me_response.request.headers)
print(users_me_response.json())
print("Status code", users_me_response.status_code)