# Using Puppet, create a manifest that kills a process named killmenow

exec { 'pKill':
  command  => 'pKill killmenow',
  provider => 'shell'
}
