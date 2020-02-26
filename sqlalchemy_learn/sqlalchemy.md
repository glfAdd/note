##### 头文件

```python
	from sqlalchemy import or_
  
  
```

##### join count group by 动态添加条件 指定字段

- sql

```pyton
SELECT
	assistant_users.new_assistant_id AS assistant_users_new_assistant_id,
	COUNT ( assistant_users.new_assistant_id ) AS all_num,
	assistants.ID AS assistant_id,
	assistants.NAME AS assistant_name,
	regions.NAME AS city_name 
FROM
	assistant_users
	LEFT OUTER JOIN user_clue_label_assoc ON user_clue_label_assoc.user_id = assistant_users.new_user_id
	JOIN assistants ON assistants.new_assistant_id = assistant_users.new_assistant_id
	JOIN regions ON regions.ID = assistants.city_code 
GROUP BY
	assistant_users.new_assistant_id,
	assistants.ID ,
	city_name
ORDER BY
	assistant_users.new_assistant_id
```

- orm

```python
filter_condition = []
filter_condition.append(Assistant.id.in_([i for i in select_assistant]))


all_data = db.session.query(
    AssistantUsers,
).outerjoin(
    UserClueLabelAssoc,
    UserClueLabelAssoc.user_id == AssistantUsers.new_user_id
).join(
    Assistant,
    Assistant.new_assistant_id == AssistantUsers.new_assistant_id
).join(
    Region,
    Region.id == Assistant.city_code
).with_entities(
    AssistantUsers.new_assistant_id,
    func.count(AssistantUsers.new_assistant_id).label('all_num'),
    Assistant.id.label('assistant_id'),
    Assistant.name.label('assistant_name'),
    Region.name.label('city_name')
).filter(
    *filter_condition
).group_by(
    AssistantUsers.new_assistant_id,
    Assistant.id,
    Region.name.label('city_name')
).order_by(
    AssistantUsers.new_assistant_id.desc()
).all()
```

##### sqlalchemy多表联合查询

```

按用户名摸糊查询
trans_details.query.join(Uses).filter(Users.username.like('%xx%'))
#select xxx from trans_details inner join trans_details on users.id=trans_details.user_id where users.username like '%xx%'

左外联接(left join)
trans_details.query.outerjoin(Uses).filter(Users.username.like('%xx%'))
#select xxx from trans_details left outer join trans_details on users.id=trans_details.user_id where users.username like '%xx%'

以上是已经设置好外键,它自动找到关联的字段.也可以自己指定:
trans_details.query.join(Uses,trans_details.user_id==Users.id).filter(Users.username.like('%xx%'))
#select xxx from trans_details inner join trans_details on users.id=trans_details.user_id where users.username like '%xx%'

另外一个更复杂的例子:
q=db.session.query(Credit_bills_details.no,Credit_bills_details.amount,Cards.no).outerjoin(Card_trans_details,
Credit_bills_details.no==Card_trans_details.trans_no).join(Cards,Card_trans_details.to_card_id==Cards.id).filter(Credit_bills_details.credit_bill_id==3)

#SELECT credit_bills_details.no AS credit_bills_details_no, credit_bills_details.amount AS credit_bills_details_amount, cards.no AS cards_no
# FROM credit_bills_details LEFT OUTER JOIN card_trans_details ON credit_bills_details.no = card_trans_details.trans_no INNER JOIN cards
# ON card_trans_details.to_card_id = cards.id  WHERE credit_bills_details.credit_bill_id = %s



```

##### 函数

```python
from sqlalchemy.sql.expression import func 
长度
func.length(db.ArticlesTable.shorttext) > 0
```



```
res = db.session.query(
    OrderRelationApply
).outerjoin(
    NursingOrder,
    NursingOrder.id == OrderRelationApply.nursing_order_id
).outerjoin(
    PrivateHospitalOrder,
    PrivateHospitalOrder.id == OrderRelationApply.private_hospital_order_id
).outerjoin(
    InsuranceOrder,
    InsuranceOrder.id == OrderRelationApply.insurance_order_id
).filter(
    OrderRelationApply.salesman_id == salesman_id,
    OrderRelationApply.status != OrderRelationStatus.audited_failed,
    or_(
        and_(extract('year', OrderRelationApply.waiting_apply_time) == time.year,
             extract('month', OrderRelationApply.waiting_apply_time) == time.month),
        and_(extract('year', OrderRelationApply.waiting_pay_commission_time) == time.year,
             extract('month', OrderRelationApply.waiting_pay_commission_time) == time.month),
        and_(extract('year', OrderRelationApply.pay_commission_time) == time.year,
             extract('month', OrderRelationApply.pay_commission_time) == time.month),
        and_(extract('year', OrderRelationApply.refund_time) == time.year,
             extract('month', OrderRelationApply.refund_time) == time.month)
    )
).with_entities(
    OrderRelationApply,
    NursingOrder,
    PrivateHospitalOrder,
    InsuranceOrder
).all()
```

