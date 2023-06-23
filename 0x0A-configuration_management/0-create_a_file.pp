# create a file in /tmp, set the mode and owners

file {'/tmp/school':
    mode => '0744',
    owner => 'www-data',
    group => 'www-data',
    content => 'I love Puppet'
}
