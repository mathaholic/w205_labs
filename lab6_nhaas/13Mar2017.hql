-- 13Mar2017

-- How many expenses are flagged as fraud by the entity in 2017?
select count(*) from report_entry
where upper(expense_type_name) LIKE '%FRAUD%'
and trans_date_key between 20170101 and 20170310

-- 8989 

-- which entities are flagging expenses as fraud in 2017?

select entity_id, count(entity_id) from report_entry
where upper(expense_type_name) LIKE '%FRAUD%'
and trans_date_key between 20170101 and 20170310
group by entity_id



--  	entity_id	count(entity_id)
-- 134	p0010094f2cv	820
-- 15	p0002484budf	471
-- 130	p0095663dxi2	368
-- 6	p0002233vdsm	310
-- 104	p0002250j4ld	254
-- 101	p0000604micm	234
-- 186	p00651pqpc	233
-- 116	p0001853bijw	231
-- 68	p0030512rz5w	207
-- 234	p0001661ngqw	183
-- 164	p0001577hfn8	153
-- 142	p0000812rpal	140
-- 10	p00018053qid	135
-- 47	p0032580bd5z	132
-- 202	p0027479soj2	120
-- 60	p0052450uwbx	117
-- 222	p0018802tmiw	114
-- 215	p00219304kab	113
-- 95	p0065205yijh	112
-- 87	p0080909d6m6	103


-- check out what the most active client is doing in this
-- area 


select 
x.expense_type_name,
x.expense_type_spend_category_name,
x.user_supp_vendor_name,
x.ccard_supp_mc_code,
x.ccard_supp_std_mc_code,
x.ccard_supp_merchant_name,
x.ccard_supp_merchant_dba_name,
x.ccard_supp_merchant_street_add,
x.ccard_supp_merchant_city,
x.ccard_supp_merchant_zip,
x.ccard_supp_merchant_state,
x.ccard_supp_merchant_ctry_code,
x.approved_usd_amt, 
x.payment_type_name
from ( select 
expense_type_name,
expense_type_spend_category_name,
user_supp_vendor_name,
ccard_supp_mc_code,
ccard_supp_std_mc_code,
ccard_supp_merchant_name,
ccard_supp_merchant_dba_name,
ccard_supp_merchant_street_add,
ccard_supp_merchant_city,
ccard_supp_merchant_zip,
ccard_supp_merchant_state,
ccard_supp_merchant_ctry_code,
approved_usd_amt, 
payment_type_name
from report_entry
where trans_date_key between 20170101 and 20170310	
and entity_id = 'p0002484budf') x

where upper(x.expense_type_name) LIKE '%FRAUD%'



select 
x.expense_type_name,
x.expense_type_spend_category_name,
x.user_supp_vendor_name,
x.ccard_supp_mc_code,
x.ccard_supp_std_mc_code,
x.ccard_supp_merchant_name,
x.ccard_supp_merchant_dba_name,
x.ccard_supp_merchant_street_add,
x.ccard_supp_merchant_city,
x.ccard_supp_merchant_zip,
x.ccard_supp_merchant_state,
x.ccard_supp_merchant_ctry_code,
x.approved_usd_amt, 
x.payment_type_name
from ( select 
expense_type_name,
expense_type_spend_category_name,
user_supp_vendor_name,
ccard_supp_mc_code,
ccard_supp_std_mc_code,
ccard_supp_merchant_name,
ccard_supp_merchant_dba_name,
ccard_supp_merchant_street_add,
ccard_supp_merchant_city,
ccard_supp_merchant_zip,
ccard_supp_merchant_state,
ccard_supp_merchant_ctry_code,
approved_usd_amt, 
payment_type_name
from report_entry
where trans_date_key between 20170101 and 20170310	
and entity_id = 'p0010094f2cv') x

where upper(x.expense_type_name) LIKE '%FRAUD%'