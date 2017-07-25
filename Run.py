# coding=utf-8
# from app import AppController, DashboardController, HostPortController, ApiController, JarController, AgentController, LogController, CapController, \
#     JsfController, UserController,HostController,AuthorityController, app,SearchController
from app import app,ScannerController
"""
lazyScanner 扫描
"""
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', debug=True, port=8093)