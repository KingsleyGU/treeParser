	#################
	# Quantitative Annotations #
	#################
qa = {
	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(finn finds fileX in the file system of entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>finn finds fileX in the file system of entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(big escalates privileges in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>big escalates privileges in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(terry finds fileX in the file system of entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>terry finds fileX in the file system of entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(terry mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it)':
	'<node refinement="disjunctive">' +
		'<label>terry mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(grey bypases authentication in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>grey bypases authentication in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(sydney bypases authentication in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>sydney bypases authentication in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">M</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(big finds fileX in the file system of entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>big finds fileX in the file system of entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(grey escalates privileges in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>grey escalates privileges in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(grey mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it)':
	'<node refinement="disjunctive">' +
		'<label>grey mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(terry bypases authentication in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>terry bypases authentication in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(terry escalates privileges in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>terry escalates privileges in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(sydney escalates privileges in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>sydney escalates privileges in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(finn bypases authentication in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>finn bypases authentication in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(cleo finds fileX in the file system of entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>cleo finds fileX in the file system of entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(administrators escalates privileges in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>administrators escalates privileges in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(cleo bypases authentication in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>cleo bypases authentication in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(finn mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it)':
	'<node refinement="disjunctive">' +
		'<label>finn mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(administrators bypases authentication in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>administrators bypases authentication in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(cleo escalates privileges in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>cleo escalates privileges in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(administrator escalates privileges in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>administrator escalates privileges in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(administrators finds fileX in the file system of entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>administrators finds fileX in the file system of entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(administrator finds fileX in the file system of entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>administrator finds fileX in the file system of entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(sydney mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it)':
	'<node refinement="disjunctive">' +
		'<label>sydney mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(ethan escalates privileges in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>ethan escalates privileges in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(big bypases authentication in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>big bypases authentication in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(administrators mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it)':
	'<node refinement="disjunctive">' +
		'<label>administrators mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(ethan mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it)':
	'<node refinement="disjunctive">' +
		'<label>ethan mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(big mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it)':
	'<node refinement="disjunctive">' +
		'<label>big mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">M</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">M</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(administrator mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it)':
	'<node refinement="disjunctive">' +
		'<label>administrator mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(cleo mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it)':
	'<node refinement="disjunctive">' +
		'<label>cleo mounts the HD of entity_vim.VirtualMachine_vm-51 and inspects it</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(ethan finds fileX in the file system of entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>ethan finds fileX in the file system of entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(sydney finds fileX in the file system of entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>sydney finds fileX in the file system of entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(administrator bypases authentication in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>administrator bypases authentication in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(ethan bypases authentication in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>ethan bypases authentication in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">M</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(finn escalates privileges in entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>finn escalates privileges in entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrator ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(grey finds fileX in the file system of entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>grey finds fileX in the file system of entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN finn ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

}