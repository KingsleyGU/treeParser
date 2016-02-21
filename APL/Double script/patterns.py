# ACTOR ACTION ASSETKIND ASSETNAME ASSETID TARGETKIND TARGETNAME TARGETID
# ACTION = In | Out | Move | Exec | Goto | Make |Force

# IN actor ITEM name id LOCATION name id  -- get item from somewhere. Immediate action, no patterns required
# IN actor ITEM name id ACTOR name id -- get item from somebody. Immediate action, no patterns required
# IN actor DATA name id ITEM name id -- get data from item, possible domain-specific patterns
# IN actor ITEM name id ITEM name id -- get item from item, possible domain-specific patterns
# FULFILL actor role <role> -- impersonate some role, possible generic pattern
# MAKE actor victim ACTION -- make someone to execute an action, possible generic pattern
patterns = {

    #########################
    #########################
    # Simple model patterns #
    #########################
    #########################

    ####################
    # Generic patterns #
    ####################
    
    # Make someone do something
    r'MAKE\s(\w+)\s(\w+)\s([\w\s]+)':
    '<node refinement="disjunctive">' + 
        '<label>[0]</label>' + 
        '<node refinement="disjunctive"><label>[1] threatens [2] to execute [3]</label></node>' + 
        '<node refinement="conjunctive">' +
            '<label>[1] blackmails [2]</label>' + 
            '<node refinement="disjunctive"><label>[1] collects some intel about [2]</label></node>' + 
            '<node refinement="disjunctive"><label>[1] blackmails [2] to execute [3]</label></node>' +
        '</node>' + 
        '<node refinement="disjunctive"><label>[1] bribes [2] to execute [3]</label></node>' + 
        '<node refinement="disjunctive">' +
            '<label>[1] socially engineers [2]</label>' + 
            '<node refinement="conjunctive">' + 
                '<label>authority attack</label>' +
                '<node refinement="disjunctive"><label>[1] impersonates authority</label></node>' + 
                '<node refinement="disjunctive"><label>[1] orders [2] to execute [3]</label></node>' + 
            '</node>' +
            '<node refinement="conjunctive">' + 
                '<label>phishing attack</label>' +
                '<node refinement="disjunctive"><label>[1] collects information about [2]</label></node>' +
                '<node refinement="disjunctive"><label>[1] launches a phishing attack targeted at [2] to execute [3]</label></node>' +
            '</node>' + 
        '</node>' + 
        '<node refinement="conjunctive">' +
            '<label>[1] acquires [2] trust and tricks him into executing [3]</label>' +
            '<node refinement="disjunctive"><label>[1] becomes friends with [2]</label></node>' +
            '<node refinement="disjunctive"><label>[1] tricks [2] into executing [3]</label></node>' +
        '</node>' + 
    '</node>', 
    
    
    # Fulfill a role
    r'FULFILL\s(\w+)\srole\s(\w+)':
    '<node refinement="conjunctive">' + 
        '<label>[0]</label>' + 
        '<node refinement="conjunctive"><label>[1] equips with required items to impersonate [2]</label></node>' +
        '<node refinement="conjunctive"><label>[1] impersonates [2]</label></node>' +
    '</node>', 

    #############################
    # Domains-specific patterns #
    #############################    
    
    # Obtain something from laptop
    r'IN\s(\w+)\sDATA\s(\w+)\s\w+\sITEM\s(Laptop)\s\w+':
    '<node refinement="conjunctive">' +
        '<label>[0]</label>' +
        '<node refinement="conjunctive">' +
            '<label>[1] obtains administrator privileges</label>' +
            '<node refinement = "disjunctive">' +
                '<label>[1] bypases authentication in [3]</label>' +
            '</node>' +
            '<node refinement = "disjunctive">' +
                '<label>[1] escalates privileges in [3]</label>' +
            '</node>' +
        '</node>' +
        '<node refinement="disjunctive">' +
            '<label>[1] finds [2] in the file system of [3]</label>' +
        '</node>' +
    '</node>',

    # Obtain something from virtual machine
    r'IN\s(\w+)\sDATA\s(\w+)\s\w+\sITEM\s(VM[0-9])\s\w+':
    '<node refinement="disjunctive">' + 
        '<label>[0]</label>' +
        '<node refinement="conjunctive">' +
            '<label>[1] obtains [2] from the running [3]</label>' +
            '<node refinement="conjunctive">' +
                '<label>[1] obtains administrator privileges</label>' +
                '<node refinement = "disjunctive">' +
                    '<label>[1] bypases authentication in [3]</label>' +
                '</node>' +
                '<node refinement = "disjunctive">' +
                    '<label>[1] escalates privileges in [3]</label>' +
                '</node>' +
            '</node>' +
            '<node refinement="disjunctive">' +
                '<label>[1] finds [2] in the file system of [3]</label>' +
            '</node>' +
        '</node>' +
        '<node refinement="conjunctive">' + 
            '<label>[1] obtains [2] from the drive of [3] directly</label>' +
            '<node refinement="disjunctive"><label>[1] mounts the HD of [3] and inspects it</label></node>' + 
            '<node refinement="disjunctive"><label>[1] finds [2] in the file system of [3]</label></node>' +
        '</node>' +
    '</node>', 

    # Obtain something from virtual machine (extended version)
    r'IN\s(\w+)\sDATA\s(\w+)\s\w+\sITEM\s+.*(VirtualMachine).*\w+':
    '<node refinement="disjunctive">' + 
        '<label>[0]</label>' +
        '<node refinement="conjunctive">' +
            '<label>[1] obtains [2] from the running [3]</label>' +
            '<node refinement="conjunctive">' +
                '<label>[1] obtains administrator privileges</label>' +
                '<node refinement = "disjunctive">' +
                    '<label>[1] bypases authentication in [3]</label>' +
                '</node>' +
                '<node refinement = "disjunctive">' +
                    '<label>[1] escalates privileges in [3]</label>' +
                '</node>' +
            '</node>' +
            '<node refinement="disjunctive">' +
                '<label>[1] finds [2] in the file system of [3]</label>' +
            '</node>' +
        '</node>' +
        '<node refinement="conjunctive">' + 
            '<label>[1] obtains [2] from the drive of [3] directly</label>' +
            '<node refinement="disjunctive"><label>[1] mounts the HD of [3] and inspects it</label></node>' + 
            '<node refinement="disjunctive"><label>[1] finds [2] in the file system of [3]</label></node>' +
        '</node>' +
    '</node>', 


    ##########################
    ##########################
    # Complex model patterns #
    ##########################
    ##########################
    
    # Obtain something from virtual machine
    r'IN\s(\w+)\sDATA\s(\w+)\s\w+\sITEM\s(entity_vim.VirtualMachine_vm-[0-9][0-9])\s\w+':
    '<node refinement="disjunctive">\n' + 
        '<label>[0]</label>\n' +
        '<node refinement="conjunctive">\n' +
            '<label>[1] obtains [2] from the running [3]</label>\n' +
            '<node refinement="conjunctive">\n' +
                '<label>[1] obtains administratorobtains administrator privileges</label>\n' +
                '<node refinement = "disjunctive">\n' +
                    '<label>[1] bypases authentication in [3]</label>\n' +
                '</node>\n' +
                '<node refinement = "disjunctive">\n' +
                    '<label>[1] escalates privileges in [3]</label>\n' +
                '</node>\n' +
            '</node>\n' +
            '<node refinement="disjunctive">\n' +
                '<label>[1] finds [2] in the file system of [3]</label>\n' +
            '</node>\n' +
        '</node>\n' +
        '<node refinement="conjunctive">\n' + 
            '<label>[1] obtains [2] from the drive of [3] directly</label>\n' +
            '<node refinement="disjunctive"><label>[1] mounts the HD of [3] and inspects it</label></node>\n' + 
            '<node refinement="disjunctive"><label>[1] finds [2] in the file system of [3]</label></node>\n' +
        '</node>\n' +
    '</node>\n', 
    
}
