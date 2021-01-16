# 如何偷偷的在网页中骂人？

首先，写一对脚本标签：

```html
<script>
</script>
```

在两个标签里面输入下面这个JavaScript代码：

```javascript
/*javascript 部分*/
function fuckyou()
console.warn('fuck you')
```

下面是触发代码，这是个按钮，可以把它放在任意位置（body内）

```html
<!--HTML 部分-->
<button onclick="fuckyou()">执行</button>
```

# 各语言Markdown

1.Assembly

```assembly
[section .data]         ;  // 注释
    strHello db "Hello,world!", 0Ah
    STRLEN equ $ - strHello
    [section .text]  ; 
    global _start    ; 
 
_start:
    mov edx, STRLEN
    mov ecx, strHello
    mov ebx, 1
    mov eax, 4    ;  sys_write
    int 0x80         ;  系统调用
    mov ebx, 0
    mov eax, 1    ;  sys_exit
    int 0x80         ;  系统调用
```

2.bash

```bash
echo Hello,world
```

3.c

```c
int main()
{
    printf("Hello, World");
    return(0);
}
```

4.c#

```c#
using System;
class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Hello, World");
    }
}
```

5.c++

```c++
#include <iostream>

int main()
{
    std::cout << "Hello World";
    return 0;
}
```

6.commonlisp

```commonlisp
(defun hello-world()
      (format t "Hello,World!"))

(hello-world)
```

7.d

```D
import std.stdio;

void main()
{
    writeln("Hello World");
}
```

8.elixir

```elixir
IO.puts "hello world"
```

9.erlang

```erlang
main(_) ->
	io:fwrite("Hello, World\n").
```

10.fortran

```fortran
program main
	print *, "Hello, World"
end
```

11.go

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello world!")
}
```

12.haskell

```haskell
main = putStrLn "Hello, World"
```

13.java

```java
public class Main {
	public static void main(String[] args) {
		System.out.println("Hello, World");
	}
}
```

14.javascript

```javascript
console.log("Hello, World");
```

15.lua

```lua
print("Hello, World")
```



16.ocaml

```ocaml
print_endline "Hello, World"
```

17.octave

```octave
printf("Hello, World\n");
```

18.pascal

```pascal
program Hello;
begin
	writeln ('Hello, World')
end.
```

19.php

```php
<?php
print("Hello, World\n");
?>
```

20.prolog

```prolog
:- initialization(main).
main :- write('Hello, World\n').
```

21.python

```python
print("Hello,World")
```

22.ruby

```ruby
puts "Hello, World"
```

23.rust

```rust
fn main() {
	println!("Hello, World");
}
```

24.typescript

```typescript
console.log("Hello, World");
```

25.cobol

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. hello.
PROCEDURE DIVISION.
DISPLAY "Hello, world!".
STOP RUN.
```

26.kotlin

```kotlin
fun main() {
	println("Hello, World")
}
```

27.objective-c

```objective-c
#import <Foundation/Foundation.h>
 
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSLog(@"Hello, World!");
    }
     return 0;
}
```

28.r

```R
cat("Hello, World\n")
```

29.scala

```scala
object Main {
	def main(args: Array[String]) = {
		println("Hello, World")
	}
}
```

30.sql

```sql
CREATE TABLE Person (
	PersonID int,
	LastName varchar(255),
	FirstName varchar(255),
	Address varchar(255),
	City varchar(255)
);

INSERT INTO Person VALUES (1, 'Tom', 'Erichsen', 'Skagen 210, Stavanger 4006', 'Norway');

SELECT * FROM Person;

```

31.swift

```swift
print("Hello, World")
```

32.visual basic

```visual basic
Public Module Program
	 Public Sub Main()
		Console.WriteLine("Hello, World")
	 End Sub
End Module
```

33.perl

```perl
print "Hello, World!\n";
```

34.clojure

```clojure
(println "hello world")
```

35.groovy

```groovy
public class Hello {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```

# Markdown字典
## 目录
[各级标题](#一级标题)<br />
[代码](####代码：)<br />
[代码块](####代码块:)<br />
[各字体样式](####粗体：)<br />
[任务列表](####任务列表：)<br />
[表格](####表格：)<br />
[各种列表](####无序列表：)<br />
[分割线](####分割线：)<br />
[区块](####区块：)<br />
[各种链接](####链接：)<br />
[各种图片](####图片：)<br />
[脚注](####脚注)<br />
[html](####执行html)<br />

## 正文
<br /><br /><br />






# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题



#### 代码：
`hello world`<br />

#### 代码块:
<br />

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

#### 粗体：

**hello world**<br />

#### 斜体：

*hello world*<br />

#### 粗斜体：

***hello world***<br />

#### 删除线：

~~hello world~~<br />

#### 任务列表：

<br />

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

#### 表格：

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

#### 无序列表：

- hello
- hi

#### 有序列表：

1. hello
2. hi

#### 分割线：

***

#### 区块：

>1
>>2
>>>3
>>>>4
>>>>>5
>>>>>>6
>>>>>>
>>>>>>>7

#### 链接：

<br />

[百度](https://baidu.com)<br />

<https://baidu.com><br />


#### 邮箱地址链接：

<br />

<1297537384@qq.com>

#### 图片：

<br />

![这是一张图片](https://tse3-mm.cn.bing.net/th/id/OIP.xOQUhfybP1oWi8Ec1DvxBAHaEK?pid=Api&rs=1)

#### 带链接的图片：
<br />

[![这是一张图片](https://tse3-mm.cn.bing.net/th/id/OIP.xOQUhfybP1oWi8Ec1DvxBAHaEK?pid=Api&rs=1"我是链接")](https://markdown.com.cn)

#### 脚注
hello world[^脚注1]

[^脚注1]:这是个脚注

#### 执行html
ps：如果你的查看Markdown工具能兼容的话你应该能看到背景动画
查看一下这个Markdown文件的源代码应该能看到这下面有HTML代码


<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World!</title>
	<style>
		/*鼠标样式动画*/
body{
    background-repeat: repeat;
    background-attachment: fixed;
    background-size:cover;
     cursor: url(https://files.cnblogs.com/files/monster-jian/cursor.ico),auto;
}
  </style>
</head>

<script src="https://xswl.rthe.net/canvas-nest.js" color="255,255,255" opacity="1" count="300" zindex="-2">
</script>

<div id="fireworks"></div>
<script src="https://xswl.rthe.net/%E7%83%9F%E8%8A%B1%E7%89%B9%E6%95%88.js"></script>
<script>
    var yh = new CursorSpecialEffects();
    yh.init();
</script>


</body>
</html>
<br /><br />












# 世界上有没有最好的Markdown编辑器、查看器？
答案是没有，有的编辑器可能不支持JavaScript脚本（有道云笔记、typora），有的编辑器可能不支持任务列表（VS code）......






