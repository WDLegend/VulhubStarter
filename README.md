# VulhubStarter
## 介绍
一个简单的脚本，根据cve列表，批量搭建漏洞测试环境。

## 使用说明

-r 指定vulhub路径，建议弄个备份，因为这个脚本会改文件，而且有些特殊的还得自己改，比如webmin那个只能开在10000端口

-s 设置启动端口，默认为46000， 依次顺序启动

-f -t from to设置启动xx到xx个容器

-x 指定要启动的CVE列表文件，默认是cve_list.txt, 可以不加

-c true/false 需要强制recreate容器的时候加上这个。

## 其他
一键docker kill：docker ps -q | xargs docker kill



