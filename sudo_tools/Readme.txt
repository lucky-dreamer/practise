用c包裹shell，并且c文件打包成可执行文件sudome，赋予该文件SUID的特殊权限（参考passwd命令的原理），文件的所属者为root，但是普通用户执行这个文件就可以获得root的权限，
使用方法为./sudome <你想用root权限执行的命令>
必须要用root账号给sudome SUID的权限，chmod 4755 sudome
为了防止被误删除，可以chattr +i sudome给隐藏防删权限
<开发这个的目的是不得已要给别人root密码的时候，可以不用给root密码，用sudome来执行root命令，同时在sudome写死了包裹的shell的路径，用sudo_conctrol来管控shell是否生成，从而管理sudome的使用与回收时间>


本地让sudome生效：1.加环境变量中可以直接执行，放在/usr/local/bin  下面
                  2.加tap支持，在/usr/share/bash-compition/compitions/中模仿sudo加类似的sudome的规则
                  3.让其与上位机兼容，能支持fsversion的命令，修改/etc/ld.so.conf.d/的配置，在文件里新加platform.conf，里面放缺少的.so所在的路径，然后ldconfig更新就可以

监控：
1.加审计： 在/etc/audit/rules.d/audit.rules里面加入：-w /usr/local/bin/sudome -p x -k suid_access(先为他添加标签)
2.重启服务或者主机生效systemctl restart auditd或auditcl -R /etc/audit/rules.d/audit.rules,验证是否生效auditctl -l
3.执行sudome，并验证 ausearch -k suid_access -i 查看日志
