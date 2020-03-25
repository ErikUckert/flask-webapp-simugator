import win32api
import win32net

def find_user(path):
    '''
    Function detects if a user is connected to a given
    IP with VNC Client 
    '''
    for line in reversed(list(open(path, 'r'))):
            if 'NtUserSession: auth' in line:
                user=line[line.find('auth ')+4:].split()[0]
                var = user
                break

            if 'Connections: disconnected' in line.rstrip():
                var = 'user logged out'
                break

            else:
                var = 'user not found'
    return var

def connect(ip):
    '''
    Function is for connecting to given IP within
    the network with passing the correct credentials
    '''
    
    username = 'puma'
    password = 'pumapuma'

    access_dict = {}
    access_dict['remote'] = ip + r'\C$'
    access_dict['password'] = password
    access_dict['username'] = username
    win32net.NetUseAdd(None, 2, access_dict)

    return None

def ip_list():
    return [r'\\DEMZKSI110016', r'\\DEMZKWD111245']