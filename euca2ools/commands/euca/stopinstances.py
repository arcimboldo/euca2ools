# Software License Agreement (BSD License)
#
# Copyright (c) 20092011, Eucalyptus Systems, Inc.
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms, with or
# without modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other
#   materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Neil Soman neil@eucalyptus.com
#         Mitch Garnaat mgarnaat@eucalyptus.com

import euca2ools.commands.eucacommand
from boto.roboto.param import Param

class StopInstances(euca2ools.commands.eucacommand.EucaCommand):

    Description = 'Stops the specified EBS-based instances.'
    Options = [Param(name='force', short_name='f', long_name='force',
                    optional=True, ptype='boolean', default=False,
                    doc='Forces the instance to stop.')]
    Args = [Param(name='instance_id', ptype='string',
                  optional=False, cardinality='+',
                  doc='unique identifier for instance to stop')]

    def display_instances(self, instances):
        for instance in instances:
            print 'INSTANCE\t%s' % instance.id
            
    def main(self):
        conn = self.make_connection_cli()
        return self.make_request_cli(conn, 'stop_instances',
                                     instance_ids=self.instance_id,
                                     force=self.force)

    def main_cli(self):
        instances = self.main()
        self.display_instances(instances)

