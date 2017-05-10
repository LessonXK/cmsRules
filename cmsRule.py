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
            {'request': {'/wp-login.php': {'body': 'action=lostpassword'}}},
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
            {'body': '/app/home/skins/default/style\.css'}
        ]
    }]
    
    jeecms = [{
            
        'version': 'All', 'description': 'JeeCms',
        'testUrl': 'http://59.110.105.40',
        'match': 
        [
            {'body': ['Powered by', 'http://www.jeecms.com', 'JEECMS']},
            {'body': '<title>Powered by JEECMS</title>'},
            {'request': {'/jeeadmin/jeecms/login.do': {'body': '/res/jeecms/css/admin\.css'}}}
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
            {'body': 'templates/default/skins/default/phpcms\.css'}
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
            {'body': b'content="骑士CMS'},
            {'body': 'Powered by <a href="http://www.74cms.com/"'},
            {'body': ['/templates/default/css/common\.css', 'selectjobscategory']}
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
    
    yuanlue = [{
            
        'version': 'All', 'description': 'yuanlueSoft',
        'testUrl': 'http://www\.zhangzhou\.gov\.cn/',
        'match': 
        [
            {'body': '<LINK charset="UTF-8" href="/cms/templates/\d+/css/header\.css'}
        ]
    }]
    
    twcms = [{
            
        'version': 'All', 'description': 'TWCMS',
        'testUrl': 'http://www.twcms.com/',
        'match': 
        [
            {'body': ['/twcms/theme/','/css/global.css']}
        ]
    }]
    
    siteserver = [{
            
        'version': 'All', 'description': 'SiteServer CMS',
        'testUrl': 'http://www.czwtmme.com/',
        'match': 
        [
            {'body': ['siteserver', 'sitefiles']},
            {'body': ['Powered by', 'http://www\.siteserver\.cn', 'SiteServer CMS']},
            {'body': '<title>Powered by SiteServer CMS</title>'},
            {'body': b'T_系统首页模板'}
        ]
    }]
    
    hdwiki = [{
            
        'version': 'All', 'description': 'HDWiki',
        'testUrl': 'http://wiki.nongwang.com/',
        'match': 
        [
            {'header': {'Set-Cookie' : 'hd_sid='}},
            {'body': 'http://kaiyuan\.hudong\.com\?hf=hdwiki_copyright_kaiyuan'},
            {'body': 'content="HDWiki'},
            {'body': '<title>powered by hdwiki!</title>'}
        ]
    }]
    
    cmstop = [{
            
        'version': 'All', 'description': 'CMSTOP',
        'testUrl': 'http://www.lezhichina.com/',
        'match': 
        [
            {'body': '/css/cmstop-common\.css'},
            {'body': '/js/cmstop-common\.js'},
            {'body': 'cmstop-list-text\.css'},
            {'body': '<a class="poweredby" href="http://www\.cmstop\.com"'}
        ]
    }]
    
    espcms = [{
            
        'version': 'All', 'description': 'ESPCMS',
        'testUrl': 'http://www.ixichong.cn/',
        'match': 
        [
            {'body': ['infolist_fff', '/templates/default/style/tempates_div\.css']},
            {'body': 'Powered by ESPCMS'}
        ]
    }]
    
    evecom = [{
            
        'version': 'All', 'description': 'EVECOM CMS',
        'testUrl': 'http://www.pingtan.gov.cn/',
        'match': 
        [
            {'body': 'href="/jhtml/ct/ct_\d{4}_\d{5}"'}
        ]
    }]
    
    foosun = [{
            
        'version': 'All', 'description': 'DotNetCMS',
        'testUrl': 'http://www.lichenonline.com.cn/',
        'match': 
        [
            {'body': 'For Foosun'},
            {'body': 'Created by DotNetCMS'},
            {'body': 'Powered by www\.Foosun\.net,Products:Foosun Content Manage system'}
        ]
    }]
    
    hanweb = [{
            
        'version': 'All', 'description': 'HanWEB',
        'testUrl': 'http://cupd.cscec.com/',
        'match': 
        [
            {'body': '/jcms_files/jcms'},
            {'body': '<a href=\'http://www\.hanweb\.com\' style=\'display:none\'>'},
            {'body': b'<meta name=\'Generator\' content=\'大汉版通\'>'},
            {'body': b'<meta name=\'Author\' content=\'大汉网络\'>'},
            {'body': b'Produced By 大汉网络'}
        ]
    }]
    
    npoint = [{
            
        'version': 'All', 'description': 'Npoint',
        'testUrl': 'http://192.151.154.82:8080/',
        'match': 
        [
            {'body': '<title>Powered by Npoint</title>'},
            {'body': 'onClick="this\.src=\'\.\./inc/usercode\.asp\?npoint='}
        ]
    }]
    
    emlog = [{
            
        'version': 'All', 'description': 'Emlog CMS',
        'testUrl': 'http://www.0797kj.com/',
        'match': 
        [
            {'body': 'content="emlog"'}
        ]
    }]
    
    ideacms = [{
            
        'version': 'All', 'description': 'IdeaCMS',
        'testUrl': 'http://222.208.39.143/',
        'match': 
        [
            {'body': 'Powered By IdeaCMS'},
            {'body': 'm_ctr32'}
        ]
    }]
    
    tccms = [{
            
        'version': 'All', 'description': 'TCCMS',
        'testUrl': 'http://186181.com/',
        'match': 
        [
            {'body': '<title>Power By TCCMS</title>'},
            {'body': ['index\.php\?ac=link_more', 'index\.php\?ac=news_list']}
        ]
    }]
    
    trscms = [{
            
        'version': 'All', 'description': 'TRSCMS',
        'testUrl': 'http://219.137.59.237:3260/',
        'match': 
        [
            {'body': '0;URL=/wcm'},
            {'body': '/wcm/app/js'},
            {'body': 'window\.location\.href = "/wcm";'},
            {'body': ['forum\.trs\.com\.cn', 'wcm']},
            {'body': b'/wcm" target="_blank">网站管理'},
            {'body': b'/wcm" target="_blank">管理'}
        ]
    }]
    
    keyicms = [{
            
        'version': 'All', 'description': 'KEYICMS',
        'testUrl': 'http://www.bj-buszc.com/',
        'match': 
        [
            {'body': '/Template/PC/Default/css/css\.css'},
            {'body': '/Template/PC/Default 2\.0/css/css\.css'},
        ]
    }]
    
    scms = [{
            
        'version': 'All', 'description': 'S-CMS',
        'testUrl': 'http://www.21jining.com',
        'match': 
        [
            {'body': '/template/s11/wp-content/themes/superscroll-ys/style.css'},
        ]
    }]
    
    edjoy = [{
            
        'version': 'All', 'description': 'ECSCMS',
        'testUrl': 'http://58.214.234.195/',
        'match': 
        [
            {'body': '<edjoy>(\r\n)?$'},
        ]
    }]
    
    sdcms = [{
            
        'version': 'All', 'description': 'SDCMS',
        'testUrl': 'http://219.137.59.237:3260/',
        'match': 
        [
            {'body': 'powered by sdcms'},
            {'body': ['var webroot=', '/js/sdcms.js']}
        ]
    }]
    
    finecms = [{
            
        'version': 'All', 'description': 'TRSCMS',
        'testUrl': 'http://www.wdngtjq.com/',
        'match': 
        [
            {'body': 'Powered by FineCMS'},
            {'body': 'dayrui@gmail.com'},
            {'body': 'Copyright" content="FineCMS'}
        ]
    }]