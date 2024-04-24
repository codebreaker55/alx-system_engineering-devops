# Puppet manifest to install flask from pip3 version 2.1.0

# install version 2.1.1 of werkzeug using pip3
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

# install flask package with version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
