'''
Created by auto_sdk on 2020.04.23
'''
from dingtalk.api.base import RestApi
class OapiTdpTaskBasicUpdateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.microapp_agent_id = None
		self.operator_userid = None
		self.task = None
		self.task_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.tdp.task.basic.update'
