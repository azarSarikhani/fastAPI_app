# fastAPI_app
This is a project done in Python that uses fastAPI to creat an app, mysql is used for database.

## usage

1. setting  up mysql locally:

> $:```docker pull mysql:latest```
> 
> $:```docker run --name mysqlapp -it -e MYSQL_ROOT_PASSWORD=88fhrqGYr0a9i5Cn2FR4SHT1iDCl3gtY -e MYSQL_DATABASE=shopdb -p 3306:3306 -d mysql:latest```


2. use mysql the root user  and either the cli tool $:```mysql -h 127.0.0.1  -u root -p``` or workbench to log in to the server

3. Since databaseis alreay created, you just need to creat tables, and a user for fastAPI:

for instruction on how to do this see [init.sql](https://github.com/azarSarikhani/fastAPI_app/blob/main/init.sql)

more info:
1. [**SQL Alcemy docs**](https://docs.sqlalchemy.org/en/20/core/engines.html#mysql)
1. [**fastAPI sql data base tutorial**](https://fastapi.tiangolo.com/tutorial/sql-databases/)
1. [**example project**](https://pypi.org/project/mysqlclient/)
1. [**MySQL workbench**](https://www.mysql.com/products/workbench/)

4. install fastAPI!

You need to have fastAPI installed, you might want to do it in a vertual environment. To do so:

> $:``` pip install "fastapi[all]" ```

Alternatively install all of the requirments listed in [requirements](https://github.com/azarSarikhani/fastAPI_app/blob/main/requirements.txt)

> $:``` pip install -r requirments.txt```

5. Export env variables and run the app!

> $:```export dbuser=root```
> 
> $:```export dbpass=88fhrqGYr0a9i5Cn2FR4SHT1iDCl3gtY```
> 
> $:```export db_adress=127.0.0.1```
> 
> $:```export db_name=shopdb```
> 
> $:```export tablename=animals```
> 
> $:```python app.py```
