import win32api
import win32net

import yaml

def find_user(path):
    '''
    Function detects if a user is connected to a given
    IP with VNC Client 
    '''
    # [[user1, user2], last known user]
    users = [[], None]

    try:
        # get the total number of lines for this logfile
        for line_counter, line in enumerate(list(open(path, 'r'))):
            line_counter+=1

        # read lines in reversed order and index them
        for index, line in enumerate(reversed(list(open(path, 'r'))), 1):
            
            # ... until a line starts with this string
            if line.startswith('<13>'):

                # check if a user has logged in and store user name & ip
                if 'Connections: authenticated:' in line:
                    user_ip = line[line.find('authenticated: ')+14:].split()[0]
                    user = line[line.find(', as ')+4:].split()[0]

                    # calculate a starting line for searching a user loggout
                    # beginning from the current line to the bottom of the logfile
                    start_line = line_counter - index
                    user_flag = 'connected'

                    for line in list(open(path, 'r'))[start_line:]:

                        if 'Connections: disconnected: '+ user_ip in line:
                            user_flag = 'disconnected'
                            users[1] = user
                            break
                        else:
                            pass

                    if user_flag == 'connected':
                        users[0].append(user)
                    else:
                        pass

                else:
                    pass

            else:
                pass

        if users[0] == []:
            users[0].append('no user connected')

        if users[1] == None:
            users[1] = 'No previous user'

    except:
        users[0].append('RealVNC not installed.')
        users[1] = 'No previous user'

    return users

def connect(ip):
    '''
    Function is for connecting to given IP within
    the network with passing the correct credentials
    '''
    
    username = 'puma'
    password = 'pumapuma'

    access_dict = {}
    access_dict['remote'] = r'\\' + ip + r'\C$'
    access_dict['password'] = password
    access_dict['username'] = username
    try:
        win32net.NetUseAdd(None, 2, access_dict)
    except:
        pass

    return None

def ip_list():
    return [r'REMOTECOMPUTER']

def load_user_names():
    return yaml.load(open('usernames.yaml', 'r'))

def get_user_name(name_dict, short_name):

	if short_name in name_dict:
		return name_dict[short_name]
	return "Name not found..."
