Step1:- login to your mysql & create a database & table


mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+


mysql> create database dataeaze;
Query OK, 1 row affected (0.01 sec)


mysql> use dataeaze;
Database changed
mysql> show tables;
Empty set (0.00 sec)


Query OK, 0 rows affected (0.02 sec)at, radio float,newspaper float,sales float);


mysql> describe advertise;
+-----------+-------+------+-----+---------+-------+
| Field     | Type  | Null | Key | Default | Extra |
+-----------+-------+------+-----+---------+-------+
| TV        | float | YES  |     | NULL    |       |
| radio     | float | YES  |     | NULL    |       |
| newspaper | float | YES  |     | NULL    |       |
| sales     | float | YES  |     | NULL    |       |
+-----------+-------+------+-----+---------+-------+
4 rows in set (0.00 sec)

mysql> select * from advertise;
Empty set (0.01 sec)

Step2:- Run the python program name argsparse.py on python terminal

 python3 argsparse.py -d shubh -m data.json
 
 RESULT:-
 
 mysql> select * from advertise;
+-------+-------+-----------+-------+
| TV    | radio | newspaper | sales |
+-------+-------+-----------+-------+
| 147.3 |  23.9 |      19.1 |  14.6 |
| 218.4 |  27.7 |      53.4 |    18 |
| 237.4 |   5.1 |      23.5 |  12.5 |
|  13.2 |  15.9 |      49.6 |   5.6 |
| 228.3 |  16.9 |      26.2 |  15.5 |
|  62.3 |  12.6 |      18.3 |   9.7 |
| 262.9 |   3.5 |      19.5 |    12 |
| 142.9 |  29.3 |      12.6 |    15 |
| 240.1 |  16.7 |      22.9 |  15.9 |
| 248.8 |  27.1 |      22.9 |  18.9 |
|  70.6 |    16 |      40.8 |  10.5 |
| 292.9 |  28.3 |      43.2 |  21.4 |
| 112.9 |  17.4 |      38.6 |  11.9 |
|  97.2 |   1.5 |        30 |   9.6 |
| 265.6 |    20 |       0.3 |  17.4 |
|  95.7 |   1.4 |       7.4 |   9.5 |
| 290.7 |   4.1 |       8.5 |  12.8 |
| 266.9 |  43.8 |         5 |  25.4 |
|  74.7 |  49.4 |      45.7 |  14.7 |
|  43.1 |  26.7 |      35.1 |  10.1 |
|   228 |  37.7 |        32 |  21.5 |
| 202.5 |  22.3 |      31.6 |  16.6 |
|   177 |  33.4 |      38.7 |  17.1 |
| 293.6 |  27.7 |       1.8 |  20.7 |
| 230.1 |  37.8 |      69.2 |  22.1 |
|  44.5 |  39.3 |      45.1 |  10.4 |
|  17.2 |  45.9 |      69.3 |   9.3 |
| 151.5 |  41.3 |      58.5 |  18.5 |
| 180.8 |  10.8 |      58.4 |  12.9 |
|   8.7 |  48.9 |        75 |   7.2 |
|  57.5 |  32.8 |      23.5 |  11.8 |
| 120.2 |  19.6 |      11.6 |  13.2 |
|   8.6 |   2.1 |         1 |   4.8 |
| 199.8 |   2.6 |      21.2 |  10.6 |
|  66.1 |   5.8 |      24.2 |   8.6 |
| 214.7 |    24 |         4 |  17.4 |
|  23.8 |  35.1 |      65.9 |   9.2 |
|  97.5 |   7.6 |       7.2 |   9.7 |
| 204.1 |  32.9 |        46 |    19 |
| 195.4 |  47.7 |      52.9 |  22.4 |
|  67.8 |  36.6 |       114 |  12.5 |
| 281.4 |  39.6 |      55.8 |  24.4 |
|  69.2 |  20.5 |      18.3 |  11.3 |
+-------+-------+-----------+-------+
43 rows in set (0.00 sec)


