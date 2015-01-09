from fabric.api import env
host1 = 'root@1.1.1.1'
ext_routers = []
router_asn = 64512
host_build = 'root@1.1.1.1'
env.roledefs = {
    'all': [host1],
    'cfgm': [host1],
    'openstack': [host1],
    'control': [host1],
    'compute': [host1],
    'collector': [host1],
    'webui': [host1],
    'database': [host1],
    'build': [host_build],
    'storage-master': [host1],
    'storage-compute': [host1],
}
env.openstack_admin_password = 'secret123'
env.hostnames = {
    'all': ['a0s1']
}
env.password = 'secret'
env.passwords = {
    host1: 'secret',
    host_build: 'secret',
}
env.ostypes = {
    host1:'centos',
}
