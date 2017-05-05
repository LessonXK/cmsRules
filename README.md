# cmsRules

匹配规则:  
[{  
    'version': '1.0', 'description': 'KesionCMS',  
    'testUrl': 'xxxxx',  
    'match':  
    [  
        {'body': '/ks_inc/common.js'},  
    ]  
},  
{
    'version': '2.0', 'description': 'KesionCMS',  
    'testUrl': 'xxxxx',  
    'match':  
    [  
        {'body': 'publish by KesionCMS'}  
    ]  
}]  

匹配字段:  
{'body': 'publish by KesionCMS'}  
{'header': 'publish by KesionCMS'}  
{'robots': 'publish by KesionCMS'}  
{'query': {'/test/123': 'body[publish by KesionCMS]'}}  

满足多个规则其中之一:  
'match':  
[  
    {'body': 'publish by KesionCMS'}  
    {'body': 'publish by KesionCMS'}  
]  

满足多个匹配条件:  
{'query': {'/test/123': ['body[.*]','header[.*]']}}  
{'body': ['test', '1234']}  
{'header': ['publish by KesionCMS','123']}  