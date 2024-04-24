# Puppet manifest to install flask from pip3 version 2.1.0

# install install version 2.0.2 of werkzeug using pip3
package { 'werkzeug':
  ensure   => '2.0.2',
  provider => 'pip3',
}

# install flask package with version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
