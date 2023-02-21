from urllib import request
from flask import *
import pymysql
from flask_mysqldb import MySQL

app = Flask(__name__)

"""app.config['MYSQL_HOST'] = "sql9.freesqldatabase.com"
app.config['MYSQL_USER'] = "sql9598467"
app.config['MYSQL_PASSWORD'] = "Yuv18canlI"
app.config['MYSQL_DB'] = "sql9598467"""

connection = pymysql.connect(
    # host='sql9.freesqldatabase.com',
    # user='sql9598557',
    # password='IXrxmb7PHv',
    # db='sql9598557'

    host='sql10.freesqldatabase.com',
    user='sql10599784',
    password='Kr1sh@08',
    db='sql10599784'

)

mysql = MySQL(app)

@app.route('/table')
def index():
    query="select * from table 1"
    conn=connection.cursor()
    conn.execute(query)
    result=conn.fetchall()
    return render_template('table.html',display=result)

@app.route('/all')
def all():
    return render_template("index.html")


@app.route('/magnitude',methods=['GET','POST'])
def magnitude():
    mag=float(request.form['magnitude'])
    print(mag)
    query="select count(*) from `earthquake` where mag > {}".format(mag)

    conn=connection.cursor()
    conn.execute(query)
    result=conn.fetchall()
    return render_template('count.html',display=result[0][0])

@app.route('/magnituderan',methods=['GET','POST'])
def magnituderan():
    mag1=float(request.form['magnitude1'])
    mag2=float(request.form['magnitude2'])
    print(mag1)
    conn=connection.cursor()
    query = "SELECT * FROM  earthquake WHERE mag >= %s AND mag <= %s"

    conn.execute(query, (mag1, mag2))

   # conn.execute(query)
    result=conn.fetchall()
    return render_template('table.html',display=result)

# Define a route to handle queries for earthquakes near a specified location
@app.route('/near_location')
def near_location():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    distance = request.args.get('distance', type=float)
    # Calculate the bounding box for the specified location and distance
    lat_min, lat_max = lat - (distance / 111.1), lat + (distance / 111.1)
    lon_min, lon_max = lon - (distance / (111.1 * cos(radians(lat)))), lon + (distance / (111.1 * cos(radians(lat))))
    earthquake = query_db('SELECT * FROM earthquake WHERE latitude >= %s AND latitude <= %s AND longitude >= %s AND longitude <= %s', (lat_min, lat_max, lon_min, lon_max))
    return render_template('earthquakes.html', earthquake=earthquake)


# Define a route to handle queries for earthquake clusters
@app.route('/clusters',methods=['GET','POST'])
def clusters():
    
    distance=float(request.form['distance'])


    
    query = "SELECT * FROM  earthquake WHERE mag > {}".format(distance) 

    conn=connection.cursor()
    conn.execute(query)
    result=conn.fetchall()
    return render_template('table.html',display=result)




@app.route('/largest_magnitude',methods=['GET','POST'])
def largest_magnitude():
    
    time1=float(request.form['time1'])
    time2=float(request.form['time2'])


    
    query = "SELECT MAX(mag) FROM theearth WHERE time between {} and {}".format(time1,time2) 

    conn=connection.cursor()
    conn.execute(query)
    result=conn.fetchall()
    return render_template('largestmag.html',display=result[0][0])




if __name__ == "__main__":
    app.run(debug=True)

  

