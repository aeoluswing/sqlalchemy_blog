#  sqlalchemy_blog
  
### **1. 工程简要说明**  
&nbsp;&nbsp;实现ORM数据库的多表及多种关系创建和实验数据的fake 

### **2. 实现步骤和原理**
        2.1.安装依赖库
            sqlalchemy——python语言的一个ORM框架，建立在数据库的API基础之上，使用关系对象映射进行数据库操作
                sqlalchemy只是一个框架，实际的数据库连接仍然需要数据库驱动实现
                sqlalchemy框架的作用有：
                    （1）描述表（表类，表项为类属性）
                    （2）定义关系（1对1，1对多，多对多关系分解成多个1对多关系）
                    （3）映射关系到数据
            pymysql——数据库驱动库，提供了不同数据库API，根据python版本和数据库类型不同，所依赖的驱动也不同
                MySQL-python:
                    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
                pymysql:
                    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
                MySQL-Connector:
                    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
                cx_Oracle:
                    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
                PostgreSql:
                    postgresql+psycopg2://user:pass@host:port/dbname?key=value&key=value...]
                    postgresql+pg8000://user:pass@host:port/dbname?key=value&key=value...]
                注意：
                    python2.7版本使用mysqldb
                    python3.5+版本使用pymysql
            faker——生成数据的库，一般用于生成虚假的测试数据
        2.2.具体步骤说明
            2.2.1.通过类创建表
                sqlalchemy通过ORM（对象关系映射）将表结构和面向对象语言中的类对应，从而操作数据库的步骤可以转变为对类或类实例的直接操作完成
                    (1)使用create_engine创建数据库的连接
                    (2)使用类定义对应的表结构，类属性的定义为表项定义，常用的数据类型有String,Integer,Text,Boolean,SmallInteger,DateTime
                    (3)relationship决定了表之间的关系
                通过Base.metadata.create_all()方法执行以上表及关系的建立
            2.2.2.建立数据连接
                通过sqlalchemy.orm实例化sessionmaker对象（实际上绑定了engine）
            2.2.3.批量构造测试数据
                faker采用工厂模式构造测试数据
                创建相关类的实例，并调用session_add()添加一个，或者session_add_all()一次添加多个
                注意最后需要用session.commit()提交

### **3. CRUD**    
    （1）update
        更新字段
            >>> a = session.query(Article).get(10)
            >>> a.title = 'My test blog post'
            >>> session.add(a)
            >>> session.commit()
        添加标签
            >>> a = session.query(Article).get(10)
            >>> a.tags.append(Tag(name='python'))
            >>> session.add(a)
            >>> session.commit()
    （2）delete
        删除查询到的结果项
            >>> a = session.query(Article).get(10)
            >>> session.delete(a)
            >>> session.commit()