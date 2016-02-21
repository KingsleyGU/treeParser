	#################
	# Quantitative Annotations #
	#################
qa = {
	r'(\s*IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
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

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
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

	r'(\s*IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
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

	r'(\s*IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN terry DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>IN terry DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51</label>' +
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

	r'(\s*IN terry ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN cleo DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51</label>' +
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

	r'(\s*IN sydney DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">TODO</parameter>' +
		'<parameter name="likelihood" class="ordinal">TODO</parameter>' +
		'<parameter name="difficulty" class="ordinal">TODO</parameter>' +
		'<parameter name="time" class="ordinal">TODO</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">M</parameter>' +
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

	r'(\s*IN grey ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN cleo ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
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

	r'(\s*IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN big ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
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

	r'(\s*IN cleo ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
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

	r'(\s*IN administrators ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN big ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
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

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">M</parameter>' +
		'<parameter name="difficulty" class="ordinal">M</parameter>' +
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

	r'(\s*IN grey ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
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

	r'(\s*IN administrators ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN cleo ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN administrator ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN sydney ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN ethan DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
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

	r'(\s*IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
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

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN big ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN big DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>IN big DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN terry ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-45 entity_vim.Network_network-45</label>' +
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

	r'(\s*IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN grey DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>IN grey DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN finn ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
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

	r'(\s*IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
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

	r'(\s*IN administrator ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN administrators ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
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

	r'(\s*IN administrator DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
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

	r'(\s*IN cleo ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
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

	r'(\s*IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
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

	r'(\s*IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
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

	r'(\s*IN sydney ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.Network_network-43 entity_vim.Network_network-43 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 LOCATION RoomDatacenter RoomDatacenter</label>' +
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

	r'(\s*IN ethan ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN sydney ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
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

	r'(\s*IN big ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN big ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
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

	r'(\s*IN finn DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>IN finn DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51</label>' +
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

	r'(\s*IN finn ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN finn ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-42 entity_vim.Network_network-42</label>' +
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

	r'(\s*IN sydney ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN sydney ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">V</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN administrator ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41 LOCATION RoomDatacenter RoomDatacenter</label>' +
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

	r'(\s*IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN grey ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
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

	r'(\s*IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

	r'(\s*IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN terry ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
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

	r'(\s*IN ethan ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.Network_network-42 entity_vim.Network_network-42 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN administrators ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators ITEM entity_vim.Network_network-44 entity_vim.Network_network-44 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
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

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Datastore_datastore-41 entity_vim.Datastore_datastore-41</label>' +
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

	r'(\s*IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44)':
	'<node refinement="disjunctive">' +
		'<label>IN administrator ITEM entity_vim.HostSystem_host-49 entity_vim.HostSystem_host-49 ITEM entity_vim.Network_network-44 entity_vim.Network_network-44</label>' +
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

	r'(\s*IN ethan ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43)':
	'<node refinement="disjunctive">' +
		'<label>IN ethan ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51 ITEM entity_vim.Network_network-43 entity_vim.Network_network-43</label>' +
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

	r'(\s*IN cleo ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter)':
	'<node refinement="disjunctive">' +
		'<label>IN cleo ITEM entity_vim.Network_network-45 entity_vim.Network_network-45 LOCATION RoomDatacenter RoomDatacenter</label>' +
		'<parameter name="cost" class="numeric">0</parameter>' +
		'<parameter name="likelihood" class="ordinal">H</parameter>' +
		'<parameter name="difficulty" class="ordinal">L</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN administrators DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51)':
	'<node refinement="disjunctive">' +
		'<label>IN administrators DATA fileX fileX ITEM entity_vim.VirtualMachine_vm-51 entity_vim.VirtualMachine_vm-51</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
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

}