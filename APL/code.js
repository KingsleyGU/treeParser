$(function(){ // on dom ready

var edges = [];
var nodes = [];

// data = {"MODELassets":["entity_vim.HostSystem_host-12","admincard","entity_vim.HostSystem_host-20","entity_vim.VirtualMachine_vm-28","entity_vim.VirtualMachine_vm-32","entity_vim.VirtualMachine_vm-27","laptop","entity_vim.Datastore_datastore-13","entity_vim.Network_network-14","entity_vim.VirtualMachine_vm-16","entity_vim.VirtualMachine_vm-29","entity_vim.VirtualMachine_vm-18","entity_vim.VirtualMachine_vm-15","entity_vim.VirtualMachine_vm-26","entity_vim.HostSystem_host-19","usercard","adminpin","userpin","fileX"],"entity_vim.HostSystem_host-19":["entity_vim.Datastore_datastore-13","id-41QsurOkW-node"],"fileX":["entity_vim.VirtualMachine_vm-26"],"entity_vim.Network_network-14":["id-41QsurOkW-node"],"entity_vim.VirtualMachine_vm-18":["entity_vim.Datastore_datastore-13","entity_vim.HostSystem_host-12"],"entity_vim.VirtualMachine_vm-16":["entity_vim.HostSystem_host-12","entity_vim.Datastore_datastore-13"],"id-41gXiuSuyW-node":["id-41gXiuSuyW-node","id-N1-7iOrO1Z-node"],"usercard":["id-NJNSqOHd1W-node"],"laptop":["id-41gXiuSuyW-node"],"id-EJSrc_SO1Z-node":["id-V1XpdrukZ-node"],"id-4JmSqdrO1W-node":["id-V1XpdrukZ-node"],"id-4kHqOBu1--node":["id-V1XpdrukZ-node"],"entity_vim.Datastore_datastore-13":["id-41QsurOkW-node"],"userpin":["usercard","id-NJNSqOHd1W-node"],"id-V1mmodHukb-node":["id-EkGmsdBuyW-node","id-V1mmodHukb-node"],"entity_vim.VirtualMachine_vm-32":["entity_vim.HostSystem_host-12","entity_vim.Datastore_datastore-13"],"entity_vim.VirtualMachine_vm-15":["entity_vim.Datastore_datastore-13","entity_vim.HostSystem_host-12"],"entity_vim.HostSystem_host-12":["entity_vim.Datastore_datastore-13","id-41QsurOkW-node"],"MODELactors":["id-NJNSqOHd1W-node","id-EyMB9_rdk--node","id-4JmSqdrO1W-node","id-EJlr5_H_JZ-node","id-V1WB5_S_JZ-node","id-EJSrc_SO1Z-node","id-4kHqOBu1--node"],"id-V1WB5_S_JZ-node":["id-V1XpdrukZ-node"],"id-V1XpdrukZ-node":["id-V1mmodHukb-node"],"MODELnodes":["id-N1-7iOrO1Z-node","id-41QsurOkW-node","id-V1XpdrukZ-node","id-41gXiuSuyW-node","id-V1mmodHukb-node","id-EkGmsdBuyW-node"],"admincard":["id-4JmSqdrO1W-node"],"id-EyMB9_rdk--node":["id-V1XpdrukZ-node"],"entity_vim.VirtualMachine_vm-27":["entity_vim.Datastore_datastore-13","entity_vim.HostSystem_host-20"],"entity_vim.VirtualMachine_vm-28":["entity_vim.HostSystem_host-20","entity_vim.Datastore_datastore-13"],"entity_vim.VirtualMachine_vm-29":["entity_vim.Datastore_datastore-13","entity_vim.HostSystem_host-20"],"id-41QsurOkW-node":["id-41QsurOkW-node"],"entity_vim.HostSystem_host-20":["entity_vim.Datastore_datastore-13","id-41QsurOkW-node"],"id-NJNSqOHd1W-node":["id-V1XpdrukZ-node"],"id-EJlr5_H_JZ-node":["id-V1XpdrukZ-node"],"adminpin":["admincard","id-4JmSqdrO1W-node"],"id-N1-7iOrO1Z-node":["id-41QsurOkW-node","id-N1-7iOrO1Z-node"],"id-EkGmsdBuyW-node":["id-EkGmsdBuyW-node","id-41gXiuSuyW-node"],"entity_vim.VirtualMachine_vm-26":["entity_vim.Datastore_datastore-13","entity_vim.HostSystem_host-19"]}// $.getJSON( "model.json")
// data = {"DoorInternal":["DoorInternal","RoomInternal"],"MODELassets":["x005","Switch1","Server2","x002","x003","Laptop","VM1","Switch2","Server1","x004","x012","pwdethan","x010","admpwdsydney","x013","x006","x007","x011","fileX","x008","pwdsydney","x009"],"WindowInternal":["WindowInternal","WindowInternal"],"RoomDatacenter":["RoomDatacenter","RoomDatacenter"],"fileX":["VM1","Laptop","Switch1","Switch2"],"admpwdsydney":["Sydney"],"pwdsydney":["Sydney"],"Switch1":["RoomInternal"],"Switch2":["RoomDatacenter"],"VM1":["Server1"],"x002":["Sydney"],"Hallway":["Hallway","Outside","DoorInternal","Hallway","WindowDatacenter"],"x003":["Terry"],"Server2":["RoomDatacenter"],"x004":["Ethan"],"x005":["Finn"],"Server1":["RoomDatacenter"],"x006":["Sydney","x002"],"x007":["Terry","x003"],"Sydney":["Outside"],"Finn":["Outside"],"Laptop":["RoomInternal"],"MODELactors":["Finn","Ethan","Sydney","Terry"],"MODELnodes":["DoorInternal","RoomDatacenter","WindowDatacenter","WindowInternal","DoorDatacenter","DoorExternal","Hallway","Outside","RoomInternal"],"x009":["Finn","x005"],"x008":["Ethan","x004"],"Outside":["DoorExternal","Outside","WindowInternal"],"RoomInternal":["RoomInternal","Hallway","WindowInternal","DoorDatacenter"],"x010":["x002"],"DoorExternal":["DoorExternal","Hallway"],"DoorDatacenter":["DoorDatacenter","RoomDatacenter"],"Terry":["Outside"],"pwdethan":["Ethan"],"Ethan":["Outside"],"WindowDatacenter":["RoomDatacenter","WindowDatacenter"],"x013":["x005"],"x011":["x003"],"x012":["x004"]}
//   .done(function(data) {
    // alert(JSON.stringify(data));
// modelData = {"edges": {"A1door": {"resource": 3, "likelihood": 2, "colorFactor": 3}, "citydoor": {"resource": 4, "likelihood": 2, "colorFactor": 4}}, "nodes": {"door": {"resource": 4, "likelihood": 2, "colorFactor": 4}, "Fred": {"resource": 4, "likelihood": 2, "colorFactor": 4}, "Charlie": {"resource": 3, "likelihood": 1, "colorFactor": 3}, "x004": {"resource": 3, "likelihood": 1, "colorFactor": 2}, "Margrethe": {"resource": 3, "likelihood": 1, "colorFactor": 3}, "x009": {"resource": 3, "likelihood": 1, "colorFactor": 3}, "C": {"resource": 4, "likelihood": 2, "colorFactor": 4}}};
// modelData = {"nodes": {"x009": {"colorFactor": 3, "likelihood": 1, "resource": 3}, "C": {"colorFactor": 4, "likelihood": 2, "resource": 4}, "city": {"colorFactor": 4, "likelihood": 2, "resource": 4}, "Charlie": {"colorFactor": 3, "likelihood": 1, "resource": 3}, "door": {"colorFactor": 4, "likelihood": 2, "resource": 4}, "Fred": {"colorFactor": 4, "likelihood": 2, "resource": 4}, "x004": {"colorFactor": 2, "likelihood": 1, "resource": 3}, "A1": {"colorFactor": 3, "likelihood": 2, "resource": 3}, "Margrethe": {"colorFactor": 3, "likelihood": 1, "resource": 3}}, "edges": {"A1door": {"colorFactor": 3, "likelihood": 2, "resource": 3}, "citydoor": {"colorFactor": 4, "likelihood": 2, "resource": 4}}};
// modelData = {"nodes": {"x004": {"likelihood": 1, "colorFactor": 2, "resource": 3}, "A1": {"likelihood": 2, "colorFactor": 3, "resource": 3}, "Fred": {"likelihood": 2, "colorFactor": 4, "resource": 4}, "Margrethe": {"likelihood": 1, "colorFactor": 3, "resource": 3}, "C": {"likelihood": 2, "colorFactor": 4, "resource": 4}, "city": {"likelihood": 2, "colorFactor": 4, "resource": 4}, "Charlie": {"likelihood": 1, "colorFactor": 3, "resource": 3}, "door": {"likelihood": 2, "colorFactor": 4, "resource": 4}, "x009": {"likelihood": 1, "colorFactor": 3, "resource": 3}}, "edges": {"citydoor": {"likelihood": 2, "colorFactor": 4, "resource": 4}, "A1city": {"likelihood": 2, "colorFactor": 3, "resource": 3}}};
modelData = {"nodes": {"city": {"colorFactor": 4, "resource": 4, "likelihood": 2}, "x009": {"colorFactor": 3, "resource": 3, "likelihood": 1}, "door": {"colorFactor": 4, "resource": 4, "likelihood": 2}, "x004": {"colorFactor": 2, "resource": 3, "likelihood": 1}, "Fred": {"colorFactor": 4, "resource": 4, "likelihood": 2}, "Margrethe": {"colorFactor": 3, "resource": 3, "likelihood": 1}, "A1": {"colorFactor": 3, "resource": 3, "likelihood": 2}, "Charlie": {"colorFactor": 3, "resource": 3, "likelihood": 1}}, "edges": {"citydoor": {"colorFactor": 4, "resource": 4, "likelihood": 2}, "A1city": {"colorFactor": 3, "resource": 3, "likelihood": 2}}};
drawData = modelData['nodes'];
edgeData = modelData['edges'];
data = {"MODELactors":["Fred","Margrethe","Charlie"],"home":["city"],"A1":["city"],"MODELassets":["STB","x001","x002","REM","x003","x007","C","x004","x010","x011","x008","x009"],"Charlie":["A1"],"MODELnodes":["city","door","bank","home","A1"],"x009":["Margrethe","x004"],"x008":["x004"],"C":["bank"],"door":["home"],"Fred":["city"],"city":["A1","bank","door"],"STB":["home"],"x010":["x007"],"Margrethe":["home"],"REM":["home"],"x001":["A1"],"bank":["city"],"x002":["Margrethe"],"x003":["C"],"x004":["Margrethe"],"x011":["Charlie","x007"],"x007":["Charlie"]};
    locationNodes = data['MODELnodes'];
    for ( var i = 0, l = locationNodes.length; i < l; i++ ) {
      var className = "";
      if(locationNodes[i] in drawData)
      {
        className = "alpha"+drawData[locationNodes[i]]['likelihood']+" color"+drawData[locationNodes[i]]['colorFactor'];
      }
      var info = { data: { id: locationNodes[i] } ,classes: className};
      nodes.push(info);
    // }
    // for ( var i = 0, l = locationNodes.length; i < l; i++ ) {
      for( var j = 0 , m = data[locationNodes[i]].length;j<m;j++)
      {
        var className = "highlighted";
        var edgeID = locationNodes[i]+data[locationNodes[i]][j];
        if(edgeID in edgeData)
        {
          className = "alpha"+edgeData[edgeID]['likelihood']+" color"+edgeData[edgeID]['colorFactor']+" line"+edgeData[edgeID]['resource'];
        }
        // alert(data[locationNodes[i]][j] + " to " + locationNodes[i]);
        var edge = {data: { id: edgeID, source:locationNodes[i], target:data[locationNodes[i]][j] },classes:className};  
        edges.push(edge);
      }
    }
    actorNodes = data['MODELactors'];
    for ( var i = 0, l = actorNodes.length; i < l; i++ ) {
      var className = "";
      if(actorNodes[i] in drawData)
      {
        className = "alpha"+drawData[actorNodes[i]]['likelihood']+" color"+drawData[actorNodes[i]]['colorFactor'];
      }
      var info = { data: { id: actorNodes[i], parent: data[actorNodes[i]][0]  } ,classes: className};
      nodes.push(info);
    }
    assetNodes = data['MODELassets'];
    for ( var i = 0, l = assetNodes.length; i < l; i++ ) { 
      parentList = data[assetNodes[i]];
      if(parentList.length > 1)
      {
          for ( var j = 0, m = actorNodes.length; j < m; j++ ) {
            var index = parentList.indexOf(actorNodes[j]);
            if (index > -1) {
                parentList.splice(index, 1);
            }
          }
      }
      var className = "";
      if(assetNodes[i] in drawData)
      {
        className = "alpha"+drawData[assetNodes[i]]['likelihood']+" color"+drawData[assetNodes[i]]['colorFactor'];
      }  
      var info = { data: { id: assetNodes[i], parent: data[assetNodes[i]][0]  },classes: className };
      nodes.push(info);
    }    
    // alert(JSON.stringify(nodes));
    //  alert(JSON.stringify(edges));
  // })
var elesJson = {}
elesJson['nodes'] = nodes;
elesJson['edges'] = edges;
// alert(JSON.stringify(elesJson));


// var elesJson = {
//   nodes: [
//     { data: { id: 'a'} },
//     { data: { id: 'b'} },
//     { data: { id: 'c'} },
//     { data: { id: 'd'} },
//     { data: { id: 'e'} }
//   ], 

//   edges: [
//     { data: { id: 'ae', weight: 1, source: 'a', target: 'e' } },
//     { data: { id: 'ab', weight: 3, source: 'a', target: 'b' } },
//     { data: { id: 'be', weight: 4, source: 'b', target: 'e' } },
//     { data: { id: 'bc', weight: 5, source: 'b', target: 'c' } },
//     { data: { id: 'ce', weight: 6, source: 'c', target: 'e' } },
//     { data: { id: 'cd', weight: 2, source: 'c', target: 'd' } },
//     { data: { id: 'de', weight: 7, source: 'd', target: 'e' } }
//   ]
// };

var cy = cytoscape({
  container: document.getElementById('cy'),
  
  boxSelectionEnabled: false,
  autounselectify: true,
  
  style: [
    {
      selector: 'node',
      css: {
        'height': 40,
        'width': 40,
        'content': 'data(id)',
        'text-valign': 'center',
        'text-halign': 'center'
      }
    },
    {
      selector: '$node > node',
      css: {
        'padding-top': '10px',
        'padding-left': '10px',
        'padding-bottom': '10px',
        'padding-right': '10px',
        'text-valign': 'top',
        'text-halign': 'center',
        'background-color': '#bbb'
      }
    },
    {
      selector: 'edge',
      css: {
        'target-arrow-shape': 'triangle',
        'line-color': '#ff0000',
        'target-arrow-color': '#ff0000'
      }
    },
    {
      selector: '.alpha1',
      css: {
        'opacity': '0.4',
        'filter': 'alpha(opacity=25)'
      }
    },
    {
      selector: '.alpha2',
      css: {
        'opacity': '0.6',
        'filter': 'alpha(opacity=50)'
      }
    },
    {
      selector: '.alpha3',
      css: {
        'opacity': '0.8',
        'filter': 'alpha(opacity=75)'
      }
    }, 
    {
      selector: '.alpha4',
      css: {
        'opacity': '1',
        'filter': 'alpha(opacity=100)'
      }
    }, 
    {
      selector: '.color1',
      css: {
        'background-color': '#00ff00',
        'line-color': '#00ff00',
        'target-arrow-color': '#00ff00',
      }
    },  
    {
      selector: '.color2',
      css: {
        'background-color': '#55aa00',
        'line-color': '#55aa00',
        'target-arrow-color': '#55aa00',
      }
    }, 
    {
      selector: '.color3',
      css: {
        'background-color': '#aa5500',
        'line-color': '#aa5500',
        'target-arrow-color': '#aa5500',
      }
    },  
    {
      selector: '.color4',
      css: {
        'background-color': '#ff0000',
        'line-color': '#ff0000',
        'target-arrow-color': '#ff0000',
      }
    }, 
    {
      selector: '.line1',
      css: {
        'width': 1,
      }
    }, 
    {
      selector: '.line2',
      css: {
        'width': 2,
      }
    }, 
     {
      selector: '.line3',
      css: {
        'width': 3,
      }
    },
    {
      selector: '.line4',
      css: {
        'width': 4,
      }
    },                              
    {
      selector: '.highlighted',
      css: {
        'background-color': '#000000',
        'line-color': '#000000',
        'target-arrow-color': '#000000',
        'transition-property': 'background-color, line-color, target-arrow-color',
        'transition-duration': '0.5s',
        'opacity': '0.8',
        'filter': 'alpha(opacity=80)'
      }
    },    
    {
      selector: ':selected',
      css: {
        'background-color': 'black',
        'line-color': 'black',
        'target-arrow-color': 'black',
        'source-arrow-color': 'black'
      }
    }
  ],
  
  elements: elesJson,
  
  layout: {
    name: 'concentric',
    concentric: function(){
      return this.data('score');
    },
    levelWidth: function(nodes){
      return 0.5;
    },
    padding: 1
  },
          // layout: {
          //   name: 'concentric',
          //   concentric: function( node ){
          //     return node.degree();
          //   },
          //   levelWidth: function( nodes ){
          //     return 1;
          //   }
          // },
  // layout: {
  //   name: 'breadthfirst',
  //   directed: true,
  //   roots: '#city',
  //   padding: 1
  // },

        //   layout: {
        //   name: 'cose',
        //   padding: 10
        // },
          //     layout: {
          //   name: 'dagre'
          // },   
    ready: function(){
    // ready 1
  }
});

// var bfs = cy.elements().bfs('#a', function(){}, true);
// bfs.find('#ad').addClass('highlighted');
}); // on dom ready