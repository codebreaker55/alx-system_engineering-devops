# Using Puppet, create a manifest that kills a process named killmenow
exec { 'pkill killmenow':
  path => '/urs/bin:/usr/sbin:/bin',
}

