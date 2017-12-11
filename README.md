第一个webAPP

新增的系统结构目录
## 代码提示自动不全配置

选择 Perference-Package Settings-SublimeCodeIntel-Settings-User,复制以下配置:

~~~
{
    "codeintel_language_settings": {
        "Python3": {
            "python3": "C:\\Python36\\python.exe",
            "codeintel_scan_extra_dir": [
                "C:\\Python36\\DLLs",
                "C:\\Python36\\Lib",
                "C:\\Python36\\Lib\\site-packages",
                "C:\\Python36\\Lib\\idlelib",
                "C:\\Python36\\python36.zip",
                "C:\\Python36",
                "C:\\Python36\\Lib\\*",
            ],
            "codeintel_scan_files_in_project": true,
            "codeintel_selected_catalogs": []
        },
    }
}
~~~

## 追踪函数、查看系统函数

配置快捷键使其同eclipse,实现ctrl+鼠标左键追踪函数,alt+left/right跳转,alt+/自动提示代码

选择 Perference-package Settings-SublimeCodeIntel-Key Bindings-User

~~~
//自动提示代码
{ "keys": ["alt+/"], "command": "code_intel_auto_complete" },
//跳转到函数定义
{ "keys": ["alt+right"], "command": "goto_python_definition"},
//返回到跳转位置
{ "keys": ["alt+left"], "command": "back_to_python_definition"}
~~~

