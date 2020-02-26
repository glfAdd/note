

```
github
https://github.com/flask-admin/flask-admin

文档
https://flask-admin.readthedocs.io/en/latest/



```

##### ModelView

```
can_create = True    													是否可以创建
can_edit = True        												是否可以编辑
can_delete = True        											是否可以删除
list_template = 'admin/model/list.html'    		修改显示该模型的html模板
edit_template = 'admin/model/edit.html'    		修改编辑该模型的html模板
create_template = 'admin/model/create.html'   修改创建该模型的html模板
column_list        														填入想要显示的字段，不填的话自动从模型中取
column_exclude_list        										填入不想显示的字段
column_labels    								一个字典，值是字段名，键是显示的名称，为字段提供显示的别名
column_descriptions        										一个字典，同上，为字段显示描述
column_formatters        											一个字典，格式化字段，定义字段的显示方式
column_type_formatters    一个字典，格式化字段类型，定义字段类型的显示方式，默认显示，None是空字符，bool是True，list是‘，’
column_display_pk        											控制主键是否显示
column_sortable_list        									选择可以被排序的字段
column_searchable_list        								选择可以被搜索的字段
column_default_sort        										默认的排序字段，默认为空
column_choices    	    											字段的可选值
column_filters        												选择可以被过滤的字段
form         													一个Form类，可以被重写, 用来在创建和编辑是使用的表单
form_base_class       												一般用来做csrf防御
form_columns=None        											选择创建或者编辑时显示的字段
form_excluded_columns        									选择创建或编辑时不想显示的字段
form_args=None    表单字段参数的字典。有关可能的选项列表，请参阅WTForms文档
form_overrides        												重写字段的表单字典
form_widget_args        											定义表单字典需要的参数
form_extra_fields        											表单额外的字段
form_ajax_refs        												使用ajax来加载外键
form_create_rules=None    为创建的表单定制规则，重写form_rules如果存在的话
form_edit_rules=None    为编辑的表单定制规则，重写form_rules如果存在的话
action_disallow_list        									选择不允许执行的操作，如删除操作
page_size=20        													设置每页显示的字段数
action_form        													 	自定义表单操作
action_view        														自定义显示操作
after_model_change        										在表单改变之后需要做的事情
after_model_delete        										在表单被删除之后需要做的事情
ajax_update        														在列表视图中编辑单个字段
can_export=False        											是否可以被导出
can_set_page_size=False    	    							是否可以设置分页的数量
can_view_details=False        								是否可以查看详细的字段
column_details_exclude_list=None    					详细字段中不显示的字段
column_details_list=None    									详细字段中显示的字段
column_display_actions=None    控制字段每个值的操作，编辑，删除，查看详细字段等
column_editable_list=None        							可以被编辑的字段
column_export_exclude_list=None    						不可以被导出的字段
column_export_list=None        								可以被导出的字段
column_extra_row_actions=None    							定制额外的字段操作
column_formatters_export=None    							定义导出的字段格式
column_type_formatters_export=None    				定义导出的字段类型的格式
create_form    																创建表单
create_modal=False    												创建时是否弹出对话框
create_modal_template='/admin/model/modals/create.html'    设置创建时弹出的对话框的模板地址
create_view    				    										创建视图
delete_form        														删除表单
delete_model        													删除模板
delete_view        														删除视图
details_modal=Flase        										查看详细时是否弹出对话框
details_modal_template=‘admin/model/modals/details.html’    设置查看详细弹出的对话框的模板地址
details_template='admin/model/details.html'   设置查看详细的模板地址
details_view        													详细视图
edit_form        															编辑表单
edit_modal=False        											编辑时是否弹出对话框
edit_modal_template='admin/model/modals/edit.html'    设置编辑时弹出对话框的模板地址
edit_view        															编辑视图
export_max_row=0    设置导出最大的数量
export_types=['csv']    设置导出类型
form_rules=None    表单规则
get_action_form()    为模型操作创建表单类
get_column_name(field)    返回一个人类可以读的字段名
get_column_names(only_column, excluded_columns)    返回一系列可以读的字段名
get_create_form()    为模型创建视图创建一个表单类
get_delete_form()    为模型删除视图创建一个表单类
get_details_columns()    获取详细字段的字段名
get_edit_form()    为模型编辑视图创建一个表单类
get_export_columns()    获取可以被导出的字段名
get_export_name(export_type='csv')    获取可以导出文件名称
get_export_value(model, name)    获取导出值
get_filter_arg(index,flt)    获取单个过滤项
get_filters()    获取所有过滤项
get_form()    获取表单类
get_list(page, sort_field, sort_desc, search, filters,page_size=None)    从数据库中获取指定的数据
get_list_columns()    获取设置的column_list中的字段
get_list_form()    获取可编辑列表视图的表单类
get_list_row_actions()    返回字段可以执行的操作
get_list_value(context,model,name)    返回要在列表视图中显示的值
get_one(id)    通过id来获取某个模型
get_pk_value(model)    获取模型的主键
get_save_return_url(model, is_created=False)    获取保存之后返回的url
get_sortable_columns()    获取可以排序的字段
handle_filter(filter)    处理过滤器
index_view(args,*kwargs)    默认显示的视图
init_search()    初始化搜索
is_action_allowed(name)    判断操作是否允许
is_editable(name)    判断是否可以编辑
is_sortable(name)    判断是否可以拍下
is_valid_filter(filter)    判断是否是合法的过滤器
list_form(obj=None)    实例化列表视图的模型编辑表单并返回
named_filter_urls=False    在url参数中使用人类可以的过滤器
on_form_prefill(form,id)    执行其他操作以预填充编辑表单
on_model_change(form,model,is_created)     在模板改变后需要做的事情
on_model_delete(model)    在模板被删除之后需要做的事情
scaffold_filters(name)    为给定的名称生成过滤器对象
scaffold_form()     从模型中创建form.BaseForm继承的类。必须在子类中实现
scaffold_list_columns()    返回模型字段名称列表。必须在子类中实现。
scaffold_list_form(widget=None, validators=None)    仅使用self.column_editable_list中的列为index_view创建表单
scaffold_sortable_columns()    返回可排序列的字典。必须在子类中实现
simple_list_pager=False   是否计数
update_model(form,model)    从表单中更新模型
validate_form(form)    验证提交的表单


```

##### 表头

```python





```

