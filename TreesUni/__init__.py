import os
if os.environ.get('SITE_STATUS') == 'production':
  import pymysql
  pymysql.install_as_MySQLdb()
