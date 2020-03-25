from flask import Flask, render_template, url_for
from tools import find_user, connect, ip_list

app = Flask(__name__)

@app.route('/')
def index():
    user_stat = []
    for single_ip in ip_list():
        ip = single_ip
        connect(ip)
        path = ip + r'\C$\ProgramData\RealVNC-Service\vncserver.log'

        # check connection status
        
        user_stat.append(find_user(path))

    return render_template('index.html', simu_status = zip(ip_list(), user_stat))

if __name__ == '__main__':
    app.run(debug=True, host='10.16.64.137')