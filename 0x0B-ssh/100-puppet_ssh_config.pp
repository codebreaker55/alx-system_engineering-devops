#!/usr/bin/env bash
# using Puppet to make changes to our configuration file.

file {'/etc/ssh/ssh_config':
	ensure => present,
	content => "\
	# SH client configuration must be configured to use the private key ~/.ssh/school
	IdentityFile ~/.ssh/school

	# SSH client configuration must be configured to refuse to authenticate using a password
	PasswordAuthentication no
	",
}
