from urllib import request
import time,os
os.system('clear')
print("""
  _    _                      _         
 | |  | |                    | |        
 | |__| |_  ___ __ ___   ___ | | ____ _ 
 |  __  \ \/ / '_ ` _ \ / _ \| |/ / _` |
 | |  | |>  <| | | | | | (_) |   < (_| |
 |_|  |_/_/\_\_| |_| |_|\___/|_|\_\__,_|
                                        
                                                                                        
""")
time.sleep(3)
print("\x1b[32m1: Find admin panel")
x = input("--> ")

if x == "1":
    print("\x1b[32m// Example: https://www.google.com")
    url =  input("\x1b[32mEnter Site --> ")
    lists = [
        'admin',
'administrator',
'admin1',
'admin2',
'admin3',
'admin4',
'admin5',
'cpanel',
'usuarios',
'usuario',
'administrator',
'moderator',
'webadmin',
'adminarea',
'bb-admin',
'adminLogin',
'admin_area',
'panel-administracion',
'instadmin',
'memberadmin',
'administratorlogin',
'adm',
'admin/account.php',
'admin/index.php',
'admin/login.php',
'admin/admin.php',
'admin/account.php',
'admin_area/admin.php',
'admin_area/login.php',
'siteadmin/login.php',
'siteadmin/index.php',
'siteadmin/login.html',
'admin/account.html',
'admin/index.html',
'admin/login.html',
'admin/admin.html',
'admin_area/index.php',
'bb-admin/index.php',
'bb-admin/login.php',
'bb-admin/admin.php',
'admin/home.php',
'admin_area/login.html',
'admin_area/index.html',
'admin/controlpanel.php',
'admin.php',
'admincp/index.asp',
'admincp/login.asp',
'admincp/index.html',
'admin/account.html',
'adminpanel.html',
'webadmin.html',
'webadmin/index.html',
'webadmin/admin.html',
'webadmin/login.html',
'admin/admin_login.html',
'admin_login.html',
'panel-administracion/login.html',
'admin/cp.php',
'cp.php',
'administrator/index.php',
'administrator/login.php',
'nsw/admin/login.php',
'webadmin/login.php',
'admin/admin_login.php',
'admin_login.php',
'administrator/account.php',
'administrator.php',
'admin_area/admin.html',
'pages/admin/admin-login.php',
'admin/admin-login.php',
'admin-login.php',
'bb-admin/index.html',
'bb-admin/login.html',
'acceso.php',
'bb-admin/admin.html',
'admin/home.html',
'login.php',
'modelsearch/login.php',
'moderator.php',
'moderator/login.php',
'moderator/admin.php',
'account.php',
'pages/admin/admin-login.html',
'admin/admin-login.html',
'admin-login.html',
'controlpanel.php',
'admincontrol.php',
'admin/adminLogin.html',
'adminLogin.html',
'admin/adminLogin.html',
'home.html',
'rcjakar/admin/login.php',
'adminarea/index.html',
'adminarea/admin.html',
'webadmin.php',
'webadmin/index.php',
'webadmin/admin.php',
'admin/controlpanel.html',
'admin.html',
'admin/cp.html',
'cp.html',
'adminpanel.php',
'moderator.html',
'administrator/index.html',
'administrator/login.html',
'user.html',
'administrator/account.html',
'administrator.html',
'login.html',
'modelsearch/login.html',
'moderator/login.html',
'adminarea/login.html',
'panel-administracion/index.html',
'panel-administracion/admin.html',
'modelsearch/index.html',
'modelsearch/admin.html',
'admincontrol/login.html',
'adm/index.html',
'adm.html',
'moderator/admin.html',
'user.php',
'account.html',
'controlpanel.html',
'admincontrol.html',
'panel-administracion/login.php',
'wp-login.php',
'adminLogin.php',
'admin/adminLogin.php',
'home.php',
'admin.php',
'adminarea/index.php',
'adminarea/admin.php',
'adminarea/login.php',
'panel-administracion/index.php',
'panel-administracion/admin.php',
'modelsearch/index.php',
'modelsearch/admin.php',
'admincontrol/login.php',
'adm/admloginuser.php',
'admloginuser.php',
'admin2.php',
'admin2/login.php',
'admin2/index.php',
'usuarios/login.php',
'adm/index.php',
'adm.php',
'affiliate.php',
'adm_auth.php',
'memberadmin.php',
'administratorlogin.php',
'admin/account.asp',
'admin/index.asp',
'admin/login.asp'
'admin/admin.asp',
'admin/account.asp',
'admin_area/admin.asp',
'admin_area/login.asp',
'siteadmin/login.asp',
'siteadmin/index.asp',
'siteadmin/login.asp',
'admin/account.asp',
'admin/index.asp',
'admin/login.asp',
'admin/admin.asp',
'admin_area/index.asp',
'bb-admin/index.asp',
'bb-admin/login.asp',
'bb-admin/admin.asp',
'admin/home.asp',
'admin_area/login.asp',
'admin_area/index.asp',
'admin/controlpanel.asp',
'admin.asp',
'admincp/index.asp',
'admincp/login.asp',
'admincp/index.asp',
'admin/account.asp',
'adminpanel.asp',
'webadmin.asp',
'webadmin/index.asp',
'webadmin/admin.asp',
'webadmin/login.asp',
'admin/admin_login.asp',
'admin_login.asp',
'panel-administracion/login.asp',
'admin/cp.asp',
'cp.asp',
'administrator/index.asp',
'administrator/login.asp',
'nsw/admin/login.asp',
'webadmin/login.asp',
'admin/admin_login.asp',
'admin_login.asp',
'administrator/account.asp',
'administrator.asp',
'admin_area/admin.asp',
'pages/admin/admin-login.asp',
'admin/admin-login.asp',
'admin-login.asp',
'bb-admin/index.asp',
'bb-admin/login.asp',
'acceso.asp',
'bb-admin/admin.asp',
'admin/home.asp',
'login.asp',
'modelsearch/login.asp',
'moderator.asp',
'moderator/login.asp',
'moderator/admin.asp',
'account.asp',
'pages/admin/admin-login.asp',
'admin/admin-login.asp',
'admin-login.asp',
'controlpanel.asp',
'admincontrol.asp',
'admin/adminLogin.asp',
'adminLogin.asp',
'admin/adminLogin.asp',
'home.asp',
'rcjakar/admin/login.asp',
'adminarea/index.asp',
'adminarea/admin.asp',
'webadmin.asp',
'webadmin/index.asp',
'webadmin/admin.asp',
'admin/controlpanel.asp',
'admin.asp',
'admin/cp.asp',
'cp.asp',
'adminpanel.asp',
'moderator.asp',
'administrator/index.asp',
'administrator/login.asp',
'user.asp',
'administrator/account.asp',
'administrator.asp',
'login.asp',
'modelsearch/login.asp',
'moderator/login.asp',
'adminarea/login.asp',
'panel-administracion/index.asp',
'panel-administracion/admin.asp',
'modelsearch/index.asp',
'modelsearch/admin.asp',
'admincontrol/login.asp',
'adm/index.asp',
'adm.asp',
'moderator/admin.asp',
'user.asp',
'account.asp',
'controlpanel.asp',
'admincontrol.asp',
'panel-administracion/login.asp',
'wp-login.asp',
'adminLogin.asp',
'admin/adminLogin.asp',
'home.asp',
'admin.asp',
'adminarea/index.asp',
'adminarea/admin.asp',
'adminarea/login.asp',
'panel-administracion/index.asp',
'panel-administracion/admin.asp',
'modelsearch/index.asp',
'modelsearch/admin.asp',
'admincontrol/login.asp',
'adm/admloginuser.asp',
'admloginuser.asp',
'admin2.asp',
'admin2/login.asp',
'admin2/index.asp',
'usuarios/login.asp',
'adm/index.asp',
'adm.asp',
'affiliate.asp',
'adm_auth.asp',
'memberadmin.asp',
'administratorlogin.asp'
    ]
    for i in lists:
        Nurl = url+"/"+i
        try:
            openurl = request.urlopen(Nurl)
            print("\x1b[32m[+]Found")
            print(Nurl)
            
            break
        except:
            print("\x1b[31m[-]Not Found")
            print(Nurl)
else:
    print("\x1b[31m Please Try Again . . .")


input("\x1b[0m\nEnter For Exit : ")
