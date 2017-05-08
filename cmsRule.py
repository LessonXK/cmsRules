#!/usr/bin/env python
#coding:utf8

class cmsRules(object):

    kesion = [{
    
        'version': 'All', 'description': 'KesionCMS',
        'testUrl': 'xxxxx',
        'match': 
        [
            {'body': '/ks_inc/common.js'},
            {'body': 'publish by KesionCMS'}
        ]
    }]
        
    douphp = [{
            
        'version': 'All', 'description': 'DouPHP',
        'testUrl': 'xxxxx',
        'match': 
        [
            {'body': 'Powered by DouPHP'},
            {'body': ['controlBase','indexLeft','recommendProduct']}
        ]
    }]
    
    rongji = [{
            
        'version': 'All', 'description': 'rongjiCMS',
        'testUrl': 'xxxxx',
        'match': 
        [
            {'body': '<link id="cms_sys_link0" href="/fpd/global.css" rel="stylesheet" type="text/css"/>'}
        ]
    }]
    
    aspcms = [{
            
        'version': 'All', 'description': 'ASPCMS',
        'testUrl': 'xxxxx',
        'match': 
        [
            {'body': '/inc/AspCms_AdvJs.asp'}
        ]
    }]
    
    ndasec = [{
            
        'version': 'All', 'description': 'NDASEC WEBSITE',
        'testUrl': 'http://www.ndasec.com',
        'match': 
        [
            {'body': ['/css/v2/common.css','/js/bootstrap.min.js']},
            {'request': {'/aboutus':{'body':['/product_service','/js/bootstrap.min.js']},'/':{'body': 'bbbbbbbbbbbbb'}}}
        ]
    }]
    