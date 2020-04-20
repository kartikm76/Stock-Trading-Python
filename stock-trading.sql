insert into transaction_type_code (code, description) values ('B', 'Buy');
insert into transaction_type_code (code, description) values ('S', 'Sell');
insert into account_type_code (code, description) values ('TRD', 'Trading');
insert into user_master (id, nstock_holdingame, ssn, isActive, profile_create_date) values ('kkm', 'kartik makker', '123-45-6789', 'Y', '2020-04-11');
insert into user_master (id, name, ssn, isActive, profile_create_date) values ('dnp', 'Deepak Pandey', '123-45-6789', 'Y', '2020-04-15');
insert into account_master (id, type, open_date, isActive) values ('TRD_001', 'TRD', '2020-04-11', 'Y');
insert into user_account (user_id, account_id) values ('kkm', 'TRD_001');
insert into account_balance (account_id, initial_balance, initial_balance_date, current_balance, current_balance_sate) values ('kkm', 'TRD_001');
insert into stock_holding (account_id, stock_symbol, holding_qty, purchase_price) values ('TRD_001', 'AMZN', 100, 2000);
select a.user_id, b.account_id, b.stock_symbol, b.holding_qty, b.purchase_price from user_account a, stock_holding b where a.account_id = b.account_id;
select a.user_id, b.account_id, b.stock_symbol, b.holding_qty, b.purchase_price from user_account a, stock_holding b where a.account_id = b.account_id 
where a.account_id = 'TRD_001'
