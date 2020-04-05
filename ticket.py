from atlassian import Jira
import json
import os
import sys

GET_TICKETS_TO_DEPLOY = os.getenv('TICKETS_TO_DEPLOY', False)

class DeploymentTicket:
    def __init__(self):
        __ATLASSSIAN_BASE_URI = os.getenv('ATLASSSIAN_BASE_URI', False)
        __ATLASSIAN_USER = os.getenv('ATLASSIAN_USER', False)
        __ATLASSIAN_API_KEY = os.getenv('ATLASSIAN_API_KEY', False)

        if any([__ATLASSSIAN_BASE_URI is False,  __ATLASSIAN_USER is False, __ATLASSIAN_API_KEY is False]):
            raise Exception('One or more environment variables are not set')

        self.jira = Jira(
            url=__ATLASSSIAN_BASE_URI,
            username=__ATLASSIAN_USER,
            password=__ATLASSIAN_API_KEY)

    def getTickets(self):
        JQL = GET_TICKETS_TO_DEPLOY
        data = self.jira.jql(JQL)

        if 'total' not in data:
            sys.exit(data)

        if data['total'] > 0:
            print(self.getHeader(data))
            print(self.getBody(data['issues']))
            print(self.getFooter())
        else:
            print("No issues ready to deploy at this moment")

    def getAssigne(self, value, defaultValue):
        if value is None:
            return defaultValue
        else:
            return value['key']

    def getHeader(self, data):
        total = data['total']
        tickets = ''
        for record in data['issues']:
            tickets += '{},'.format(record['key'])

        header = 'Total Ticket Count: *{}* [Filter|{}/issues/?jql=Key%20in%20({})] \n\n'.format(
            total, self.jira.url, tickets)
        header += 'h2. Tickets By Engineer: \n'
        return header

    def getBody(self, issues):
        body = ''
        assignee = ''
        for record in issues:
            currentAssignee = self.getAssigne(
                record['fields']['assignee'], 'Undefined')

            if assignee != currentAssignee:
                body += '[~{}] \n'.format(currentAssignee)
                assignee = currentAssignee

            body += '# {} {} \n'.format(record['key'],
                                        record['fields']['summary'].encode('utf-8', errors='ignore'))

        return body

    def getFooter(self):
        footer = 'commit: \n'
        footer += 'pipeline: \n'

        return footer

if __name__ == '__main__':
    deploymentTicket = DeploymentTicket()
    deploymentTicket.getTickets()
