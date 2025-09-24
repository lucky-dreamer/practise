用c包裹shell，并且打包成可执行文件，赋予该文件SUID的特殊权限（参考passwd命令的原理），文件的所属者为root，但是普通用户执行这个文件就可以获得root的权限，
使用方法为./sudome <你想用root权限执行的命令>
必须要用root账号给sudome SUID的权限，chmod 4755 sudome
为了防止被误删除，可以chattr +i sudome给隐藏防删权限
