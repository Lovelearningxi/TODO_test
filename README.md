TODO功能：

1.创建新的TODO

```powershell
$ curl http://localhost:5000/todos -d "task=something new" -X POST -v

Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /todos HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.55.1
> Accept: */*
> Content-Length: 18
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 18 out of 18 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 26
< Server: Werkzeug/1.0.1 Python/3.6.8
< Date: Mon, 05 Oct 2020 14:18:15 GMT
<
{"task": "something new"}
* Closing connection 0

```

2.列出某条TODO

```powershell
$ curl http://localhost:5000/todos

{"todo1": {"task": "something different"}, "todo3": {"task": "something new"}}

$ curl http://localhost:5000/todos/todo3

{"task": "something new"}

$ curl http://localhost:5000/todos/todo2

{"message": "Todo todo2 doesn't exist"}

```

3.删除某条TODO

```powershell
$ curl http://localhost:5000/todos/todo2 -X DELETE -v

*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> DELETE /todos/todo2 HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.55.1
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< Server: Werkzeug/1.0.1 Python/3.6.8
< Date: Mon, 05 Oct 2020 14:22:06 GMT
<
* Closing connection 0

```

4.更新所有TODO

```powershell
$ curl http://localhost:5000/todos/todo1 -d "task=something different" -X PUT -v

*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> PUT /todos/todo1 HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.55.1
> Accept: */*
> Content-Length: 24
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 24 out of 24 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 32
< Server: Werkzeug/1.0.1 Python/3.6.8
< Date: Mon, 05 Oct 2020 14:37:52 GMT
<
{"task": "something different"}
* Closing connection 0
```



要求:

1.使用Flask作为开发框架

√

2.TODO的数据储存在Cassandra

X Cassandra适配有问题，使用的MySQL

3.遵循RESTful开发规范

乄

4.每个api都有对应的测试

  在上面的代码块中有显示

5.使用dockers对应用进行打包和部署，提供打包应用Dockerfile文件

在打包的过程中有些关于Oracle VM VirtualBox的问题  因为现在上课的课程依然需要Oracle VM VirtualBox 所以不方便修改其中的参数（好不容易搭好的hadoop 不想整坏了，改天换个电脑试试）Dockerfile写了 但不知道对不对（应该不对） 暂时这样 有需要修改的再说 

SealW# TODO_test
