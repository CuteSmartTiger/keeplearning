1.数据准备
create table stock(
	id int auto_increment not null,
	product_id int not null comment '商品ID',
	category_id int not null comment '分类ID',
	warehouse_id int not null comment '仓库ID',
	count int not null comment '库存数量',
	primary key(id)
	) comment '库存表'
;

insert into stock(product_id,category_id,warehouse_id,count)
	values(2030,9,1,10),(2030,9,2,15),(2030,9,3,20),(2040,8,1,30),
	(2040,8,2,20);

select product_id,warehouse_id,sum(count) from stock group by product_id;