# coding=utf-8
"""
WTForms支持的HTML标准字段
StringField	            文本字段
TextAreaField	        多行文本字段
PasswordField	        密码文本字段
HiddenField	            隐藏文本字段
DateField	            文本字段，值为datetime.date格式
DateTimeField	        文本字段，值为datetime.datetime格式
IntegerField	        文本字段，值为整数
DecimalField	        文本字段，值为decimal.Decimal
FloatField	            文本字段，值为浮点数
BooleanField	        复选框，值为True和False
RadioField	            一组单选框
SelectField	            下拉列表
SelectMultipleField	    下拉列表，可选择多个值
FileField	            文本上传字段
SubmitField	            表单提交按钮
FormField	            把表单作为字段嵌入另一个表单
FieldList	            一组指定类型的字段

WTForms常用验证函数
DataRequired	        确保字段中有数据
EqualTo	                比较两个字段的值，常用于比较两次密码输入
Length	                验证输入的字符串长度
NumberRange	            验证输入的值在数字范围内
URL	                    验证URL
AnyOf	                验证输入值在可选列表中
NoneOf	                验证输入值不在可选列表中
"""

from flask import Flask, render_template, redirect, url_for, session, request, flash
# wtf扩展的表单类
from flask_wtf import FlaskForm
# 自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField
# wtf扩展提供的表单验证器
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
# 必须配置这个, 永福crf验证
app.config['SECRET_KEY'] = 'aaabbbbccadsfasfasdf'


# 自定义表单类，文本字段、密码字段、提交按钮
class LoginForm(FlaskForm):
    # DataRequired保证数据必须填写, 并且不为空
    user_name = StringField(label=u'用户名', validators=[DataRequired(u'用户名不能为空')])
    password1 = PasswordField(label=u'密码', validators=[DataRequired(u'密码不能为空')])
    password2 = PasswordField(label=u'确认密码', validators=[DataRequired(u'确认密码不能为空'), EqualTo('password1', u'两次密码不一致')])
    submit = SubmitField(u'提交')


@app.route('/index/')
def home():
    user_name = session.get('user_name', '')
    return user_name


# 定义根路由视图函数，生成表单对象，获取表单数据，进行表单数据验证
@app.route('/login/', methods=['GET', 'POST'])
def index():
    # 创建表单对象
    # 如果是post请求,数据会保存在这个对象中
    form = LoginForm()
    # 判断form中的数据, 如果form满足所有的验证器则返回True
    if form.validate_on_submit():
        us = form.user_name.data
        ps1 = form.password1.data
        ps2 = form.password2.data
        print(us, ps1, ps2)
        session['user_name'] = us
        return redirect(url_for('home'))
    return render_template('wtf.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
