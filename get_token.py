from fyers_api import accessToken

client_id = "APD18S1PBD-100"
secret_key = "MATZUHKQU1"
redirect_uri = "https://www.google.com/"

response_type = "code"
state = "sample_state"
grant_type = "authorization_code"

# auth_code = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2OTA0MzM4MjMsImV4cCI6MTY5MDQ2MzgyMywibmJmIjoxNjkwNDMzMjIzLCJhdWQiOiJbXCJkOjFcIiwgXCJkOjJcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYVTA0MDUzIiwib21zIjoiSzEiLCJoc21fa2V5IjoiYjViNDQ0ZDY5YzY5Nzc3YTU1Nzg5NzcyZTBkYWEzNDY3ZDcwYjE1YmRlZjA4MTRlNDVhYTZkMGEiLCJub25jZSI6IiIsImFwcF9pZCI6IkFQRDE4UzFQQkQiLCJ1dWlkIjoiM2E4NDdjZGQzYWEyNGM3MzhkY2FiZTU5OGQyOTA0NDgiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.W6k6Qo83Eae0QNpVQU95IPpIOZDhB65Sl64zd-hYzl4'

session=accessToken.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type
)

# session.set_token(auth_code)

response = session.generate_authcode()
# response = session.generate_token()
print(response)
