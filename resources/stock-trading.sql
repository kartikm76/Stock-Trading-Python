insert into transaction_type_code (code, description) values ('B', 'Buy');
insert into transaction_type_code (code, description) values ('S', 'Sell');
insert into account_type_code (code, description) values ('TRD', 'Trading');

Last login: Sat Apr 25 12:33:31 on ttys002
kartikmakker@Kartiks-MBP ~ % cd "Kartik Workspace 
dquote> "
cd: no such file or directory: Kartik Workspace\n
kartikmakker@Kartiks-MBP ~ % cd "Kartik Workspace"
kartikmakker@Kartiks-MBP Kartik Workspace % ls -lrt
total 0
drwxr-xr-x   9 kartikmakker  staff  288 Feb 19  2019 Spring Boot Projects
drwxr-xr-x   7 kartikmakker  staff  224 Feb 22  2019 PyCharm Projects
drwxr-xr-x  30 kartikmakker  staff  960 Apr 20  2019 Udacity-Image-Classifier-Part1
drwxr-xr-x  20 kartikmakker  staff  640 Apr 30  2019 Udacity-Image-Classifier-Part2
drwx------   4 kartikmakker  staff  128 Nov 19 06:39 VirtualBox VMs
drwxr-xr-x   7 kartikmakker  staff  224 Dec 17 08:53 Fixed Income
drwxr-xr-x   4 kartikmakker  staff  128 Jan 14 17:27 AWS Lambda
drwxr-xr-x@  6 kartikmakker  staff  192 Jan 24 17:44 AWS FI Analytics
drwxr-xr-x  10 kartikmakker  staff  320 Apr 10 12:34 AWS Chalice Example
drwxr-xr-x  10 kartikmakker  staff  320 Apr 18 21:01 Stock-Trading-Python - BKUP - 0420
drwxr-xr-x  10 kartikmakker  staff  320 Apr 19 15:42 Stock-Trading-React - BKUP
drwxr-xr-x  14 kartikmakker  staff  448 Apr 20 09:10 StockReader - Java
drwxr-xr-x  12 kartikmakker  staff  384 Apr 20 13:04 Tools
drwxr-xr-x  20 kartikmakker  staff  640 Apr 20 13:07 Python Scripts
drwxr-xr-x  12 kartikmakker  staff  384 Apr 20 13:10 JS Projects
drwxr-xr-x   7 kartikmakker  staff  224 Apr 20 14:06 spark-kafka-cassandra-applying-lambda-architecture
drwxr-xr-x  14 kartikmakker  staff  448 Apr 20 14:08 React Projects
drwxr-xr-x  12 kartikmakker  staff  384 Apr 24 22:34 Stock-Trading-React
drwxr-xr-x   3 kartikmakker  staff   96 Apr 25 12:32 GitHub
drwxr-xr-x  14 kartikmakker  staff  448 Apr 27 23:40 Stock-Trading-Python
kartikmakker@Kartiks-MBP Kartik Workspace % cd Stock-Trading-Python
kartikmakker@Kartiks-MBP Stock-Trading-Python % ls -lrt
total 72
-rw-r--r--@ 1 kartikmakker  staff  19791 Apr 11 17:33 stock-trading-schema.pdf
-rw-r--r--  1 kartikmakker  staff   1320 Apr 20 09:30 README.md
drwxr-xr-x  5 kartikmakker  staff    160 Apr 20 09:49 src
drwxr-xr-x  8 kartikmakker  staff    256 Apr 20 14:12 my_env
-rw-r--r--  1 kartikmakker  staff   1798 Apr 25 10:48 requirements.txt
-rw-r--r--  1 kartikmakker  staff   2068 Apr 27 23:33 stock-trading.sql
-rw-r--r--  1 kartikmakker  staff   1071 Apr 27 23:40 stocks.txt
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi stocks.list
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi stocks.list
kartikmakker@Kartiks-MBP Stock-Trading-Python % ls -lrt       
total 72
-rw-r--r--@ 1 kartikmakker  staff  19791 Apr 11 17:33 stock-trading-schema.pdf
-rw-r--r--  1 kartikmakker  staff   1320 Apr 20 09:30 README.md
drwxr-xr-x  5 kartikmakker  staff    160 Apr 20 09:49 src
drwxr-xr-x  8 kartikmakker  staff    256 Apr 20 14:12 my_env
-rw-r--r--  1 kartikmakker  staff   1798 Apr 25 10:48 requirements.txt
-rw-r--r--  1 kartikmakker  staff   2068 Apr 27 23:33 stock-trading.sql
-rw-r--r--  1 kartikmakker  staff   1071 Apr 27 23:41 stocks.txt
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi stock.txt
kartikmakker@Kartiks-MBP Stock-Trading-Python % ls -lrt
total 72
-rw-r--r--@ 1 kartikmakker  staff  19791 Apr 11 17:33 stock-trading-schema.pdf
-rw-r--r--  1 kartikmakker  staff   1320 Apr 20 09:30 README.md
drwxr-xr-x  5 kartikmakker  staff    160 Apr 20 09:49 src
drwxr-xr-x  8 kartikmakker  staff    256 Apr 20 14:12 my_env
-rw-r--r--  1 kartikmakker  staff   1798 Apr 25 10:48 requirements.txt
-rw-r--r--  1 kartikmakker  staff   2068 Apr 27 23:33 stock-trading.sql
-rw-r--r--  1 kartikmakker  staff   1071 Apr 27 23:41 stocks.txt
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi stocks.txt


Press ENTER or type command to continue
kartikmakker@Kartiks-MBP Stock-Trading-Python % ls -lrt
total 80
-rw-r--r--@ 1 kartikmakker  staff  19791 Apr 11 17:33 stock-trading-schema.pdf
-rw-r--r--  1 kartikmakker  staff   1320 Apr 20 09:30 README.md
drwxr-xr-x  5 kartikmakker  staff    160 Apr 20 09:49 src
drwxr-xr-x  8 kartikmakker  staff    256 Apr 20 14:12 my_env
-rw-r--r--  1 kartikmakker  staff   1798 Apr 25 10:48 requirements.txt
-rw-r--r--  1 kartikmakker  staff   4808 Apr 28 00:21 stock-trading.sql
-rw-r--r--  1 kartikmakker  staff   3530 Apr 28 00:21 stocks.txt
kartikmakker@Kartiks-MBP Stock-Trading-Python % mv stocks.txt stock_master.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % ls -lrt
total 80
-rw-r--r--@ 1 kartikmakker  staff  19791 Apr 11 17:33 stock-trading-schema.pdf
-rw-r--r--  1 kartikmakker  staff   1320 Apr 20 09:30 README.md
drwxr-xr-x  5 kartikmakker  staff    160 Apr 20 09:49 src
drwxr-xr-x  8 kartikmakker  staff    256 Apr 20 14:12 my_env
-rw-r--r--  1 kartikmakker  staff   1798 Apr 25 10:48 requirements.txt
-rw-r--r--  1 kartikmakker  staff   4808 Apr 28 00:21 stock-trading.sql
-rw-r--r--  1 kartikmakker  staff   3530 Apr 28 00:21 stock_master.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % wc -l stock_master.sql 
      30 stock_master.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % ls -lrt           
total 80
-rw-r--r--@ 1 kartikmakker  staff  19791 Apr 11 17:33 stock-trading-schema.pdf
-rw-r--r--  1 kartikmakker  staff   1320 Apr 20 09:30 README.md
drwxr-xr-x  5 kartikmakker  staff    160 Apr 20 09:49 src
drwxr-xr-x  8 kartikmakker  staff    256 Apr 20 14:12 my_env
-rw-r--r--  1 kartikmakker  staff   1798 Apr 25 10:48 requirements.txt
-rw-r--r--  1 kartikmakker  staff   4808 Apr 28 00:21 stock-trading.sql
-rw-r--r--  1 kartikmakker  staff   3530 Apr 28 00:21 stock_master.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % cp stock_master.sql user_master.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi user_master.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi user_master1.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi user_master.sql 
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi user_master1.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi user_master1.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi user_master.sql 
kartikmakker@Kartiks-MBP Stock-Trading-Python % rm user_master1.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi user_master.sql 
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi account_balance.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi account_master.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi account_master.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi account_balance.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi user_account.sq;
kartikmakker@Kartiks-MBP Stock-Trading-Python % ls -lrt
total 176
-rw-r--r--@ 1 kartikmakker  staff  19791 Apr 11 17:33 stock-trading-schema.pdf
-rw-r--r--  1 kartikmakker  staff   1320 Apr 20 09:30 README.md
drwxr-xr-x  5 kartikmakker  staff    160 Apr 20 09:49 src
drwxr-xr-x  8 kartikmakker  staff    256 Apr 20 14:12 my_env
-rw-r--r--  1 kartikmakker  staff   1798 Apr 25 10:48 requirements.txt
-rw-r--r--  1 kartikmakker  staff   3530 Apr 28 00:21 stock_master.sql
-rw-r--r--  1 kartikmakker  staff   4494 Apr 28 11:19 user_master.sql
-rw-r--r--@ 1 kartikmakker  staff    165 Apr 28 12:37 ~$SampleData.xlsx
-rw-r--r--@ 1 kartikmakker  staff  27158 Apr 28 14:19 SampleData.xlsx
-rw-r--r--  1 kartikmakker  staff   3255 Apr 28 14:22 account_master.sql
-rw-r--r--  1 kartikmakker  staff   3406 Apr 28 14:25 account_balance.sql
-rw-r--r--  1 kartikmakker  staff    229 Apr 28 14:25 stock-trading.sql
-rw-r--r--  1 kartikmakker  staff   2381 Apr 28 14:38 user_account.sq
kartikmakker@Kartiks-MBP Stock-Trading-Python % ls -lrt *.sql
-rw-r--r--  1 kartikmakker  staff  3530 Apr 28 00:21 stock_master.sql
-rw-r--r--  1 kartikmakker  staff  4494 Apr 28 11:19 user_master.sql
-rw-r--r--  1 kartikmakker  staff  3255 Apr 28 14:22 account_master.sql
-rw-r--r--  1 kartikmakker  staff  3406 Apr 28 14:25 account_balance.sql
-rw-r--r--  1 kartikmakker  staff   229 Apr 28 14:25 stock-trading.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % mv stock-trading.sql stock_trading.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi stock_trading.sql 
kartikmakker@Kartiks-MBP Stock-Trading-Python % mv stock_trading.sql codes.sql
kartikmakker@Kartiks-MBP Stock-Trading-Python % ls -lrt
total 176
-rw-r--r--@ 1 kartikmakker  staff  19791 Apr 11 17:33 stock-trading-schema.pdf
-rw-r--r--  1 kartikmakker  staff   1320 Apr 20 09:30 README.md
drwxr-xr-x  5 kartikmakker  staff    160 Apr 20 09:49 src
drwxr-xr-x  8 kartikmakker  staff    256 Apr 20 14:12 my_env
-rw-r--r--  1 kartikmakker  staff   1798 Apr 25 10:48 requirements.txt
-rw-r--r--  1 kartikmakker  staff   3530 Apr 28 00:21 stock_master.sql
-rw-r--r--  1 kartikmakker  staff   4494 Apr 28 11:19 user_master.sql
-rw-r--r--@ 1 kartikmakker  staff    165 Apr 28 12:37 ~$SampleData.xlsx
-rw-r--r--@ 1 kartikmakker  staff  27158 Apr 28 14:19 SampleData.xlsx
-rw-r--r--  1 kartikmakker  staff   3255 Apr 28 14:22 account_master.sql
-rw-r--r--  1 kartikmakker  staff   3406 Apr 28 14:25 account_balance.sql
-rw-r--r--  1 kartikmakker  staff    229 Apr 28 14:25 codes.sql
-rw-r--r--  1 kartikmakker  staff   2381 Apr 28 14:38 user_account.sq
kartikmakker@Kartiks-MBP Stock-Trading-Python % vi stock_holding.sql

insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_134', 'VSTM', 28, 0.105);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_134', 'BYND', 78, 92.63);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_138', 'NVDA', 57, 294.08);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_138', 'GNC', 54, 8.26);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_150', 'VISL', 40, 2.715);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_150', 'NXPI', 51, 92.13);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_150', 'QTNT', 37, 2.59);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_150', 'GOOG', 83, 1270.88);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_150', 'AIM', 35, 3.1);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_186', 'VISL', 48, 7.715);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_186', 'GOOG', 89, 1274.88);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_212', 'VSTM', 28, 1.895);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_212', 'BBBY', 37, 1.41);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_212', 'LYV', 41, 36.01);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_221', 'NAT', 56, 0.2);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_221', 'USO', 16, 6.81);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_268', 'VISL', 30, 7.715);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_268', 'LYV', 15, 41.01);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_285', 'RCL', 67, 31.47);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_285', 'LYV', 77, 37.01);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_342', 'TNP', 67, 2.98);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_342', 'QTNT', 56, 0.59);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_342', 'AXSM', 80, 90);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_367', 'FFIV', 21, 123.92);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_367', 'YTEN', 64, 4.91);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_373', 'YTEN', 71, 2.91);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_373', 'LYV', 14, 41.01);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_384', 'VISL', 91, 2.715);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_384', 'BYND', 45, 92.63);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_385', 'VSTM', 81, 0.105);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_385', 'FFIV', 22, 123.92);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_442', 'NAT', 18, 1.2);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_442', 'CCL', 81, 6.98);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_584', 'YTEN', 90, 4.91);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_584', 'BYND', 42, 98.63);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_761', 'QTNT', 49, 1.41);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_761', 'CGC', 33, 8.53);
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_776', 'GOOG', 74, 1274.88);
