# 接口自动化规则：

1.必须有的四个一级关键字：name,base_url,request,validate

2.在request一级关键字下必须包含两个二级关键字，method、URL

3.传参方式：在request一级关键字下，通过二级关键字参数

    如果是get请求，通过params传参
    如果是post请求
        传json格式，通过json关键字传参
        传表单格式，通过data关键字传参
        传文件格式，通过files关键字传参
          files:
             media:"d:\1.png"

4.如果需要做接口关联的话，必须使用一级关键字，extract，如
    extract：
        json提取方式
        access_token： access_token
        正则表达式提取方式
        access_token: '"access_token":"(.*?)"'
    取值：如：${get_extract_data(access_token)}

 5.热加载：
    当yaml需要使用动态参数时，那么可以做debug_talk.py文件中写方法调用
    注意：传参时，需要什么类型的数据，需要做强转，int（min）

6.csv
    name,appid,secret,grant_type,assert_str
    获得token接口,wx74a8627810cfa308,e40a02f9d79a8097df497e6aaf93ab80,client_credential,access_token
    appid必填项检查,"",e40a02f9d79a8097df497e6aaf93ab80,client_credential,errcode
    secret必填项检查,wx74a8627810cfa308,"",client_credential,errcode


7.日志

