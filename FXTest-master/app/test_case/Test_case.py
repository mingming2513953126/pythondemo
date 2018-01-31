# -*- coding: utf-8 -*-
# @Date    : 2017-07-20 21:06:16
# @Author  : lileilei
from app.common.requ_case import Api
from app.common.dict_com import assert_in
from app.common.log import log_t
class ApiTestCase():
    def __init__(self,inteface_url,inteface_meth,inteface_parm,inteface_assert,file,headers):
        self.result_pass=0
        self.result_fail=0
        self.result_toal=0
        self.url=inteface_url
        self.meth=inteface_meth
        self.parm=inteface_parm
        self.assert_test=inteface_assert
        self.bask_list=[]
        self.result_pf=[]
        self.headers=headers
        self.title = u'测试日志'
        self.log_can = log_t(self.title, filename=file)
    def testapi(self):
        for case in range(len(self.url)):
            api=Api(url=self.url[case],fangshi=self.meth[case],params=self.parm[case],headers=self.headers[case])
            apijson=api.getJson()
            self.log_can.info_log(u'测试的:接口地址：%s,请求头：%s,参数:%s,实际返回:%s,预期:%s'%(self.url[case],self.headers[case],self.parm[case],apijson,self.assert_test[case]))
            come=assert_in(self.assert_test[case],apijson)
            if come=='pass':
                self.result_pass+=1
                self.result_toal+=1
                self.bask_list.append(apijson)
                self.result_pf.append('pass')
            else:
                self.result_fail+=1
                self.result_toal+=1
                self.bask_list.append(apijson)
                self.result_pf.append('fail')
        return self.result_toal ,self.result_pass,self.result_fail,self.result_pf,self.bask_list