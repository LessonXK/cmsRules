#!/usr/bin/env python
#coding:utf8

class cmsRules(object):

    kesion = [{
    
        'version': 'All', 'description': 'KesionCMS',
        'testUrl': 'http://www.qiaochang.com/',
        'match': 
        [
            {'body': '/ks_inc/common.js'},
            {'body': 'publish by KesionCMS'}
        ]
    }]
        
    douphp = [{
            
        'version': 'All', 'description': 'DouPHP',
        'testUrl': 'http://www.yjqchina.com/',
        'match': 
        [
            {'body': 'Powered by DouPHP'},
            {'body': ['controlBase','indexLeft','recommendProduct']}
        ]
    }]
    
    rongji = [{
            
        'version': 'All', 'description': 'rongjiCMS',
        'testUrl': 'http://www.fjtzb.org.cn/',
        'match': 
        [
            {'body': '<link id="cms_sys_link0" href="/fpd/global.css" rel="stylesheet" type="text/css"/>'}
        ]
    }]
    
    aspcms = [{
            
        'version': 'All', 'description': 'ASPCMS',
        'testUrl': 'http://www.wenpaoji666.com/',
        'match': 
        [
            {'body': '/inc/AspCms_AdvJs.asp'}
        ]
    }]
    
    wordpress = [{
            
        'version': 'All', 'description': 'WordPress',
        'testUrl': 'http://68.46.4.97:44818/',
        'match': 
        [
            {'body': 'content="WordPress'},
            {'header': {'X-Pingback': '/xmlrpc.php'}, 'body': '/wp-includes/'}
        ]
    }]
    
    joomla = [{
            
        'version': 'All', 'description': 'Joomla',
        'testUrl': 'http://59.125.46.167:1080',
        'match': 
        [
            {'body': 'content="Joomla'},
            {'body': ['/media/system/js/core.js','/media/system/js/mootools-core.js']}
        ]
    }]
    
    dedecms = [{
            
        'version': 'All', 'description': 'DedeCms',
        'testUrl': 'http://www.jingyitech.cn',
        'match': 
        [
            {'body': '/templets/default/style/dedecms.css'},
            {'body': ['Powered by', 'http://www.dedecms.com/','DedeCMS']},
            {'body': 'Power by DedeCms'},
            {'request': {'/data/admin/ver.txt':{'body': '^20[0-9][0-9][0-1][0-9][0-3][0-9]$'}}}
        ]
    }]
    
    metinfo = [{
            
        'version': 'All', 'description': 'MetInfo',
        'testUrl': 'http://www.020chigo.com/',
        'match': 
        [
            {'body': '/images/css/metinfo.css'},
            {'body': 'Powered by MetInfo'},
            {'body': 'powered_by_metinfo'},
            {'body': 'content="MetInfo'}
        ]
    }]
    
    empire = [{
            
        'version': 'All', 'description': 'Empire',
        'testUrl': 'http://www.weeloo.com/',
        'match': 
        [
            {'body': 'Powered by EmpireCMS'},
        ]
    }]
    
    cmseasy = [{
            
        'version': 'All', 'description': 'CmsEasy',
        'testUrl': 'http://www.youdaihe.com/',
        'match': 
        [
            {'body': 'content="CmsEasy'},
            {'body': 'Powered by CmsEasy'}
        ]
    }]
    
    drupal = [{
            
        'version': 'All', 'description': 'Drupal',
        'testUrl': 'http://80.229.149.166:1080/',
        'match': 
        [
            {'body': 'jQuery.extend\(Drupal.settings'},
            {'body': ['/sites/default/files/', '/sites/all/modules/', '/sites/all/themes/']},
            {'header': {'X-Generator': 'Drupal'}},
            {'body': 'content="Drupal'}
        ]
    }]
    
    thinksaas = [{
            
        'version': 'All', 'description': 'thinkSAAS',
        'testUrl': 'http://www.diwuqu.com/',
        'match': 
        [
            {'body': '/app/home/skins/default/style.css'}
        ]
    }]
    
    jeecms = [{
            
        'version': 'All', 'description': 'JeeCms',
        'testUrl': 'http://59.110.105.40',
        'match': 
        [
            {'body': ['Powered by', 'http://www.jeecms.com', 'JEECMS']},
            {'body': '<title>Powered by JEECMS</title>'},
            {'request': {'/jeeadmin/jeecms/login.do': {'body': '/res/jeecms/css/admin.css'}}}
        ]
    }]
    
    phpcms = [{
            
        'version': 'All', 'description': 'phpCMS',
        'testUrl': 'http://www.cscglzdwgov.com.cn/',
        'match': 
        [
            {'body': '/data/config.js'},
            {'body': 'content="Phpcms'},
            {'body': 'Powered by Phpcms'},
            {'body': ['Powered by', 'http://www.phpcms.cn']},
            {'body': 'templates/default/skins/default/phpcms.css'}
        ]
    }]
    
    pageadmin = [{
            
        'version': 'All', 'description': 'pageAdmin',
        'testUrl': 'http://wmb.shmtu.edu.cn/',
        'match': 
        [
            {'body': 'content="PageAdmin'},
            {'body': 'Powered by PageAdmin'},
            {'body': "Powered by <a href='http://www.pageadmin.net'"},
            {'request': {'/e/master/login.aspx': {'body': '<link rel="stylesheet" href="master.css'}}}
        ]
    }]
    
    _74cms = [{
            
        'version': 'All', 'description': '74CMS',
        'testUrl': 'http://218.201.212.11:8080',
        'match': 
        [
            {'body': 'content="74cms.com'},
            {'body': 'content="\xc6\xef\xca\xbfCMS'},
            {'body': 'Powered by <a href="http://www.74cms.com/"'},
            {'body': ['/templates/default/css/common.css', 'selectjobscategory']}
        ]
    }]
    
    phpshe = [{
            
        'version': 'All', 'description': 'phpShe',
        'testUrl': 'http://182.61.102.110',
        'match': 
        [
            {'body': ['Powered by', 'http://www.phpshe.com']},
            {'request': {'/admin.php?mod=do&act=login': {'body': 'include/class/authcode\.class\.php\?w=80&h=32'}}}
            
        ]
    }]
    