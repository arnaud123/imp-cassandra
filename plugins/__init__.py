"""
    Copyright 2013 KU Leuven Research and Development - iMinds - Distrinet

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Administrative Contact: dnet-project-office@cs.kuleuven.be
    Technical Contact: bart.vanbrabant@cs.kuleuven.be
"""
from Imp.plugins.base import plugin, Context
from Imp.execute.proxy import DynamicProxy

@plugin
def seeds(cluster : "cassandra::Cluster") -> "list":
    """
        Finds ALL cassandra nodes in the network, sorts them by IP 
	and returns them.
    """
    return sorted([node.host.ip for node in cluster.servers]);
