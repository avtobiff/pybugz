#!/usr/bin/env python

import argparse

from bugz import __version__
from bugz.cli import PrettyBugz
from bugz.config import config

def make_attach_parser(subparsers):
	attach_parser = subparsers.add_parser('attach',
		help = 'attach file to a bug')
	attach_parser.add_argument('bugid',
		help = 'the ID of the bug where the file should be attached')
	attach_parser.add_argument('filename',
		help = 'the name of the file to attach')
	attach_parser.add_argument('-c', '--content-type',
		default='text/plain',
		help = 'mimetype of the file (default: text/plain)')
	attach_parser.add_argument('-d', '--description',
		help = 'a description of the attachment.')
	attach_parser.add_argument('-p', '--patch',
		action='store_true',
	help = 'attachment is a patch')
	attach_parser.set_defaults(func = PrettyBugz.attach)

def make_attachment_parser(subparsers):
	attachment_parser = subparsers.add_parser('attachment',
		help = 'get an attachment from bugzilla')
	attachment_parser.add_argument('attachid',
		help = 'the ID of the attachment')
	attachment_parser.add_argument('-v', '--view',
		action="store_true",
		default = False,
		help = 'print attachment rather than save')
	attachment_parser.set_defaults(func = PrettyBugz.attachment)

def make_get_parser(subparsers):
	get_parser = subparsers.add_parser('get',
		help = 'get a bug from bugzilla')
	get_parser.add_argument('bugid',
		help = 'the ID of the bug to retrieve.')
	get_parser.add_argument("-a", "--no-attachments",
		action="store_false",
		default = True,
		help = 'do not show attachments',
		dest = 'attachments')
	get_parser.add_argument("-n", "--no-comments",
		action="store_false",
		default = True,
		help = 'do not show comments',
		dest = 'comments')
	get_parser.set_defaults(func = PrettyBugz.get)

def make_modify_parser(subparsers):
	modify_parser = subparsers.add_parser('modify',
		help = 'modify a bug (eg. post a comment)')
	modify_parser.add_argument('bugid',
		help = 'the ID of the bug to modify')
	modify_parser.add_argument('-a', '--assigned-to',
		help = 'change assignee for this bug')
	modify_parser.add_argument('-C', '--comment-editor',
		action='store_true',
		help = 'add comment via default editor')
	modify_parser.add_argument('-F', '--comment-from',
		help = 'add comment from file.  If -C is also specified, the editor will be opened with this file as its contents.')
	modify_parser.add_argument('-c', '--comment',
		help = 'add comment from command line')
	modify_parser.add_argument('-d', '--duplicate',
		type = int,
		default = 0,
		help = 'this bug is a duplicate')
	modify_parser.add_argument('-k', '--keywords',
		help = 'set bug keywords'),
	modify_parser.add_argument('--priority',
		choices=config.choices['priority'].values(),
		help = 'change the priority for this bug')
	modify_parser.add_argument('-r', '--resolution',
		choices=config.choices['resolution'].values(),
		help = 'set new resolution (only if status = RESOLVED)')
	modify_parser.add_argument('-s', '--status',
		choices=config.choices['status'].values(),
		help = 'set new status of bug (eg. RESOLVED)')
	modify_parser.add_argument('-S', '--severity',
		choices=config.choices['severity'],
		help = 'set severity for this bug')
	modify_parser.add_argument('-t', '--title',
		help = 'set title of bug')
	modify_parser.add_argument('-U', '--url',
		help = 'set URL field of bug')
	modify_parser.add_argument('-w', '--whiteboard',
		help = 'set Status whiteboard'),
	modify_parser.add_argument('--add-cc',
		action = 'append',
		help = 'add an email to the CC list')
	modify_parser.add_argument('--remove-cc',
		action = 'append',
		help = 'remove an email from the CC list')
	modify_parser.add_argument('--add-dependson',
		action = 'append',
		help = 'add a bug to the depends list')
	modify_parser.add_argument('--remove-dependson',
		action = 'append',
		help = 'remove a bug from the depends list')
	modify_parser.add_argument('--add-blocked',
		action = 'append',
		help = 'add a bug to the blocked list')
	modify_parser.add_argument('--remove-blocked',
		action = 'append',
		help = 'remove a bug from the blocked list')
	modify_parser.add_argument('--component',
		help = 'change the component for this bug')
	modify_parser.add_argument('--fixed',
		action='store_true',
		help = 'mark bug as RESOLVED, FIXED')
	modify_parser.add_argument('--invalid',
		action='store_true',
		help = 'mark bug as RESOLVED, INVALID')
	modify_parser.set_defaults(func = PrettyBugz.modify)

def make_namedcmd_parser(subparsers):
	namedcmd_parser = subparsers.add_parser('namedcmd',
		help = 'run a stored search')
	namedcmd_parser.add_argument('command',
		help = 'the name of the stored search')
	namedcmd_parser.add_argument('--show-status',
		action = 'store_true',
		help = 'show status of bugs')
	namedcmd_parser.add_argument('--show-url',
		action = 'store_true',
		help = 'show bug id as a url')
	namedcmd_parser.set_defaults(func = PrettyBugz.namedcmd)

def make_post_parser(subparsers):
	post_parser = subparsers.add_parser('post',
		help = 'post a new bug into bugzilla')
	post_parser.add_argument('--product',
		help = 'product')
	post_parser.add_argument('--component',
		help = 'component')
	post_parser.add_argument('--prodversion',
		help = 'version of the product')
	post_parser.add_argument('-t', '--title',
		help = 'title of bug')
	post_parser.add_argument('-d', '--description',
		help = 'description of the bug')
	post_parser.add_argument('-F' , '--description-from',
		help = 'description from contents of file')
	post_parser.add_argument('--append-command',
		help = 'append the output of a command to the description')
	post_parser.add_argument('-a', '--assigned-to',
		help = 'assign bug to someone other than the default assignee')
	post_parser.add_argument('--cc',
		help = 'add a list of emails to CC list')
	post_parser.add_argument('-U', '--url',
		help = 'URL associated with the bug')
	post_parser.add_argument('--depends-on',
		help = 'add a list of bug dependencies',
		dest='dependson')
	post_parser.add_argument('--blocked',
		help = 'add a list of blocker bugs')
	post_parser.add_argument('-k', '--keywords',
		help = 'list of bugzilla keywords')
	post_parser.add_argument('--batch',
		action="store_true",
		help = 'do not prompt for any values')
	post_parser.add_argument('--default-confirm',
		choices = ['y','Y','n','N'],
		default = 'y',
		help = 'default answer to confirmation question')
	post_parser.add_argument('--priority',
		choices=config.choices['priority'].values(),
		help = 'set priority for the new bug')
	post_parser.add_argument('-S', '--severity',
		choices=config.choices['severity'],
		help = 'set the severity for the new bug')
	post_parser.set_defaults(func = PrettyBugz.post)

def make_search_parser(subparsers):
	search_parser = subparsers.add_parser('search',
		help = 'search for bugs in bugzilla')
	search_parser.add_argument('terms',
		nargs='*',
		help = 'strings to search for in title or body')
	search_parser.add_argument('-o', '--order',
		choices = config.choices['order'].keys(),
		default = 'number',
		help = 'display bugs in this order')
	search_parser.add_argument('-a', '--assigned-to',
		help = 'email the bug is assigned to')
	search_parser.add_argument('-r', '--reporter',
		help = 'email the bug was reported by')
	search_parser.add_argument('--cc',
		help = 'restrict by CC email address')
	search_parser.add_argument('--commenter',
		help = 'email that commented the bug')
	search_parser.add_argument('-s', '--status',
		action='append',
		help = 'restrict by status (one or more, use all for all statuses)')
	search_parser.add_argument('--severity',
		action='append',
		choices = config.choices['severity'],
		help = 'restrict by severity (one or more)')
	search_parser.add_argument('--priority',
		action='append',
		choices = config.choices['priority'].values(),
		help = 'restrict by priority (one or more)')
	search_parser.add_argument('-c', '--comments',
		action='store_true',
		default=None,
		help = 'search comments instead of title')
	search_parser.add_argument('--product',
		action='append',
		help = 'restrict by product (one or more)')
	search_parser.add_argument('-C', '--component',
		action='append',
		help = 'restrict by component (1 or more)')
	search_parser.add_argument('-k', '--keywords',
		help = 'restrict by keywords')
	search_parser.add_argument('-w', '--whiteboard',
		help = 'status whiteboard')
	search_parser.add_argument('--show-status',
		action = 'store_true',
		help='show status of bugs')
	search_parser.add_argument('--show-url',
		action = 'store_true',
		help='show bug id as a url.')
	search_parser.set_defaults(func = PrettyBugz.search)

def make_parser():
	parser = argparse.ArgumentParser(
		epilog = 'use -h after a sub-command for sub-command specific help')
	parser.add_argument('-b', '--base',
		default = 'https://bugs.gentoo.org/',
		help = 'base URL of Bugzilla')
	parser.add_argument('-u', '--user',
		help = 'username for commands requiring authentication')
	parser.add_argument('-p', '--password',
		help = 'password for commands requiring authentication')
	parser.add_argument('-H', '--httpuser',
		help = 'username for basic http auth')
	parser.add_argument('-P', '--httppassword',
		help = 'password for basic http auth')
	parser.add_argument('-f', '--forget',
		action='store_true',
		help = 'forget login after execution')
	parser.add_argument('-q', '--quiet',
		action='store_true',
		default = False,
		help = 'quiet mode')
	parser.add_argument('--columns', 
		type = int,
		default = 0,
		help = 'maximum number of columns output should use')
	parser.add_argument('--encoding',
		help = 'output encoding (default: utf-8).')
	parser.add_argument('--skip-auth',
		action='store_true',
		default = False,
		help = 'skip Authentication.')
	parser.add_argument('--version',
		action='version',
		help='show program version and exit',
		version='%(prog)s ' + __version__)
	subparsers = parser.add_subparsers(help = 'help for sub-commands')
	make_attach_parser(subparsers)
	make_attachment_parser(subparsers)
	make_get_parser(subparsers)
	make_modify_parser(subparsers)
	make_namedcmd_parser(subparsers)
	make_post_parser(subparsers)
	make_search_parser(subparsers)
	return parser

def get_kwds(args):
	bugz = {}
	cmd = {}
	global_attrs = ['user', 'password', 'httpuser', 'httppassword', 'forget',
		'base', 'columns', 'encoding', 'quiet', 'skip_auth']
	for attr in dir(args):
		if attr[0] != '_' and attr != 'func':
			if attr in global_attrs:
				bugz[attr] = getattr(args,attr)
			else:
				cmd[attr] = getattr(args,attr)
	return bugz, cmd
