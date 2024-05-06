import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')


config = {
            'server':           '2captcha.com', # can be also set to 'rucaptcha.com'
    		'apiKey':           api_key,
    		'softId':            123,
    		# 'callback':         'https://your.site/result-receiver', # if set, sovler with just return captchaId, not polling API for the answer
    		'defaultTimeout':    120,
    		'recaptchaTimeout':  600,
    		'pollingInterval':   10,
	    }

solver = TwoCaptcha(**config)

try:
    result = solver.keycaptcha(s_s_c_user_id          = 184015,
                            s_s_c_session_id       = 'c32c9934c68b2968bee0332b9346da42',
                            s_s_c_web_server_sign  = 'c93c8d136d5ee6ee6fe27ab2be54901d',
                            s_s_c_web_server_sign2 = 'eec85fcfeda28bffd7764d712d4089e7',
                            url                    = 'https://2captcha.com/ru/demo/keycaptcha'
                            # proxy                  = {
                            #                           'type': 'HTTPS',
                            #                           'uri': 'login:password@IP_address:PORT'}
                            )

        
except Exception as e:
    sys.exit(e)
    
else:
    sys.exit('result: ' + str(result))

    