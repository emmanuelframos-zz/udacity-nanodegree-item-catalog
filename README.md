# e-Sports Game Catalog

## Description
An application to register games and its characters, considering release dates.
The application was built in [AngularJS](https://angularjs.org/) + [Bootstrap](http://getbootstrap.com/) and supports Google Plus authentication.

## Installing dependencies
- [Install](https://www.python.org/downloads/) Python 2.7
- [Install](http://flask.pocoo.org/docs/0.12/installation/) Flask
- [Install](http://initd.org/psycopg/docs/install.html) psycopg2 (PostgreSQL database adapter for Python)
- [Install](http://docs.sqlalchemy.org/en/latest/intro.html#installation-guide) SQLAlchemy
- [Install](https://developers.google.com/api-client-library/python/start/installation) Google API Python Client
- [Install](https://www.jetbrains.com/pycharm) PyCharm Community IDE for Python
- [Install](https://www.postgresql.org/download) PostgreSQL Database Server with pgAdmin Client

## Running e-Sports Game Catalog
- Certify that PostgreSQL service is running
- In pgAdmin, create the database and tables (scripts are found in **sql/e_sport_games.sql** file)
- Certify to configure database properties in **database.properties** file
- Configure **run task** on PyCharm such as:
![](http://imageshack.com/a/img924/9261/ewbH22.png?raw=true)
- Select **run task** and clik on Run or Debug button
- Access the application in [http://localhost:5000](http://localhost:5000)

## e-Sports Game Catalog Funcionalities
**Login** <br/>
![](https://imagizer.imageshack.us/v2/579x362q90/923/5h5ZQV.png?raw=true)

**Game Listing** <br/>
![](http://imagizer.imageshack.us/v2/1055x327q90/923/Pq88uT.png?raw=true)

**Game Creation & Updating** <br/>
![](http://imagizer.imageshack.us/v2/836x510q90/924/ziu5Md.png?raw=true)

**Game Character Listing** <br/>
![](http://imagizer.imageshack.us/v2/1055x410q90/923/hL2eOf.png?raw=true)

**Game Character Creation & Updating** <br/>
![](http://imagizer.imageshack.us/v2/880x510q90/924/AFYnld.png?raw=true)

## Supported Python Versions
We recommend that you use Python 2.7

## License
It is free software, and may be redistributed.