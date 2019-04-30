import web

db_host = 'ui0tj7jn8pyv9lp6.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'opjy6t791xm2rmns'
db_user = 'ngjzwqtz2zg37q2o'
db_pw = 'uk5dib72ra6mvzqj'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )