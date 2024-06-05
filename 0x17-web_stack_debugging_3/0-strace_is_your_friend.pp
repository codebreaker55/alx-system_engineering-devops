# by using strace, find out why Apache is returning a 500 error, then use a puppet to fix
# fixing bad "phpp" extintion to "php" in the wordpress file "wp-settings.php"

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
