import time
from fyers_api import fyersModel
from fyers_api import accessToken
from pyotp import TOTP
from selenium import webdriver
from selenium.webdriver.common.by import By

client_id = "APD18S1PBD-100"
secret_key = "MATZUHKQU1"
redirect_uri = "https://www.google.com/"

username = 'XU04053'
totp = 'abcdef'
pin1 = '1'
pin2 = '1'
pin3 = '1'
pin4 = '1'

def generate_auth_code():
    session = accessToken.SessionModel(client_id=client_id, secret_key=secret_key,
                                       redirect_uri=redirect_uri, response_type='code',
                                       grant_type='authorization-code')

    response = session.generate_authcode()

    driver = webdriver.Chrome()
    driver.get(response)

    driver.find_element(By.ID, 'login_client_id').click()
    driver.find_element(By.ID, 'fy_client_id').send_keys(username)
    driver.find_element(By.ID, 'clientIdSubmit').click()
    time.sleep(5)
    t = TOTP(totp).now()
    print(t)

    driver.find_element(By.XPATH('//*[@="first"]')).send_keys(t[0])
    driver.find_element(By.XPATH('//*[@="second"]')).send_keys(t[1])
    driver.find_element(By.XPATH('//*[@="third"]')).send_keys(t[2])
    driver.find_element(By.XPATH('//*[@="fourth"]')).send_keys(t[3])
    driver.find_element(By.XPATH('//*[@="fifth"]')).send_keys(t[4])
    driver.find_element(By.XPATH('//*[@="sixth"]')).send_keys(t[5])

    driver.find_element(By.XPATH('//*[@id="confirmOtpSubmit"]')).click()
    time.sleep(5)

    driver.find_element(By.ID("verify-pin-page")).find_element(By.ID("first")).send_keys(pin1)
    driver.find_element(By.ID("verify-pin-page")).find_element(By.ID("second")).send_keys(pin2)
    driver.find_element(By.ID("verify-pin-page")).find_element(By.ID("third")).send_keys(pin3)
    driver.find_element(By.ID("verify-pin-page")).find_element(By.ID("fourth")).send_keys(pin4)

    driver.find_element(By.XPATH('//*[@id="verifyPinSubmit"]')).click()
    time.sleep_code=(5)

    newurl = driver.current_url
    auth_code = newurl[newurl.index('auth_code=')+10:newurl.index('&state')]
    driver.quit()
    return auth_code


auth_code = generate_auth_code()
print(auth_code)


