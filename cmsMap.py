#!/usr/bin/env python
#coding:utf8

#author: xiaokong

import sys
import os
import re
import logging
import requests
import urlparse
import argparse

try:
    from cmsRule import cmsRules
except SyntaxError as e:
    print 'rule file is error'
    sys.exit(1)

class cmsMap(object):
    
    def __init__(self):
        
        self.__search = dict()
        self.__request = dict()
        self.__header = dict()
        self.__robots = None
        self.__target = None
        self.__body = None
        self.__logger = None
        self.__rules = self.__getRulesDict()
        self.__request,self.__search = self.__parseRules()
    
    #解析规则文件
    #解析格式为{name:[match[1],match[2]]}
    def __parseRules(self):
        
        search = dict()
        request = dict()
       
        for name,rules in self.__rules.items():
            for rule in rules:
                match = rule['match']
                for match_i in match:
                    #动态解析类型
                    if match_i.has_key('request'):
                        if request.has_key(name):
                            request[name].append(match_i['request'])
                        else:
                            request[name] = [match_i['request']]
                    #静态解析类型
                    elif match_i.has_key('body') or match_i.has_key('header') or match_i.has_key('robots'):
                        if search.has_key(name):
                            search[name].append(match_i)
                        else:
                            search[name] = [match_i]
    
        return request,search
        
    #获得响应内容等基本信息
    def __getTargetInfo(self):
        
        status = None
        data = self.__requestUrl(self.__target)
        if data['code'] != 200:
            status = False
        else:
            self.__body = data['content']
            self.__header = data['headers']
            self.__target = data['realUrl'] #重置跳转后获得目标地址
            self.__robots = self.__requestRobots()
            status = True
        
        return status
    
    #判断静态策略是否成功
    def __checkRule(self, rule, body=None, robots=None, headers=None):
        
        result = None
        flag = False    #识别到CMS则赋值为True
        if body == None:
            body = self.__body
        if robots == None:
            robots == self.__robots
        if headers == None:
            headers = self.__header
        
        for bhr,bhr_rule in rule.items():
            #=======BODY======
            if bhr == 'body' and body != None:
                #判断是否需满足多个规则 
                if isinstance(bhr_rule, list):
                    num = 0
                    for i in bhr_rule:
                        if not re.search(i, body, re.IGNORECASE):
                            break
                        num = num + 1
                    if num == len(bhr_rule): 
                        flag = True
                        result =  rule
                    else:
                        flag = False
                        break
                #需满足单个规则
                elif isinstance(bhr_rule, str):
                    if re.search(bhr_rule, body, re.IGNORECASE):
                        flag = True
                        result = rule
                    else:
                        flag = False
                        break
            #=======ROBOTS.TXT======            
            elif bhr == 'robots' and robots != None:
                #需满足多个规则    
                if isinstance(bhr_rule, list):
                    num = 0
                    for i in bhr_rule:
                        if not re.search(i, robots, re.IGNORECASE):
                            break
                        num = num + 1
                    if num == len(bhr_rule): 
                        flag = True
                        result = rule
                    else:
                        flag = False
                        break
                #需满足单个规则
                elif isinstance(bhr_rule, str):
                    if re.search(bhr_rule, robots, re.IGNORECASE):
                        flag = True
                        result = rule
                    else:
                        flag = False
                        break
            #=======SERVER HEADERS======    
            elif bhr == 'header' and len(headers) != 0:
                self.__logger.debug(self.__header)
                for header,header_rule in bhr_rule.items():
                    if not self.__header.has_key(header.lower()):
                        flag = False
                        break
                    #需满足多个规则 
                    elif isinstance(header_rule, list):
                        num = 0
                        for i in bhr_rule:
                            if not re.search(i, headers[header.lower()], re.IGNORECASE):
                                break
                            num = num + 1
                        if num == len(header_rule):
                            flag = True
                            result = rule
                        else:
                            flag = False 
                            break
                    #需满足单个规则
                    elif isinstance(header_rule, str):
                        if re.search(header_rule, headers[header.lower()], re.IGNORECASE):
                            flag = True
                            result = rule
                        else:
                            flag = False
                            break
                            
            #=======新的解析变量判断在此添加====== 
            
        if flag == True:
            return result
        else:
            return False
        
    #判断静态策略
    #解析静态策略的格式为
    #{name:[{'body/header/request':['xxx']},{同左}]}
    #{name:[{'body/header/request':'xxx'},{同左}]}
    def __checkStaticRules(self, ruleCustom=None):
        
        result = None   #保存返回结果
        if ruleCustom == None:
            search = self.__search
        else:
            search = ruleCustom
            
        for name,rules in search.items(): 
        #rules:[{'body/header/request':'xxx'},{同左}]
            for rule in rules:  
            #rule: {'body/header/request':'xxx'}
                status = self.__checkRule(rule)
                if status != False:
                    return (name,status)
        
        return False
        
    #判断动态策略
    #动态请求规则解析格式
    #{name: [{'/123.txt':{'body':'1234'}}]}
    def __checkDynamicRules(self, ruleCustom=None):
        
        result = None
        flag = False
        if ruleCustom == None:
            request = self.__request
        else:
            request = ruleCustom
            
        for name,rules in request.items():
        #rules:[{'/123.txt':{'body':'1234'}}]
            for rule in rules:
            #rule:{'/123.txt':{'body':'1234'}}
                for path,path_rules in rule.items():
                #path_rules:{'body':'1234'}
                    rep = self.__requestUrl(self.__urlUnParse(path=path))
                    if rep['code'] < 0:
                        flag = False
                        break
                    status = self.__checkRule(path_rules, body=rep['content'], headers=rep['headers'])
                    if status != False:
                        flag = True
                        result = (name, rule)
                    else:
                        flag = False
                        break
                        
                if flag == True:
                    return result
        
        return False
        
    #获得规则字典
    def __getRulesDict(self):
        
        rules = dict(vars(cmsRules))
        #删除内置的方法
        if rules.has_key('__doc__'):
            del rules['__doc__']
        if rules.has_key('__module__'):
            del rules['__module__']
        if rules.has_key('__dict__'):
            del rules['__dict__']
        if rules.has_key('__weakref__'):
            del rules['__weakref__']
            
        return rules
    
    #重组URL
    def __urlUnParse(self, path=''):
        
        return self.__target[:len(self.__target)-self.__target[::-1].find('/')] + path
        
    #请求URL
    def __requestUrl(self, url):
        #响应存储内容
        data = {
            'content': None,    #响应内容
            'errorMsg': None,   #响应状态
            'code': None,       #响应状态吗
            'headers': None,    #响应头
            'realUrl': None     #真实URL
        }
        try:
            self.__logger.debug(url)
            #自动读取存储的Cookies
            r = requests.session()
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
            rep = r.get(url, headers=headers, timeout=10)
            #抛出响应为200外的异常
            rep.raise_for_status()
            data['content'] = rep.content
            data['code'] = rep.status_code
            data['headers'] = dict(rep.headers)
            data['realUrl'] = rep.url
        except requests.HTTPError as e:
            data['content'] = rep.content
            data['errorMsg'] = str(e)
            data['headers'] = dict(rep.headers)
            data['code'] = rep.status_code
            self.__logger.debug(url+" : "+data['errorMsg'])
        except requests.ConnectionError as e:
            data['errorMsg'] = str(e)
            data['code'] = -1   #网络异常
            self.__logger.debug(url+" : "+data['errorMsg'])
        except Exception as e:
            data['errorMsg'] = str(e)
            data['code'] = -2   #其他异常
            self.__logger.debug(url+" : "+data['errorMsg'])
        
        return data
    
    #请求robots.txt文件
    def __requestRobots(self):
        
        contentRobots = None
        resRobots = self.__requestUrl(self.__urlUnParse(path='/robots.txt'))
        if resRobots['code'] == 200:
            if 'User-agent:' in resRobots['content']:
                contentRobots = resRobots['content']
        
        if not contentRobots:
            self.__logger.debug(self.__target+" : robots.txt is not exists")
        return contentRobots
    
    #解析结果
    def __parseResult(self, result):
        
        if result != False:
            name = result[0]
            rule = result[1]
            for i in self.__rules[name]:
                if  rule in i['match']:
                    version = i['version']
                    descript = i['description']
                    self.__logger.log(41, 'CMS is identificat : '+str([name, version, descript]))
                    break
                
    def setLogger(self, logger):
        '''添加日志记录'''
        self.__logger = logger
        
    def queryRules(self):
        '''查询所有规则列表'''
        for name,rules in self.__rules.items():
            self.__logger.log(41, str({name: rules}))
    
    def queryRulesReuqest(self):
        '''查询静态规则列表'''
        for name,rules in self.__request.items():
            self.__logger.log(41, str({name: rules}))
        
    def queryRulesSearch(self):
        '''查询动态规则列表'''
        for name,rules in self.__search.items():
            self.__logger.log(41, str({name: rules}))
    
    def checkCmsMap(self, target):
        '''判断目标的CMS类型
           args:target-测试的目标
        '''
        
        self.__target = target
        if not self.__getTargetInfo():
            self.__logger.error(self.__target + ' : access error')
            return False
            
        status = self.__checkStaticRules()
        if status != False:
            self.__logger.debug(str(status))
            self.__parseResult(status)
            return True
        else:
            status = self.__checkDynamicRules()
            self.__logger.debug(str(status))
            self.__parseResult(status)
        
    def testRulesOne(self, ruleName):
        '''单条规则测试
           args: ruleName-要测试规则的变量名
           return：None
        '''
        if not self.__rules.has_key(ruleName):
             self.__logger.error("ruleName is not exists")
        else:
            for rule in self.__rules[ruleName]:
                self.__target = rule['testUrl']
                if not self.__getTargetInfo():
                    self.__logger.error(self.__target+ ' :测试站点访问异常')
                else:
                    if self.__search.has_key(ruleName):
                        self.__logger.debug(str({ruleName: self.__search[ruleName]}))
                        result = self.__checkStaticRules(ruleCustom={ruleName: self.__search[ruleName]})
                        self.__logger.log(41, str(result))
                    if self.__request.has_key(ruleName):
                        self.__logger.debug(str({ruleName: self.__request[ruleName]}))
                        result = result = self.__checkDynamicRules(ruleCustom={ruleName: self.__request[ruleName]})
                        self.__logger.log(41, str(result))
            
    def testRulesAll(self):
        '''所有规则测试
           return: None
        '''
        for name,rules in self.__rules.items():
            for rule in rules:
                self.__target = rule['testUrl']
                if not self.__getTargetInfo():
                    self.__logger.error(self.__target+ ' :测试站点访问异常')
                else:
                    if self.__checkStaticRules() == False and self.__checkDynamicRules() == False:
                        self.__logger.log(41, str({name: rule}))
        
def logger(v):
    
    logging.addLevelName(41, 'VUL')
    logger = logging.getLogger('cmsMap')
    
    try:
        from logutils.colorize import ColorizingStreamHandler
        handler = ColorizingStreamHandler(sys.stdout)
        handler.level_map[logging.getLevelName('VUL')] = (None, 'red', True)
        handler.level_map[logging.INFO] = (None, 'white', False)
    except ImportError:
        handler = logging.StreamHandler(sys.stdout)
    
    formatter = logging.Formatter("%(message)s", "%Y-%m-%d %H:%M:%S") 
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(v*10)
    
    return logger
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', dest='target', help='Target URL')
    parser.add_argument('-c', dest='ruleName', type=str, help='test one rule of name')
    parser.add_argument('-t', '--test', dest='test', action='store_true', help='test all rules')
    parser.add_argument('-s', '--static', dest='search', action='store_true', help='show static rules')
    parser.add_argument('-d', '--dynamic', dest='request', action='store_true', help='show dynamic rules')
    parser.add_argument('-a', '--all', dest='rules', action='store_true', help='show all rules')
    parser.add_argument('-v', dest='verbose', choices=[1,2,3], default=4, type=int, help='show debug')
    
    p = parser.parse_args()
    cmsMap = cmsMap()
    cmsMap.setLogger(logger(p.verbose))
        
    if p.target:
        if 'http://' in p.target:
            target = p.target
        else:
            target = 'http://' + p.target
            
        cmsMap.checkCmsMap(target)
    elif p.ruleName:
        cmsMap.testRulesOne(p.ruleName)
    elif p.test:
        cmsMap.testRulesAll()
    elif p.rules:
        cmsMap.queryRules()
    elif p.search:
        cmsMap.queryRulesSearch()
    elif p.request:
        cmsMap.queryRulesReuqest()
    else:
        parser.print_help()  
    
    