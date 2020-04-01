from flask import Flask, render_template, url_for
from tools import find_user, connect, ip_list, load_user_names, get_user_name

app = Flask(__name__)

@app.route('/')
def index():

    user_stat = []
    for single_ip in ip_list():

        # handle windows logon on every machine
        connect(single_ip)
        
        # get the actual & last users for every machine
        path = r'\\' + single_ip + r'\C$\ProgramData\RealVNC-Service\vncserver.log'     
        users = find_user(path)
        
        # Translate shortnames into realnames
        real_current_users = [get_user_name(load_user_names()['users'], user) for user in users[0]]
        real_last_user = get_user_name(load_user_names()['users'], users[1])
        user_stat.append([real_current_users, real_last_user])


    return render_template('index.html', simu_status = zip(ip_list(), user_stat))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')