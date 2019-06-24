import traceback
import datetime
import sys
import threading
import smtplib
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from config import config
from core import models
import const


def send(body):
    subject = body.get('subject', '')
    mail_to = body.get('to', [])
    mail_from = body.get('from', config.MAIL_SEND)
    copy_to = body.get('cc', [])
    content = body.get('body', '')

    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = mail_from
    msg['To'] = ";".join(mail_to)
    msg['Cc'] = ';'.join(copy_to)
    try:
        s = smtplib.SMTP()
        s.connect(config.SMTP_HOST, config.SMTP_PORT)
        s.ehlo()
        s.starttls()
        s.login(config.MAIL_USER, config.MAIL_PASSWORD)
        s.sendmail(config.MAIL_SEND, mail_to + copy_to, msg.as_string())
        sys.stdout.flush()
        s.close()
    except Exception as exception:
        print("send email error ...", "*" * 10)
        print(exception)
        print(traceback.format_exc())


def send_email(body):
    t = threading.Thread(target=send, args=(body,))
    t.start()


def ad2name(ads):
    ads = ads.split(',')
    ads = list(set(ads))
    data = []
    for ad in ads:
        try:
            user = models.User.get(models.User.username == ad)
            if user.name:
                data.append(user.name)
            else:
                data.append(ad)
        except models.User.DoesNotExist:
            data.append(ad)
    return ', '.join(data)


def ad2email(ads):
    ads = ads.split(',')
    ads = list(set(ads))
    data = []
    for ad in ads:
        try:
            user = models.User.get(models.User.username == ad)
            if user.email:
                data.append(user.email)
            else:
                data.append('{0}@BKJK.COM'.format(ad))
        except models.User.DoesNotExist:
            data.append('{0}@BKJK.COM'.format(ad))
    return data


def utc2local(data):
    return data + datetime.timedelta(hours=8)


def deploy_mail(deploy):
    # jinja2 init
    loader = FileSystemLoader('templates')
    env = Environment(loader=loader)
    env.filters['ad2name'] = ad2name
    env.filters['utc2local'] = utc2local
    # 上线流程 通知操作邮件内容
    email_dict = {
        const.WAIT_APPROVE: {
            'operator': 'approver',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 申请上线，请审核',
            'template': 'deploy_approver_mail.html',
        },
        const.WAIT_QA: {
            'operator': 'qa',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 申请上线，等待您的操作',
            'template': 'deploy_operate_mail.html',
        },
        const.WAIT_OPS: {
            'operator': 'ops',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 申请上线，等待您的操作',
            'template': 'deploy_operate_mail.html',
        },
        const.WAIT_DEV: {
            'operator': 'dev',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 申请上线，等待您的操作',
            'template': 'deploy_operate_mail.html',
        },
        const.DONE: {
            'operator': 'all',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 上线完成',
            'template': 'deploy_done_mail.html',
        },
    }
    cc_to_security = None
    if email_dict.get(deploy.status).get('operator') == 'all':
        to_all = [deploy.creator, deploy.approver, deploy.qa, deploy.ops, deploy.dev, deploy.dba, deploy.pm]
        operator = ','.join(to_all)
        cc_to_security = 'security@BKJK.COM'
    elif email_dict.get(deploy.status).get('operator') == 'dev':
        to_all = [deploy.dev, deploy.pm]
        operator = ','.join(to_all)
    elif email_dict.get(deploy.status).get('operator') == 'ops' and deploy.have_sql:
        to_all = [deploy.ops, deploy.dba]
        operator = ','.join(to_all)
    else:
        operator = getattr(deploy, email_dict.get(deploy.status).get('operator'))
    subject = email_dict.get(deploy.status).get('subject')
    template = env.get_template(email_dict.get(deploy.status).get('template'))
    if operator:
        to = ad2email(operator) if operator else []
        to = list(set(to))
        cc = [deploy.cc]
        if cc_to_security:
            cc.append(cc_to_security)
        subject = subject.format(system=deploy.system, version=deploy.version, ID=deploy.id)
        link = const.BASE_DEPLOY_URL.format(deploy_id=deploy.id)
        body = {
            'from': "Dalmore System",
            'subject': subject,
            'to': to,
            'cc': cc,
            'body': template.render(deploy=deploy, operator=operator, link=link)
        }
        send_email(body)


def change_mail(change):
    # jinja2 init
    loader = FileSystemLoader('templates')
    env = Environment(loader=loader)
    env.filters['ad2name'] = ad2name
    env.filters['utc2local'] = utc2local
    # 变更流程 通知操作邮件内容
    email_dict = {
        const.WAIT_APPROVE: {
            'operator': 'approver',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 变更申请[{change_type}]，请审核',
            'template': 'change_approver_mail.html',
        },
        const.WAIT_QA: {
            'operator': 'qa',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 变更申请[{change_type}]，等待您的操作',
            'template': 'change_operate_mail.html',
        },
        const.WAIT_OPS: {
            'operator': 'ops',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 变更申请[{change_type}]，等待您的操作',
            'template': 'change_operate_mail.html',
        },
        const.WAIT_DEV: {
            'operator': 'dev',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 变更申请[{change_type}]，等待您的操作',
            'template': 'change_operate_mail.html',
        },
        const.DONE: {
            'operator': 'all',
            'subject': '[Dalmore ID: {ID}] {system} {version}: 变更完成[{change_type}]',
            'template': 'change_done_mail.html',
        },
    }
    if email_dict.get(change.status).get('operator') == 'all':
        to_all = [change.creator, change.approver, change.qa, change.ops, change.dev, change.pm, change.dba]
        operator = ','.join(to_all)
    elif email_dict.get(change.status).get('operator') == 'dev':
        to_all = [change.dev, change.pm]
        operator = ','.join(to_all)
    elif email_dict.get(change.status).get('operator') == 'ops' and change.have_sql:
        to_all = [change.ops, change.dba]
        operator = ','.join(to_all)
    else:
        operator = getattr(change, email_dict.get(change.status).get('operator'))
    subject = email_dict.get(change.status).get('subject')
    template = env.get_template(email_dict.get(change.status).get('template'))
    if operator:
        to = ad2email(operator) if operator else []
        to = list(set(to))
        cc = [change.cc]
        subject = subject.format(system=change.system, version=change.version, ID=change.id,
                                 change_type=change.change_type)
        link = const.BASE_CHANGE_URL.format(change_id=change.id)
        body = {
            'from': "Dalmore System",
            'subject': subject,
            'to': to,
            'cc': cc,
            'body': template.render(change=change, operator=operator, link=link)
        }
        send_email(body)
