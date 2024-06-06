from ldap3 import Connection, Server, SIMPLE, ALL

LDAP_SERVER = 'eldap2.iut.univ-paris8.fr'
LDAP_BASE_DN = 'dc=iut,dc=univ-paris8,dc=fr'
LDAP_USER_DN = 'uid={},ou=people,' + LDAP_BASE_DN

def authenticate_with_ldap(username, password):
    print(f"Authenticating user: {username}")
    server = Server(LDAP_SERVER, get_info=ALL)
    user_dn = LDAP_USER_DN.format(username)
    try:
        conn = Connection(server, 
                          user=user_dn, 
                          password=password, 
                          authentication=SIMPLE, 
                          auto_bind=True)
        if conn.bind():
            print(f"User {username} authenticated successfully.")
            conn.unbind()
            return True
        else:
            print(f"LDAP connection failed for user {username}.")
    except Exception as e:
        print(f"LDAP authentication error for user {username}: {e}")

    print(f"Authentication failed for user {username}.")
    return False

authenticate_with_ldap('mtoure', 'muB436D77')
