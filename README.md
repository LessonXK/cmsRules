# cmsRules

[{
    'version': '1.0', 'description': 'KesionCMS',
    'match': 
    [
        {'body': '/ks_inc/common.js'},
    ]
},
{
    'version': '2.0', 'description': 'KesionCMS',
    'match': 
    [
        {'body': 'publish by KesionCMS'}
    ]
}]

匹配方法：

'body': 'publish by KesionCMS' #响应正文正则匹配
'header': 'SERVER: .*ASP' #响应头正则匹配
'robots': '123' #robots.txt正则匹配
'query': {'/test/123': 'body[.*]'} 

需同时满足多个匹配条件时，使用列表形式:

'query': {'/test/123': ['body[.*]','header[.*]']}

-----end----- 
